"""Name of program: FinalProject_2322663.py
   Author of program: Stephanie Roussy
   Last date program was modified: 11/27/21
   Summary of the program's intent: To create
   a GUI interface and associated methods,
   classes, files, and threads for clients
   and managers of the construction company.
   This program includes concepts such as loops,
   text files (read and write), lists and
   dictionaries, functions, images, classes and
   objects, multithreading, and at least one
   search and sort algorithm."""

from breezypythongui import EasyFrame

import turtle
turtle.hideturtle()
tr = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=1400, height=800)
wn.bgpic('logo.gif')
wn.mainloop()
         

from FinalThreads import *

class construction(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "QuickFix Remodeling")
        self.setSize(width = 1300, height = 760)
        self.theSum = 0.0

        # greeting
        self.addLabel (text = "Welcome to QuickFix", row = 0, column = 1, sticky = "E")
        self.addLabel (text = "                                                                         With over 30 years of experience, QuickFix is a one stop shop for kitchen remodeling", row = 1, column = 1, columnspan = 3)
        # select manager or customer program
        self.manager = self.addButton(text = "Manager's Program", row = 2, column = 1, command = self.openSupplies)
        self.customer = self.addButton(text = "Customer's Program", row = 2, column = 2, command = self.kitchenSupplies)
        global myRemodelSquare
        myRemodelSquare = RemodelSquare()
        global myRemodelFlat
        myRemodelFlat = RemodelFlat()
        global myCalcEst
        myCalcEst = CalcEst()
        global myQuote
        myQuote = Quote()
##########  reading manager's supplies   ##########
        
    def openSupplies(self):
        self.customer["state"] = "disabled"
        self.addLabel (text = "Kitchen Remodeling Needs", row = 3, column = 2, sticky = "W", columnspan = 2)
        self.addLabel (text = "The following items are sold by square footage:", row = 4, column = 2, sticky = "W", columnspan = 2)
        self.addLabel (text = "      Item Name                                  Wholesale Price       Retail Price         Monthly Orders", row = 5, column = 1)
        self.outputsquare = self.addTextArea("", row = 6, column = 2, width = 80, height = 15)
        self.addLabel (text = "The following items are sold at a flat rate:", row = 4, column = 1, sticky = "W", columnspan = 2)
        self.addLabel (text = "      Item Name                                  Wholesale Price       Retail Price         Monthly Orders", row = 5, column = 2)
        self.flatArea = self.addTextArea("", row = 6, column = 1, width = 80, height = 15)
        self.outputsquare.setText(myRemodelSquare.managerSquareOptions())
        self.flatArea.setText(myRemodelFlat.managerFlatOptions())
        self.buttons()

##########  adding items to flat rate options  ##########
        
    def addFlatItem(self):
        self.addFlatButton.destroy()
        self.addLabel(text = "Enter item name:", row = 8, column = 1, columnspan = 2, sticky = "W")
        self.itemFlatName = self.addTextField(text = "", row = 8, column = 1, width = 5, sticky = "NS")
        self.addLabel(text = "Enter item's wholesale price: ", row = 9, column = 1, columnspan = 2, sticky = "W")
        self.addFlatWholesale = self.addIntegerField(value = "", row = 9, column = 1, width = 5, sticky = "NS")
        self.addLabel(text = "Enter item's retail price: ", row = 10, column = 1, columnspan = 2, sticky = "W")
        self.addFlatRetail = self.addIntegerField(value = "", row = 10, column = 1, width = 5, sticky = "NS")
        self.addButton(text = "Add item to supplies", row = 11, column = 1, command = self.addFlat)

##########   adding new item to utilities.txt file #########
    def addFlat(self):
        myRemodelFlat.addFlat(self.itemFlatName.getText(), self.addFlatWholesale.getValue(), self.addFlatRetail.getValue())
        self.openSupplies()
        self.addFlatbutton.destroy()

##########  deleting menu items   ##########

    def deleteFlatItem(self):
        self.deleteFlatButton.destroy()
        self.addLabel(text = "     Enter item number to delete:       ", row = 13, column = 1, sticky = "W")
        self.deleteFlatNumber = self.addIntegerField(value = "", row = 13, column = 1, width = 5, sticky = "NS")
        self.addButton(text = "Delete item from supplies", row = 14, column = 1, command = self.Flatdelete)

