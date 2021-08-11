numbers = input()
j = 0
if (not numbers.isnumeric()):
    print('Bukan Angka')
else:
    for i in numbers:
        j += int(i)
        for l in range(0,int(i)):
            if(int(i)%2 == 1):
                print("#",end="")
            elif(int(i)%2 == 0):
                print("@",end="")
        if(j>=5):
            print("$",end="\n")
            j = 0
        else:
            print(end="\n")