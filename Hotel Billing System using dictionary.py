'''Hotel billing system 

id      item      quantity    price   bill
1       poha        2          20      40
2       tea         5          10      50
3       pizza       1          200     200

total price=290  
''' 
db={1:"Poha",2:"Tea",3:"Pizza",4:"Sandwich",5:"Coffee"}
price={1:25,2:10,3:200,4:30,5:15}

items=[]
quantity=[]

while True:
    print("---- AAPL HOTEL----")
    print(""" 
          1.Poha
          2.Tea
          3.Pizza
          4.Sandwich
          5.Coffee""")
    i=int(input("Enter no of items:"))
    q=int(input("Enter no of quantity:"))
    items.append(i)
    quantity.append(q)
    print(items)
    print(quantity)
    c=input("Do you want to continue:(Y/N):")
    if c=='n':
        print("-"*105)
        print("Print Bill")
        print("-"*105)
        sum=0
        for i in range(len(items)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|" .format(i+1,db[items[i]],quantity[i],price[items[i]],quantity[i]*price[items[i]]))
            sum=sum+quantity[i],price[items[i]]
        print("Your total bill is",sum)