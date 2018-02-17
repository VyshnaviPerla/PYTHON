contact_list = [{"name":'vyshu', "number":7205498, "email":"lpgxp@mail.umkc.edu"},{"name":"manu", "number":9010511222, "email":"manojagadde1105@gmail.com"},{"name":"sphurthy","number":8886266688,"email":"spoon@gmail.com"}]
# enter name to get details
nm = input("Enter name to get contact: ")
# checks the complete list
for i in contact_list:
# 'if condition' for checking the name is in the dictionary or not
    if nm in i.values():
# if true print
        print(i)
# enter number to get details
num = int(input("Enter number to get contact: "))
# checks the complete list
for j in contact_list:
# 'If condition' for checking the entered number is in dictinary or not
    if num in j.values():
# if true print
        print(j)
# enter the name if you want to edit the number
nme = input("Enter name to get contact and edit number: ")
# checks the complete list
for k in contact_list:
# If the entered name in dictionary
    if nme in k.values():
# Print the contact
        print(k)
# edit the number of the contact
        newnum = int(input("Enter number to edit: "))
# Editing the number
        k["number"] = newnum
# Print the contact
        print(k)