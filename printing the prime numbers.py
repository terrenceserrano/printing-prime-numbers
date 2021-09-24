#Create a program that will print the prime numbers in a range of numbers

#input of the user for the range of the input

n = int(input("Enter the range of numbers here: "))

#use a for loop for the number in the range in the format for "item name" in "arguement"

for num in range(n):
    if num > 1: #this is the start of the count
        #this is the condition for the prime
        for i in range(2, num): #we introduced, i, as integer and the range starts from 2 to the range num
            if (num % i) == 0: #we use modulus here to check if the condition is satisfied to continue the loop
                break #this is to break the loop
        else:
            print(num)