##########  deleting item from utilities.txt file #########
    def Flatdelete(self):
        myRemodelFlat.deleteFlat(self.deleteFlatNumber.getValue())
        self.openSupplies()
        self.deleteFlatButton.destroy()
       
##########  updating retail prices   ##########

    def updateFlatItem(self): 
        self.updateFlatButton.destroy()
        self.addLabel(text = "        Enter item number to be updated:          ", row = 16, column = 1, sticky = "W")
        self.inputFlatUpdate = self.addIntegerField(value = "", row = 16, column = 1, width = 5, sticky = "NS")
        self.addLabel(text = "       Enter the item's new retail price:        ", row = 17, column = 1, sticky = "W")
        self.newFlatPrice = self.addFloatField(value = "", row = 17, column = 1, width = 5, sticky = "NS")
        self.addButton(text = "Save price update", row = 18, column = 1, command = self.updateFlat)

###### updating price in utilities.txt file ########
    def updateFlat(self):
        myRemodelFlat.updateFlatPrice(self.inputFlatUpdate.getValue(), self.newFlatPrice.getValue())
        self.openSupplies()
        self.updateFlatButton.destroy()

##########  adding items to square footage options  ##########
        
    def addSquareItem(self):
        self.addSquareButton.destroy()
        self.addLabel(text = "Enter item name:", row = 8, column = 2, sticky = "W")
        self.itemSquareName = self.addTextField(text = "", row = 8, column = 2, width = 5, sticky = "NS")
        self.addLabel(text = "Enter item's wholesale price: ", row = 9, column = 2, sticky = "W")
        self.addSquareWholesale = self.addIntegerField(value = "", row = 9, column = 2, width = 5, sticky = "NS")
        self.addLabel(text = "Enter item's retail price: ", row = 10, column = 2, sticky = "W")
        self.addSquareRetail = self.addIntegerField(value = "", row = 10, column = 2, width = 5, sticky = "NS")
        self.addButton(text = "Add item to supplies", row = 11, column = 2, command = self.addSquare)

##########   adding newe item to remodel.txt file #########
    def addSquare(self):
        myRemodelSquare.addSquare(self.itemSquareName.getText(), self.addSquareWholesale.getValue(), self.addSquareRetail.getValue())
        self.openSupplies()
        self.addSquareButton.destroy()

##########  deleting square footage items   ##########

    def deleteSquareItem(self):
        self.deleteSquareButton.destroy()
        self.addLabel(text = "   Enter item number to be deleted: ", row = 13, column = 2, sticky = "W")
        self.deleteSquareNumber = self.addIntegerField(value = "", row = 13, column = 2, width = 5, sticky = "NS")
        self.addButton(text = "Delete item from supplies", row = 14, column = 2, command = self.deleteSquare)

##########  deleting square footage items from remodel.txt file #########
    def deleteSquare(self):
        myRemodelSquare.deleteSquare(self.deleteSquareNumber.getValue())
        self.openSupplies()
        self.deleteSquareButton.destroy()
       
##########  updating retail prices   ##########

    def updateSquareItem(self): 
        self.updateSquareButton.destroy()
        self.addLabel(text = "Enter item number to be updated: ", row = 16, column = 2, sticky = "W")
        self.inputSquareUpdate = self.addIntegerField(value = "", row = 16, column = 2, width = 5, sticky = "NS")
        self.addLabel(text = "Enter the item's new retail price: ", row = 17, column = 2, sticky = "W")
        self.newSquarePrice = self.addFloatField(value = "", row = 17, column = 2, width = 5, sticky = "NS")
        self.addButton(text = "Save price update", row = 18, column = 2, command = self.updateSquare)
        
########### updating prices in remodel.txt file #########
    def updateSquare(self):
        myRemodelSquare.updateSquarePrice(self.inputSquareUpdate.getValue(), self.newSquarePrice.getValue())
        self.openSupplies()
        self.updateSquareButton.destroy()

 ##########  manager program button options   ##########
    def buttons(self):
        self.addFlatButton = self.addButton(text = "Add Item", row = 7, column =1, command = self.addFlatItem)
        self.deleteFlatButton = self.addButton(text = "Delete Item", row = 12, column = 1, command = self.deleteFlatItem)
        self.updateFlatButton = self.addButton(text = "Update Price", row = 15, column = 1, command = self.updateFlatItem)
        self.exitButton = self.addButton(text = "Exit Program", row = 19, column = 1, command = self.quitmanager)
        self.addSquareButton = self.addButton(text = "Add Item", row = 7, column =2, command = self.addSquareItem)
        self.deleteSquareButton = self.addButton(text = "Delete Item", row = 12, column = 2, command = self.deleteSquareItem)
        self.updateSquareButton = self.addButton(text = "Update Price", row = 15, column = 2, command = self.updateSquareItem)

