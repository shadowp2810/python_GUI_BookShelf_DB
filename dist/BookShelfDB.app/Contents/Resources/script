from tkinter import *

import appBackend

def getSelectedRow(event):
    try:
        global selected_tuple
        index = listFromDB.curselection()[0]
        selected_tuple = listFromDB.get(index)
        
        eTitle.delete( 0 , END )    # clears field
        eTitle.insert( END , selected_tuple[1] )    # populates field
        
        eAuthor.delete( 0 , END )
        eAuthor.insert( END , selected_tuple[2] )
        
        eYear.delete( 0 , END )
        eYear.insert( END , selected_tuple[3] )
        
        eISBN.delete( 0 , END )
        eISBN.insert( END , selected_tuple[4] )
    except IndexError: 
        pass
    

def viewCommand():
    listFromDB.delete( 0 , END )        # everything from 0 to end is deleted 
    for row in appBackend.view():
        listFromDB.insert( END , row )      # new lines are inserted end of row
        
def searchCommand():
    listFromDB.delete( 0 , END )       
    for row in appBackend.search(
            title_text.get() ,
            author_text.get() ,
            year_text.get() ,
            iSBN_text.get() ):
        listFromDB.insert( END , row ) 

def addCommand():
    appBackend.insert(
        title_text.get() ,
        author_text.get() ,
        year_text.get() ,
        iSBN_text.get() )
    
    listFromDB.delete( 0 , END )        # clears list   
    for row in appBackend.search(       # populates list with just added and duplicates
            title_text.get() ,
            author_text.get() ,
            year_text.get() ,
            iSBN_text.get() ):
        listFromDB.insert( END , row ) 
        
def updateCommand():
    listFromDB.delete( 0 , END )        # everything from 0 to end is deleted 
    for row in appBackend.view():
        listFromDB.insert( END , row )      # new lines are inserted end of row
    appBackend.update(
        selected_tuple[0] , 
        title_text.get() ,
        author_text.get() ,
        year_text.get() ,
        iSBN_text.get() )
    viewCommand()
        
def deleteCommand():
    appBackend.delete(selected_tuple[0])
    viewCommand()


windowNoFrame = Tk()

windowNoFrame.wm_title("Bookshelf")

window = Frame(
    windowNoFrame , 
    relief = 'sunken' ,
    bd = 1 , 
    bg = '#E5E5E5' )

window.pack( fill = 'both' , expand = True )


lTitle = Label(window, text = "Title" , bg = '#E9E5E5' )
lTitle.grid( 
            row = 0 , column = 0 , 
            pady = ( 4 , 2 ) )

title_text = StringVar()
eTitle = Entry(window, textvariable = title_text)
eTitle.grid( 
            row = 0 , column = 1 , 
            padx = 2 , pady = ( 4 , 2 ) , 
            sticky = 'w' )


lAuthor = Label(window, text = "Author" , bg = '#E9E5E5' )
lAuthor.grid( 
             row = 0 , column = 2 , 
             pady = ( 4 , 2 ) )

author_text = StringVar()
eAuthor = Entry(window, textvariable = author_text )
eAuthor.grid( 
             row = 0 , column = 3 , 
             padx = 10 , pady = ( 4 , 2 ) )


lYear = Label(window, text = "Year" , bg = '#E9E5E5' )
lYear.grid( 
           row = 1 , column = 0, 
           pady = ( 2 , 10 ) )

year_text = StringVar()
eYear = Entry(window, textvariable = year_text )
eYear.grid( 
           row = 1 , column = 1 , 
           padx = 2 , pady = ( 2 , 10 ) , 
           sticky = 'w' )


lISBN = Label(window, text = "ISBN" , bg = '#E9E5E5' )
lISBN.grid( 
           row = 1 , column = 2, 
           pady = ( 2 , 10 ) )

iSBN_text = StringVar()
eISBN = Entry(window, textvariable = iSBN_text )
eISBN.grid( 
           row = 1 , column = 3 , 
           padx = 10 , pady = ( 2 , 10 ) )



listFromDB = Listbox(window, height = 6 , width = 35 )
listFromDB.grid( 
                row = 2 , column = 0 , 
                rowspan = 7 , columnspan = 2 , 
                padx = 10 , pady = 10 , 
                sticky = 'ewns' )

scrollBarForListY = Scrollbar(window)
scrollBarForListY.grid( 
                       row = 2 , column = 2 , 
                       rowspan = 7 , 
                       sticky = 'nsw' )

scrollBarForListX = Scrollbar(window)
scrollBarForListX.grid( 
                       row = 9 , column = 0 , 
                       columnspan = 2 , 
                       sticky = 'ew' )

listFromDB.configure( 
        yscrollcommand = scrollBarForListY.set , 
        xscrollcommand = scrollBarForListX.set )

scrollBarForListY.configure( 
        command = listFromDB.yview , 
        orient = VERTICAL )

scrollBarForListX.configure( 
        command = listFromDB.xview , 
        orient = HORIZONTAL )

listFromDB.bind('<<ListboxSelect>>', getSelectedRow)    #python expects an event to be passed


bViewAll = Button(
    window , 
    text = "View all" , 
    width = 12 ,
    command = viewCommand )
bViewAll.grid( 
              row = 2 , column = 3 , 
              padx = 2 , pady = 2 )

bSearchEntry = Button(
    window , 
    text = "Search entry" , 
    width = 12 ,
    command = searchCommand )
bSearchEntry.grid( 
                  row = 3 , column = 3 , 
                  padx = 2 , pady = 2 )

bAddEntry = Button(
    window , 
    text = "Add entry" , 
    width = 12 ,
    command = addCommand )
bAddEntry.grid( 
               row = 4 , column = 3 , 
               padx = 2 , pady = 2 )

bUpdateEntry = Button(
    window , 
    text = "Update entry" , 
    width = 12 ,
    command = updateCommand )
bUpdateEntry.grid( 
                  row = 5 , column = 3 , 
                  padx = 2 , pady = 2 )

bDeleteEntry = Button(
    window , 
    text = "Delete entry" , 
    fg = 'red' , 
    width = 12 ,
    command = deleteCommand )
bDeleteEntry.grid( 
                  row = 6 , column = 3 , 
                  padx = 2 , pady = 2 )

bClose = Button(
    window , 
    text = "Close" , 
    width = 12 ,
    command = windowNoFrame.destroy )
bClose.grid( 
            row = 7 , column = 3 , 
            padx = 2 , pady = 2 )


window.columnconfigure(4, weight=1)
window.rowconfigure(8, weight=1)

window.mainloop()



