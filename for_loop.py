## Number Chain Excersice
##Number Chain
#Chain up the numbers

#Instructions
#Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.

#After the results have printed ask the user if they would like to continue.

#If "y", restart the process, starting at 0 again.

#If "n", exit the chain.

#Bonus
#Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.




answer= 'y'

total=0

while answer == 'y':

    numbers=int(input('How many numbers'))

    n=total

    numbers+= total

    while n<numbers:

        print(n)
        n+=1

    total = numbers
    answer=input('Do you want to play again? (y/n)')
