import inflect

mylist = []
p = inflect.engine() 

while True:
    try:
        user = input("Name:")
        mylist.append(user)
    except:
        break
        
print (f"Adieu, adieu, to {p.join(mylist)}")