##########  reading customer's Supply Options   ##########

    def kitchenSupplies(self):
        self.manager["state"] = "disabled"
        self.addLabel (text = "                                                                                                                           Kitchen Remodeling Needs", row = 3, column = 1, columnspan = 3)
        self.addLabel (text = "List 1 offers items sold by square footage:", row = 4, column = 1, sticky = "W", columnspan = 2)
        self.addLabel (text = "     Item Name                                       Retail Price", row = 5, column = 1)
        self.outputsquare = self.addTextArea("", row = 6, column = 1, width = 80, height = 15)
        self.addLabel (text = "List 2 offers items sold at a flat rate:", row = 4, column = 2, sticky = "W", columnspan = 2)
        self.addLabel (text = "     Item Name                          Retail Price", row = 5, column = 2)
        self.flatArea = self.addTextArea("", row = 6, column = 2, width = 80, height = 15)
        self.click = self.addLabel (text = "   Click the button below to calculate an estimate for items found in list 1 by inputting a square footage       ", row = 7, column = 1)
        self.startsquareorder = self.addButton(text = "Calculate Estimate", row = 8, column =1, command = self.squareStartEst)
        self.outputsquare.setText(myRemodelSquare.customerSquareOptions())
        self.flatArea.setText(myRemodelFlat.customerFlatOptions())
        self.addButton(text = "     Exit Program    ", row = 14, column = 2, command = self.quitcustomer)
        
##########  Allowing customer to add items to create estimate from list 1 supplies   ##########

    def squareStartEst(self):
        self.click.config(text="")
        self.startsquareorder.destroy()
        self.enterList = self.addLabel(text = "Enter item # from list 1: ", row = 8, column = 1, sticky = "W")
        self.custItem = self.addIntegerField(value = "", row = 8, column = 1, width = 5, sticky = "NS")
        self.cheapest = self.addLabel(text = "Click the sort button to list items from cheapest to most expensive", row = 8, column = 2, sticky = "W")
        self.footage = self.addLabel(text = "Enter square footage of surface for item: ", row = 9, column = 1, sticky = "W")
        self.custSqr = self.addIntegerField(value = "", row = 9, column = 1, width = 5, sticky = "NS")
        self.sorting = self.addButton(text = "Sort", row = 9, column = 2, command = self.sorter)
        self.addItem = self.addButton(text = "Add item", row = 10, column = 1, command = self.addToSquare)
        self.finished = self.addLabel(text = "Once finished adding all desired items from list 1 click continue ", row = 11, column = 1, sticky = "W")
        self.continued = self.addButton(text = "Continue", row = 12, column =1, command = self.continuing)

########## Sort items from cheapest to most expensive ##########
        
    def sorter(self):
        self.cheapest.destroy()
        self.sorting.destroy()
        self.flatArea.setText(myRemodelFlat.FlatSorter())
        self.s=RemodelSquare()
        self.L=self.s.SquareSorter()
        self.outputsquare.setText(self.L)
        
##########  Allowing customer to add items to create estimate from list 2 supplies   ##########

    def flatStartEst(self):
        self.list2.destroy()
        self.finish.destroy()
        self.enterList = self.addLabel(text = "Enter list 2 item # to add for estimate:           ", row = 8, column = 1, sticky = "W")
        self.custItem = self.addIntegerField(value = "", row = 8, column = 1, width = 5, sticky = "NS")
        self.twoadd = self.addButton(text = "Add item", row = 9, column = 1, command = self.AddListTwo)
        self.desired = self.addLabel(text = "Once finished adding all the desired items, click Finish & Estimate Price ", row = 10, column = 1, sticky = "W")
        self.finish2 = self.addButton(text = "Calculate Estimated Price", row = 11, column =1, command = self.EstimateTwo)

##########  Multiplying square footage by price for list 1   ##########
    def addToSquare(self):
        num = int(self.custItem.getNumber())
        sqr = int(self.custSqr.getNumber())
        myCalcEst.createEst(num, sqr)
        myCalcEst.before()
        self.custItem.setNumber(0)
        self.custSqr.setNumber(0)

