


candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]


for candy in candyList:

    print(str([candyList.index(candy)])+' ' + candy)

allowance=int(input("your allowance"))

n=1
candycart=[]

while n <= allowance:

    selected_item=int(input("Select Item"))
        
    candycart.append( candyList[selected_item])

    n=n+1
    
print(candycart)






