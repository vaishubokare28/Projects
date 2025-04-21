db={1:{"name":"john","city":"pune","percentage":78,"course":"python"}}

# db[roll]['name']="john"
#db[roll]['course']="python"
print("-"*80)
print(" "*30,"The Kiran Academy ")
print("-"*80)

while True:
    print(""" 
        1.Create record
        2.Display record
        3.Update record
        4.Delete record  
    """)
    i=int(input("Enter choice="))
    if i==1:
        details={}
        roll=int(input("Enter rollno= "))#2
        name=input("Enter name= ") #blake
        city=input("Enter city= ") #mumbai
        percentage=int(input("Enter percentage")) #75
        course=input("Enter course=")#java
     
        #varname[key]=value
        details['name']=name  #name:blake
        details['city']=city #city:mumbai
        details['percentage']=percentage #percentage:75
        details['course']=course # course:java
       
        db[roll]=details
        #print(db)

    elif i==2:
      print("-"*106)
      print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("roll","name","city","percentage","course"))
      print("-"*106)

      for roll in db:
          print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll,db[roll]['name'],db[roll]['city'], db[roll]['percentage'],db[roll]['course']))

    elif i==3:
        
        roll=int(input("Enter rollno= "))
        print("""1.Name
        2.city
        3.percentage
        4.course """)
        c=int(input("Enter your choice="))
        if c==1:
            un=input("Enter name= ")  #Harish
            # db[2]['name']=Harish
            db[roll]['name']=un
            print("Record updated sucessfully")

        elif c==2:
            uc=input("enter city=")  #Nagar
            #db[2]['city']='Nagar'
            db[roll]['city']=uc
            print("Record updated successfully")
        elif c==3:
            up=int(input("Enter percentage= "))
            db[roll]['percentage']=up
            print("Record updated successfully")
        elif c==4:
            uc=input("enter course= ")
            db[roll]['course']=uc
            print("record updated successfully")
        else:
            print("Invalid choice")


    elif i==4:
        roll=int(input("Enter roll= "))
        del db[roll]
        print("Recored delete Successfully")
    else:
        print("Invalid choice")