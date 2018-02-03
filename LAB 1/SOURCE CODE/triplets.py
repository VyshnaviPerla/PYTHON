def trip(t, n):
    found =False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (t[i] + t[j] + t[k] == 0):
                    print( t[i], t[j], t[k])
                    found = True

    if (found == False):
        print("Triplets not found ")


t = [5,4,9,8,-6,-1,-7,-2,]
n = len(t)
trip(t, n)
