

catalog=['Pecan', 'Apple Crisp','Bean','Banoffee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Steak']


for pie in catalog:
    print(str([catalog.index(pie)])+' ' + pie)

stopper="n"
shopping_cart=[]

while stopper != 'y':

    order=input("give me your order please")

    shopping_cart.append(order)

    stopper= input('is that all [y/n]')


for buy in shopping_cart:

    print (str(shopping_cart.count(buy))+''+catalog[buy].value)
