import numpy as np
x = np.random.randint(0, 20, 15)
#create an array of size 15 in range 0-20
print("Given List:")
#prints the list of elements in the array
print(x)
print("Most frequent value:")
#gives most frequent value in the list
print(np.bincount(x).argmax())