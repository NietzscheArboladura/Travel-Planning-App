from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Person(object):
    "Person Object"
    def __init__(self, fullname, age, gender):
        self.fullName = fullname
        self.age = age
        self.gender = gender


class User:

    _guestList = []

    listLength = 0

    def addUser(self):
        gList = []
        print("This part is where you will be adding the Guests")
        numberOfGuests = int(input("Enter the number of people joining: "))
        print("There are is a total of: "+ str(numberOfGuests) + " guests.")

        for x in range(numberOfGuests):
            guestName = input("Enter the name of Guest no."+ str(x + 1) + ": ")
            guestAge = int(input("Enter the Guest's age: "))
            guestGender = input("Enter the Guest gender [Male/Female/Other]: ")
            self._guestList.append(Person(guestName,guestAge,guestGender))
            gList.append(Person(guestName,guestAge,guestGender))

            self.listLength = len(gList)
            print()
        
        return gList
    
    
    def removeUser(self):
        try:
            print("Remove a Guest -  \nPlease Select the Guest among the list below - ")
            x = 0
            for obj in guestSystem._guestList:
                print("Index no."+ str(x) + " " + obj.fullName)
                x += 1
            guestToRemove = int(input("Enter the Index number of the Guest you want to Remove: "))
            self._guestList.pop(guestToRemove)
        except:
            print("Unexpected Error")
        
    def showUserList(self):
        if(len(self._guestList) > 0):
            print("Current Guests:")
            x = 0
            for obj in self._guestList:
                print("Guest ID."+ str(x) + " " + obj.fullName)
                x += 1
        else:
            print("Currently no Guests")
    
    def userMain(self):
        print("***Fellow Visitors Menu***")
        if(len(self._guestList) == 0):
            print("Currently no people going on the trip, add some.")
            self.addUser()
            self.showUserList()
        else:
            print("There are Currently " + str(self.listLength) + " guests")
            gChoice = int(input("\n1.) Add more Guests\n2.) Remove a Guest\nEnter Choice Here: "))
            if(gChoice == 1):
                self.addUser()
            else:
                self.removeUser()
        

if __name__ == "__main__":
    "MAIN METHOD TO TEST THE GUEST CLASS"
    guestSystem = User()

    guestSystem.userMain()

        

