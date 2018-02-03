#list of students who are enrolled in python
list11 = ['chandu', 'shivani', 'anusha', 'sri']
print("Python Students")
print(list11)
#list of students who are enrolled in web
list12 = ['manoja', 'sphurthy', 'hari', 'chandu', 'shivani', 'anusha', 'bhargavi']
print("Web Students")
print(list12)
#print the students who are common in both the classes
print("Students in both python and web classes are: ")
for a in list11:
    if a in list12:
        print(a)

#students who are enrolled in either of the classes
print("Students in either of web development or python are:")

#odd one's out from the first list
for b in list11:
    if b not in list12:
        print(b)
#odd one's out from the second list
for c in list12:
    if c not in list11:
        print(c)
