import random as rand
import csv
import os

global fieldnames
global listLines

fileExists = os.path.isfile("customers.csv")
fieldnames = ["First name", "Last name", "Customer number"]
listLines = []

# Create header
if not fileExists:
    with open("customers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()




# ------Functions------ #

def add():
    if(fileExists):
        with open("customers.csv", "r") as f:
            reader = csv.DictReader(f)
            
            uniqueNumber = rand.randint(10000,99999)
            for line in reader:
                while (uniqueNumber == line["Customer number"]):
                    uniqueNumber = rand.randint(10000,99999)
    else:
        uniqueNumber = rand.randint(10000,99999)

    fname = str(input("First name: "))
    lname = str(input("Last name: "))
    cnumber = str("PBL" + str(uniqueNumber))

    with open("customers.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerow({"First name" : fname, "Last name" : lname, "Customer number" : cnumber})

def get():    
    while(True):
        request = str(input("Request by: fname | lname | cnumber: "))

        with open("customers.csv", "r") as f:
            reader = csv.DictReader(f)
            
            if (request == "fname"):
                fname = str(input("Enter first name: "))
                for line in reader:
                    if (line["First name"] == fname):
                        print(line)
                break

            elif (request == "lname"):
                lname = str(input("Enter last name: "))
                for line in reader:
                    if (line["Last name"] == lname):
                        print(line) 
                break

            elif (request == "cnumber"):
                cnumber = str(input("Customer number: "))
                for line in reader:
                    if (line["Customer number"] == cnumber):
                        print(line) 
                break

def getall():
    with open("customers.csv", "r") as f:
        reader = csv.DictReader(f)

        print("\n\n")
        for line in reader:
            print(line["First name"], line["Last name"], "|", line["Customer number"])
        print("\n\n")

def delete():
    while (True):
        request = str(input("Delete by: fname | lname | cnumber: "))

        with open("customers.csv", "r") as f:
            reader = csv.DictReader(f)

            if (request == "fname"):
                fname = str(input("Enter first name: "))
                for line in reader:
                    listLines.append(line)
                    if (line["First name"] == fname):
                        selectedLine = line
                break

            elif (request == "lname"):
                lname = str(input("Enter last name: "))
                for line in reader:
                    listLines.append(line)
                    if (line["Last name"] == lname):
                        selectedLine = line
                break

            elif (request == "cnumber"):
                cnumber = str(input("Enter customer number: "))
                for line in reader:
                    listLines.append(line)
                    if (line["Customer number"] == cnumber):
                        selectedLine = line
                break
    
    listLines.remove(selectedLine)
    
    with open("customers.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for line in listLines:
            writer.writerow(line)

    listLines.clear()

def deleteall():
    with open("customers.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)  
        writer.writeheader()

# ------Main loop------ #       

while (True):
    command = input("add | get | getall | delete | delall | x: ")
    if (command == "x"):
        break

    if (command == "add"):
        while (True):
            add()
            
            conCheck = input("Add another? y/n: ")
            if(conCheck == "n"):
                break
            else:
                pass
    
    if (command == "get"):
        while (True):
            get()
            
            conCheck = input("Get another? y/n: ")
            if(conCheck == "n"):
                break
            else:
                pass

    if (command == "getall"):
        getall()

    if (command == "delete"):
        while (True):
            delete()

            conCheck = input("Delete another? y/n: ")
            if(conCheck == "n"):
                break
            else:
                pass

    if (command == "delall"):
        deleteall()