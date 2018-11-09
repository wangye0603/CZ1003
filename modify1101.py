#search by food category function
from tkinter import *
import tkinter.messagebox
from operator import itemgetter



#database
#food court name[0] / food name[1] / review marks[2] / average price[3]
canteeninfo = [["Food Court 1","chicken rice",3.5,3],
               ["Food Court 1","ban mian",3,4],
               ["Food Court 1","seafood",3.5,15],
               ["Food Court 1","xiaolongbao",4,10],
               ["Food Court 2","chicken rice",3.6,3.2],
               ["Food Court 2​","ban mian",2.6,3],
               ["Food Court 2","seafood",4,17],
               ["Food Court 2","xiaolongbao",4.3,14],
               ["Food Court 14","chicken rice",4,3.8],
               ["Food Court 14","ban mian",3,4.1],
               ["Food Court 14","seafood",3.9,10],
               ["Food Court 14","xiaolongbao",3.8,12],
               ["North Hill Food Court","chicken rice",3.5,4],
               ["North Hill Food Court","ban mian",3,3.5]]


root = Tk()#main GUI
root.title("FoodKoala")#rename
root.minsize(width=300,height=300)#make default size
topFrame = Frame(root)#top frame
topFrame.pack()
bottomFrame = Frame(root)#bottom frame
bottomFrame.pack(side=BOTTOM)




#quit button, show warning on click, choose yes to quit
def qt (event):
    box_qt = tkinter.messagebox.askquestion("warning","are u sure u wanna leave?")
    if box_qt == "yes":
        global root
        root.destroy()

#get the value of search box
def retrieve ():
    var = entry_srch.get()
    return var

#show srch results in textbox
def srch(event):
    text="Search results for '"+ retrieve()+"' :"


    listresult = food.search(canteeninfo,retrieve())
    abc = text +"\n\n"+ str(listresult)
    txt_srch.delete("1.0",END)
    txt_srch.insert(END,abc)
    
def sortbyrank(event):
    text="Search results for '"+ retrieve()+"' :"
    listresult = food.search(sort_rank,retrieve())
    abc = text +"\n\n"+ str(listresult)
    txt_srch.delete("1.0",END)
    txt_srch.insert(END,abc)

def sortbyprice(event):
    text="Search results for '"+ retrieve()+"' :"
    listresult = food.search(sort_price,retrieve())
    abc = text +"\n\n"+ str(listresult)
    txt_srch.delete("1.0",END)
    txt_srch.insert(END,abc)

'''
def sort(event):
    arrange = sorted(canteeninfo,key=itemgetter(attr_no))
    return arrange
'''

class food:
    def __init__(self,canteen,name,marks,price,distance):
        self.c = canteen
        self.n = name
        self.m = marks
        self.p = price
        self.d = distance
    #enter the raw list, return a sorted list by index
    def sortby(attr_no):
        arrange = sorted(canteeninfo,key=itemgetter(attr_no))
        return arrange
    #enter a list and keyword, return items containing keyword.
    def search(thislist,keyword):
        textlist = []
        for eachlist in thislist:
            if keyword in eachlist[1]:
                textlist.append(eachlist)
        return textlist


'''



#popup a new window
def newwindow (event):
    leaf = Tk()
    leaf.title("FoodKoala-search by food")#rename
    leaf.minsize(width=300,height=300)#make default size
   # leaf.maxsize(width=300,height=300)
    topFrame_leaf = Frame(leaf)
    topFrame_leaf.pack()
    bottomeFrame_leaf = Frame(leaf)
    bottomeFrame_leaf.pack(side=BOTTOM)
    button_Rank = Button(topFrame_leaf,text="sort by rank")
    button_Rank.pack(side=TOP)
    button_Price = Button(topFrame_leaf,text="sort by price")
    button_Price.pack(side=TOP)
    button_Distance = Button(topFrame_leaf,text="sort by distance")
    button_Distance.pack(side=TOP)

    labelresult = Label(topFrame_leaf,text="Search results for '"+ retrieve()+"' :")
    labelresult.pack(side=TOP)
    
    listresult = food.search(sort_marks,retrieve())
    labelresult = Label(topFrame_leaf,text= listresult)
    labelresult.pack(side=TOP)



    
    leaf.mainloop()

    

    button_Rank.bind("<Button-1>",byrank(labelresult))
    button_Price.bind("<Button-1>",byprice(labelresult))
    button_Distance.bind("<Button-1>",bydistance)



'''

#main page design
entry_srch = Entry(topFrame)
entry_srch.pack()

sort_marks = food.sortby(2)#sort by review
sort_rank = sort_marks[::-1]#sort by rank
sort_price = food.sortby(3)#sort by price




#srch_marks = food.search(sort_marks,retrieve())#searched items in list


button_srch = Button(topFrame,text="Search by food category")
button_srch.pack()
button_srch.bind("<Button-1>",srch)#call srch event on click


button_Rank = Button(topFrame,text="sort by rank")
button_Rank.pack(side=LEFT)
button_Rank.bind("<Button-1>",sortbyrank)
button_Price = Button(topFrame,text="sort by price")
button_Price.pack(side=LEFT)
button_Price.bind("<Button-1>",sortbyprice)



txt_srch = Text(bottomFrame,height=12,width=30)
txt_srch.pack()

button_qt = Button(bottomFrame,text="Quit")
button_qt.pack()
button_qt.bind("<Button-1>",qt)#call qt on click





root.mainloop()
