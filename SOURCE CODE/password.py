#user should enter the password

print("Enter the password:")
a=input()

#password should be in the given range

x=len(a)
if x>6:
    if x<16:
        print("password in range")
    else:
        print("password should be in range 6-16 characters")

#password should contain atleast one numeric value

q=0
for c in a:
    if c.isdigit():
        print("password contains a numeric value")
        q=1
        break
if q==0:
    print("Numeric value missing")

#password should contain atleast one special character

b=0
while b==0:
    if '$' in a:
        print("password contains a special character")
        break
    elif '@' in a:
        print("password contains a special character")
        break
    elif '!' in a:
        print("password contains a special character")
        break
    elif '*' in a:
        print("password contains a special character")
        break
    else:
        print("Special character missing")
        break

#password should contain a lower case

r=0
for c in a:
    if c.islower():
        print("password contains a lower case")
        r=1
        break
if r==0:
    print("lowercase missing")

#password should contain an upper case

s=0
for c in a:
    if c.isupper():
        print("password contains an upper case")
        s=1
        break
if s==0:
    print("uppercase missing")