#initialise the different types of books
bookdict = dict([("web technologies",50),("software engineering",60),("database",55),("computer networks",65),("statistical learning",68),("java",70)])
#prints the list of books
print("List of books in store:")
for k,v in bookdict.items():
    print(k,v)
#prints the book name with its cost
print("Enter the range of cost to find the books")
start = int(input("Enter the starting limit:"))
last = int(input("Enter the ending limit"))
for name,val in bookdict.items():
    if val >= start and val <= last:
#prints the list of books in the given range
        print("Books available in the given cost",name)