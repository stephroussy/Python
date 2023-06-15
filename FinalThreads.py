"""Name of program: FinalThreads.py
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

import logging
from time import sleep
from threading import Thread

logging.basicConfig(filename = 'construction.log', level=logging.INFO, format= "%(threadName)s:")

class RemodelSquare(Thread):
    def __init__(self):
# printing supplies priced per square footage
        Thread.__init__(self, name = "remodel")
        file1 = open('remodel.txt', 'r')
        lines = file1.readlines()
        self.changes = []
        self.item = []
        self.wholesalePrice = []
        self.retailPrice = []
        self.monthlyOrders = []
        for line in lines:
            words = line.split("|")
            
            self.item.append(words[0])
            self.wholesalePrice.append(words[2])
            self.retailPrice.append(float(words[1]))
            self.monthlyOrders.append(int(words[3]))
    def run(self):
        logging.info("The items sold per square footage are being read")
        sleep(1)
# manager program reading items charged per square footage
    def managerSquareOptions (self):
        self.changes = ""
        for i in range(len(self.item)):
            self.changes += ("%-3s %-30s %-15s %-17s %-50s \n"%(str(i + 1), self.item[i], "${:,.2f}".format(float(self.wholesalePrice[i])), "${:,.2f}".format(float(self.retailPrice[i])), str(self.monthlyOrders[i])))
        return self.changes
# add item to supplies sold per square footage
    def addSquare(self, newItem, newWholesale, newRetail):
        file1 = open('remodel.txt', 'w')
        self.newItem = newItem
        self.newWholesale = newWholesale
        self.newRetail = newRetail
        self.item.append(self.newItem)
        self.wholesalePrice.append(self.newWholesale)
        self.retailPrice.append(float(self.newRetail))
        self.monthlyOrders.append(0)
        self.updates = ""
        for i in range(len(self.item)):
            self.updates = "%s|%s|%s|%s\n"%(self.item[i], self.retailPrice[i], self.wholesalePrice[i], self.monthlyOrders[i])
            file1.write(self.updates)
# delete item from supplies sold per square footage
    def deleteSquare(self, selection):
        file1 = open('remodel.txt', 'w')
        self.selection = selection
        self.item.pop(int(self.selection) - 1)
        self.wholesalePrice.pop(int(self.selection) - 1)
        self.retailPrice.pop(int(self.selection) - 1)
        self.monthlyOrders.pop(int(self.selection) - 1)
        self.updates = ""
        for i in range(len(self.item)):
            self.updates = "%s|%s|%s|%s\n"%(self.item[i], self.retailPrice[i], self.wholesalePrice[i], self.monthlyOrders[i])
            file1.write(self.updates)
# update retail price for supplies sold per square footage
    def updateSquarePrice(self, selection, newPrice):
        file1 = open('remodel.txt', 'w')
        self.selection = selection
        self.newPrice = newPrice
        self.retailPrice[int(self.selection) - 1] = float(self.newPrice)
        self.updates = ""
        for i in range(len(self.item)):
            self.updates = "%s|%s|%s|%s\n"%(self.item[i], self.retailPrice[i], self.wholesalePrice[i], self.monthlyOrders[i])
            file1.write(self.updates) 
# customer program for supplies sold per square footage
    def customerSquareOptions (self):
        self.changes = ""
        for i in range(len(self.item)):
            self.changes += ("%-3s %-30s %-10s \n"%(str(i + 1), self.item[i], "${:,.2f}".format(float(self.retailPrice[i]))))
        return self.changes
# providing option for customer to sort items sold per square footage to sort from cheapest to most expensive
    def SquareSorter(self):
        self.changes=""
        n=len(self.item)
        for i in range(0,n,1):
            for j in range(0,n-1-i,1):
                if self.retailPrice[j]>self.retailPrice[j+1]:
                    temp=self.item[j]
                    self.item[j]=self.item[j+1]
                    self.item[j+1]=temp
                    temp=self.wholesalePrice[j]
                    self.wholesalePrice[j]=self.wholesalePrice[j+1]
                    self.wholesalePrice[j+1]=temp
                    temp=self.retailPrice[j]
                    self.retailPrice[j]=self.retailPrice[j+1]
                    self.retailPrice[j+1]=temp
                    temp=self.monthlyOrders[j]
                    self.monthlyOrders[j]=self.monthlyOrders[j+1]
                    self.monthlyOrders[j+1]=temp
            
            
        for i in range(len(self.item)):
            self.changes+=("%-3s %-30s %-10s \n"%(str(i + 1), self.item[i], "${:,.2f}".format(float(self.retailPrice[i]))))
        return self.changes
    
class RemodelFlat(Thread):
    def __init__(self):
# printing supplies sold at a flat rate
        Thread.__init__(self, name = "remodel")
        file1 = open('utilities.txt', 'r')
        lines = file1.readlines()
        self.flatchanges = []
        self.flatitem = []
        self.flatwholesalePrice = []
        self.flatretailPrice = []
        self.flatmonthlyOrders = []
        for line in lines:
            words = line.split("|")
            
            self.flatitem.append(words[0])
            self.flatwholesalePrice.append(words[2])
            self.flatretailPrice.append(float(words[1]))
            self.flatmonthlyOrders.append(int(words[3]))
    def run(self):
        logging.info("The items sold at a flat rate are being read")
        sleep(1)
# manager program reading items with a flat rate
    def managerFlatOptions (self):
        self.flatchanges = ""
        for i in range(len(self.flatitem)):
            self.flatchanges += ("%-3s %-29s %-14s %-17s %-50s \n"%(str(i + 1), self.flatitem[i], "${:,.2f}".format(float(self.flatwholesalePrice[i])), "${:,.2f}".format(float(self.flatretailPrice[i])), str(self.flatmonthlyOrders[i])))
        return self.flatchanges
# add item to supplies sold at a flat rate
    def addFlat(self, newItem, newWholesale, newRetail):
        file1 = open('utilities.txt', 'w')
        self.newItem = newItem
        self.newWholesale = newWholesale
        self.newRetail = newRetail
        self.flatitem.append(self.newItem)
        self.flatwholesalePrice.append(self.newWholesale)
        self.flatretailPrice.append(float(self.newRetail))
        self.flatmonthlyOrders.append(int(0))
        self.flatupdates = ""
        for i in range(len(self.flatitem)):
            self.flatupdates = "%s|%s|%s|%s\n"%(self.flatitem[i], self.flatretailPrice[i], self.flatwholesalePrice[i], self.flatmonthlyOrders[i])
            file1.write(self.flatupdates)
# delete item from supplies sold at a flat rate
    def deleteFlat(self, selection):
        file1 = open('utilities.txt', 'w')
        self.selection = selection
        self.flatitem.pop(int(self.selection) - 1)
        self.flatwholesalePrice.pop(int(self.selection) - 1)
        self.flatretailPrice.pop(int(self.selection) - 1)
        self.flatmonthlyOrders.pop(int(self.selection) - 1)
        self.flatupdates = ""
        for i in range(len(self.flatitem)):
            self.flatupdates = "%s|%s|%s|%s\n"%(self.flatitem[i], self.flatretailPrice[i], self.flatwholesalePrice[i], self.flatmonthlyOrders[i])
            file1.write(self.flatupdates)
# update retail price for supplies sold at a flat rate
    def updateFlatPrice(self, selection, newPrice):
        file1 = open('utilities.txt', 'w')
        self.selection = selection
        self.newPrice = newPrice
        self.flatretailPrice[int(self.selection) - 1] = float(self.newPrice)
        self.flatupdates = ""
        for i in range(len(self.flatitem)):
            self.flatupdates = "%s|%s|%s|%s\n"%(self.flatitem[i], self.flatretailPrice[i], self.flatwholesalePrice[i], self.flatmonthlyOrders[i])
            file1.write(self.flatupdates) 
# customer program reading items with a flat rate
    def customerFlatOptions (self):
        self.flatchanges = ""
        for i in range(len(self.flatitem)):
            self.flatchanges += ("%-3s %-22s %-10s \n"%(str(i + 1), self.flatitem[i], "${:,.2f}".format(float(self.flatretailPrice[i]))))
        return self.flatchanges

# providing option for customer to sort items sold at a flat rate to sort from cheapest to most expensive
    def FlatSorter(self):
        self.flatchanges=""
        n=len(self.flatitem)
        for i in range(0,n,1):
            for j in range(0,n-1-i,1):
                if self.flatretailPrice[j]>self.flatretailPrice[j+1]:
                    temp=self.flatitem[j]
                    self.flatitem[j]=self.flatitem[j+1]
                    self.flatitem[j+1]=temp
                    temp=self.flatwholesalePrice[j]
                    self.flatwholesalePrice[j]=self.flatwholesalePrice[j+1]
                    self.flatwholesalePrice[j+1]=temp
                    temp=self.flatretailPrice[j]
                    self.flatretailPrice[j]=self.flatretailPrice[j+1]
                    self.flatretailPrice[j+1]=temp
                    temp=self.flatmonthlyOrders[j]
                    self.flatmonthlyOrders[j]=self.flatmonthlyOrders[j+1]
                    self.flatmonthlyOrders[j+1]=temp

        for i in range(len(self.flatitem)):
            self.flatchanges+=("%-3s %-30s %-10s \n"%(str(i + 1), self.flatitem[i], "${:,.2f}".format(float(self.flatretailPrice[i]))))
        return self.flatchanges
     
# calculating estimate for customer based on items selected
class CalcEst(Thread):
    def __init__(self):
        Thread.__init__(self, name = "Calculate Estimate")
        RemodelSquare.__init__(self)
        RemodelFlat.__init__(self)
        global estimate
        self.estimate = 0

    def run(self):
        logging.info("Creating an estimate for the customer")
        sleep(1)

# calculating estimate using the items needed to multiply by square footage
    def createEst(self, num, sqr):
        file1 = open('remodel.txt', 'w')
        self.num = num
        self.sqr = sqr
        self.beforeEstimate = 0
        sqrPrice = float(self.retailPrice[(num) - 1])
        self.monthlyOrders[int(num) - 1] += 1
        self.beforeEstimate += (sqrPrice * sqr)
        self.updates = ""
        for i in range(len(self.item)):
            self.updates = "%s|%s|%s|%s\n"%(self.item[i], self.retailPrice[i], self.wholesalePrice[i], self.monthlyOrders[i])
            file1.write(self.updates)

    def before(self):
        return self.beforeEstimate
# calculating estimate adding the items multiplied by square footage to those priced at a flat rate
    def addFlat(self, num):
        file1 = open('utilities.txt', 'w')
        self.num = num
        self.flatSum = 0
        flatPrice = float(self.flatretailPrice[(num) - 1])
        self.flatmonthlyOrders[(num) - 1] += 1
        self.flatSum += (flatPrice)
        self.flatupdates = ""
        for i in range(len(self.flatitem)):
            self.flatupdates = "%s|%s|%s|%s\n"%(self.flatitem[i], self.flatretailPrice[i], self.flatwholesalePrice[i], self.flatmonthlyOrders[i])
            file1.write(self.flatupdates)

    def estimation(self):
        self.estimate = (self.flatSum + self.beforeEstimate)
        return self.estimate
    
# form created for customers who want a precise estimate       
class Quote(Thread):
    def __init__(self):
        Thread.__init__(self, name = "Quote")
        RemodelSquare.__init__(self)
        RemodelFlat.__init__(self)
        CalcEst.__init__(self)

    def run(self):
        logging.info("The customer is asking for a quote")
        sleep(1)

    def receive(self, first, last, phone, email):
        file3 = open('quote.txt', 'a')
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        formList = {"First Name": self.first, "Last Name": self.last, "Phone Number": self.phone, "Email":self.email}
        for (key,value) in formList.items():
            file3.write("%-28s %-28s \n"%(key,value))

global myRemodelSquare
myRemodelSquare = RemodelSquare()
global myRemodelFlat
myRemodelFlat = RemodelFlat()
global myCalcEst
myCalcEst = CalcEst()
global myQuote
myQuote = Quote()

myRemodelSquare.start()
myRemodelFlat.start()
myCalcEst.start()
myQuote.start()

myRemodelSquare.join()
myRemodelFlat.join()
myCalcEst.join()
myQuote.join()
