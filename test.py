x=int(input())
y=int(input())
count = 0               # Initialize count value as a '0'

while (True):                         # use while loop to print infinite pattern
    if count == 0:                  # If count value is 0 then it print the value of 'y' for 'x' time
        print(x, end=',')
        for i in range(x):
            print(y, end=',')
        count = count+1             # increase count for the proper pattern

    elif (count < y+1) and (count > 0):   # It use to print the 'y' value for 'y' times starting with 'x' up to 'y' Times
        print(x, end=',')
        for i in range(y):
            print(y, end=',')
        count = count+1

    elif count == (y+1):        # If count value is equal to (y+1) then initialize count to zero
        count = 0               # Initialize counter to zero to print pattern in proper manner