##########  Displaying Customer's Estimate   ##########
    def continuing(self):
        self.enterList.config(text="")
        self.custItem.destroy()
        self.footage.config(text="")
        self.custSqr.destroy()
        self.finished.config(text="")
        self.addItem.destroy()
        self.continued.destroy()
        self.click.config(text="")
        self.list2 = self.addButton(text = "Add additional items from list 2", row = 8, column =1, command = self.flatStartEst)
        self.finish = self.addButton(text = "Skip List 2 & Estimate Price", row = 9, column =1, command = self.EstimateOne)
        
########## Calculating Estimate   ##########

    def AddListTwo(self):
        num2 = int(self.custItem.getNumber())
        myCalcEst.addFlat(num2)
        self.custItem.setNumber(0)

########## Calculating Estimate Using Only List 1   ##########

    def EstimateOne(self):
        self.finish.destroy()
        self.one = self.addLabel(text = "* Please note that the following estimate is an approximation and not a guarantee *", row = 8, column = 1, sticky = "W")
        self.enterList = self.addLabel(text = "Considering the items you added, your estimate = $%0.2f" %myCalcEst.before(), row = 9, column = 1, sticky = "W")
        self.enterList2 = self.addLabel(text = "For a more accurate quote from our professionals fill out the following form:", row = 10, column = 1, sticky = "W")
        self.forming()

########## Calculating Estimate Using Both Lists   ##########

    def EstimateTwo(self):
        self.enterList.config(text="")
        self.custItem.destroy()
        self.twoadd.destroy()
        self.desired.config(text="")
        self.finish2.destroy()
        self.one = self.addLabel(text = "* Please note that the following estimate is an approximation and not a guarantee *", row = 8, column = 1, sticky = "W", rowspan = 2)
        self.enterList = self.addLabel(text = "Considering the items you added, your estimate = $%0.2f" %myCalcEst.estimation(), row = 10, column = 1, sticky = "W", rowspan = 2)
        self.enterList2 = self.addLabel(text = "For a more accurate quote from our professionals fill out the following form:", row = 12, column = 1, sticky = "W", rowspan = 2)
        self.forming()

########## Create form for customer to recieve quote   ##########
        
    def forming(self):
        self.enterfirst = self.addLabel(text = "Enter First name:", row = 14, column = 1, columnspan = 2, sticky = "W")
        self.first = self.addTextField(text = "", row = 14, column = 1, width = 20, sticky = "NS")
        self.enterlast = self.addLabel(text = "Enter Last name:", row = 15, column = 1, columnspan = 2, sticky = "W")
        self.last = self.addTextField(text = "", row = 15, column = 1, width = 20, sticky = "NS")
        self.enterphone = self.addLabel(text = "Enter Phone number:", row = 16, column = 1, columnspan = 2, sticky = "W")
        self.phone = self.addTextField(text = "", row = 16, column = 1, width = 20, sticky = "NS")
        self.enteremail = self.addLabel(text = "Enter email:", row = 17, column = 1, columnspan = 2, sticky = "W")
        self.email = self.addTextField(text = "", row = 17, column = 1, width = 20, sticky = "NS")
        self.quote = self.addButton(text = "Submit Contact Information", row = 19, column =1, command = self.sendQuote)
        
########## Sending Quote to Manager   ##########

    def sendQuote(self):
        self.quote.destroy()
        self.list2.destroy()
        self.enterfirst.config(text="")
        self.first.destroy()
        self.enterlast.config(text="")
        self.last.destroy()
        self.enterphone.config(text="")
        self.phone.destroy()
        self.enteremail.config(text="")
        self.email.destroy()
        self.one.config(text="")
        self.enterList.config(text="")
        self.enterList2.config(text="") 
        myQuote.receive(self.first.getText(), self.last.getText(), self.phone.getText(), self.email.getText())
        self.addLabel(text = "Thank you for choosing Quick Fix for your kitchen remodel", row = 8, column = 1, columnspan = 2, sticky = "W")
        self.addLabel(text = "One of our certified professionals will be reaching out to you shortly", row = 9, column = 1, columnspan = 2, sticky = "W")

##########  Quit Programs   ##########
    def quitmanager(self):
        exit()

    def quitcustomer(self):
        exit()
        
def main():
    construction().mainloop()

if __name__ == "__main__":
    main()

       






       





        





       






       





        



