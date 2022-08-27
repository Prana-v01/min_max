#22/04/13
#Pranav.M

max_num = 0
lc = 0
sums = 0
num = 0

while num != -1:
    try:
        num = int(input("numbers: "))
    except ValueError: #Value error would be the only exception raised so we're specifcally looking for that.
        print("error, not an integer!") #instead of crashing the program it will tell the user to input an integer.
    sums += num
    if lc == 0: #this will run once to make the min_num = num this will make the lowest number what the user continuesly inputs instead of a fixed number.
        min_num = num
        print("minimum number is now: ", min_num)
    elif num < min_num and num != -1:
        min_num = num #this updates the minimum to the input thats less then the previous input and not -1
        print("new minimum is: ", min_num) #inform user.
    elif num > max_num and num != -1: #this will dictate the maximum.
        max_num = num
        print("new maximum is: ", max_num)
    lc += 1
print()
print(f"minimum number: {min_num}\nmaximum number: {max_num}")
print("average: ",(sums+1)/(lc-1)) #sum + 1 because when the user enters -1 it counts so i need to add +1
#same logic applies with the loop counter - 1.
