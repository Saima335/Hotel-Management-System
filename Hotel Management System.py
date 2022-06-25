#creating an empty dictionary
guest={}
#define function that add the record of system
def add_guest():
    while True:
        try:
            #prompt the user to enter the guest ID
            G_ID=eval(input("enter the guest ID: "))
            if G_ID in guest.keys():
                print("this guest ID already exist..enter new guest ID")
                G_ID=eval(input("enter the guest ID: "))
            break
        except:
            print("something wrong in the input")
    #prompt the user to enter the guest name
    name=input("enter the guest name: ")
    while True:
        try:
            #prompt the user to enter the guest age
            age=eval(input("enter the guest age in years: "))
            while age<=0:
                print("invalid age..again input the age")
                age=eval(input("enter the guest age in years: "))
            break
        except:
            print("something wrong in the input")
    #prompt the user to enter the guest contact number
    contactNo=input("enter the guest contact number: ")
    #adding elements in the dictionary
    guest[G_ID]=[name,age,contactNo]
#define function that view the record of system
def view_guest():
    #if addchk is 1 the record will exist
    if guest:
        #display the heading of the table
        print("guest id\t guest name\tguest age\tguest contact number")
        #for each key of the dictioanry
        for k in guest.keys():
            #make a lsit of the elements in each key
            lstguest=guest[k]
            #display the contents of the dictionary
            print("  ",k,"\t\t" , lstguest[0],"    \t",lstguest[1],"\t\t",lstguest[2])
    #if addchk is not 1
    else:
        #display no record was entered 
        print("No record exist")
#define function that search the guest record
def search_guest():
    #if addchk is 1 the record will exist
    if guest:
        while True:
            try:
                #prompt the user to enter the guest ID he want to search the record for
                search=eval(input("enter the guest ID you want to search: "))
                break
            except:
                print("something wrong in the input")
        #no guest ID is found here so found become false
        found=False
        #for each key of the dictioanry
        for k in guest.keys():
            #if search is present in the dictionary,guest
            if search in guest:
                #make the list of elements of each key of the dictionary,guest
                lstguest=guest[k]
                #guest ID is found here so found become true
                found=True
                #break the loop
                break
        #if searched element is found in dictionary
        if found==True:
            #display record is found
            print("record found")
            #display the heading of the table
            print("guest id\t guest name\tguest age\tguest contact number")
            #display the contents of the dictionary
            print("  ",search,"\t\t" , lstguest[0],"    \t",lstguest[1],"\t\t",lstguest[2])
        #if searched element is not found in the dictionary
        else:
            #display record is not found
            print("record not found")
    #if addchk is not 1
    else:
        #display no record was entered
        print("No record exist")
#define function that edit the guest record
def edit_guest():
    #if addchk is 1
    if guest:
        while True:
            try:
                #prompt the user to enter the guest ID for which he want to edit the record
                edit=eval(input("enter the guest ID for which you want to edit the record: "))
                break
            except:
                print("something wrong in the input")
        #no guest ID is found here so found become false
        found=False
        #for each key in dictionary
        for k in guest.keys():
            #if guest ID for which you want to edit record exist in the dictioanry
            if edit in guest:
                #prompt the user to enter the new name of the guest
                new_name=input("enter the updated name of the guest: ")
                #prompt the user to enter the new age of the guest
                new_age=eval(input("enter the updated age of the guest: "))
                #prompt the user to enter the new contact number of the guest
                new_contactNo=input("enter the updated contact number of the guest: ")
                #make a new list of the key new elements for which the record is edited
                guest[edit]=[new_name,new_age,new_contactNo]
                #guest ID is found here so found become true
                found=True
                #break the loop
                break
        #if element you want the record to be edited for is found in dictionary
        if found==True:
            #display the record is edited
            print("record is edited")
            #display the heading of the table 
            print("guest id\t guest name\tguest age\tguest contact number")
            #for each key of dictioanry
            for k in guest.keys():
                #make a list of each of the elements of teh list 
                lstguest=guest[k]
                #print the contents of the table
                print("  ",k,"\t\t" , lstguest[0],"    \t",lstguest[1],"\t\t",lstguest[2])
        #if element which you want to edit is not found in the dictionary
        else:
            #display no such element exist
            print("no such guest ID exit for which the record is to be deleted")
    #if addchk is not 1
    else:
        #dispaly no record was entered
        print("No record exist")
    
#define function that delete the guest record
def delete_guest():
    #if addchk is 1
    if guest:
        while True:
            try:
                #prompt the user to enter the guest ID for which he want to delete the record
                delete=eval(input("enter the guest ID for which you want to delete the record: "))
                break
            except:
                print("something wrong in the input")
        #no guest ID is found here so found become false
        found=False
        #for each key of the dictioanry
        for k in guest.keys():
            #if deleted element is present in dictionary
            if delete in guest:
                #make the list of elements of each key of the dictionary,guest
                lstguest=guest[k]
                #guest ID is found here so found become true
                found=True
                #break the loop
                break
        #if element you want to delete is found in dictionary
        if found==True:
            #del that specific key 
            del guest[delete]
            #display the record is deleted
            print("record is deleted")
            #print the heading of the table
            print("guest id\t guest name\tguest age\tguest contact number")
            #for each key of dictionary
            for k in guest.keys():
                #make the list of elements of each key of the dictionary,guest
                lstguest=guest[k]
                #print the body of the table
                print("  ",k,"\t\t" , lstguest[0],"    \t",lstguest[1],"\t\t",lstguest[2])
        #if element which you want to delete is not found in the dictionary
        else:
            #display no such ID exist
            print("no such ID exist for which the record is to be deleted")
    #if addchk is not 1
    else:
        #display no record was entered
        print("No record exist")
#define a function that displays the menu
def menu1():
    while True:
        #print the heading of menu
        print("Hotel management system:-")
        while True:
            try:
                #prompt the user to enter the function he want to perform 
                menu1=eval(input("1) add guest \n2)view guest \n3)search guest \n4)edit guest \n5)delete guest \n6)exit \nenter your choice"))
                break
            except:
                print("something wrong in the input")
        #if user enters 1
        if menu1==1:
            #call the add function
            add_guest()
        #if user enters 1
        elif menu1==2:
            #call the view function
            view_guest()
        #if user enters 1
        elif menu1==3:
            #call the search function
            search_guest()
        #if user enters 1
        elif menu1==4:
            #call the edit function
            edit_guest()
        #if user enters 1
        elif menu1==5:
            #call the delete function
            delete_guest()
        #if user enters 1
        elif menu1==6:
            #break the loop and exit 
            break
        #if user enters anything other than 1 to 6
        else:
            #print enter number from 1 to 6
            print("invalid input,please enter a number from 1 to 6")

#creating an empty dictionary
room={}
#define function that add the record of system
def add_room():
    while True:
        try:
            #prompt the user to enter the room ID
            R_ID=eval(input("enter the room ID: "))
            if R_ID in room.keys():
                print("this room ID already exist..enter new room ID")
                R_ID=eval(input("enter the room ID: "))
            break
        except:
            print("something wrong in the input")
    while True:
        try:
            #prompt the user to enter the room floorNumber
            floorNumber=eval(input("enter the room floorNumber: "))
            break
        except:
            print("something wrong in the input")
    #prompt the user to enter the room heating
    while True:
        heating=input("enter the room heating: ")
        if heating.lower()=="yes" or heating.lower()=="no":
            break
        else:
            print("enter yes or no")
    #prompt the user to enter the room furniture type
    while True:
        furnitureType=input("enter the room furniture type: ")
        if furnitureType.isalpha():
            break
        else:
            print("enter a string")
    #adding elements in the dictionary
    room[R_ID]=[floorNumber,heating,furnitureType]
#define function that view the record of system
def view_room():
    #if addchk is 1 the record will exist
    if room:
        #display the heading of the table
        print("room id\t room floorNumber\troom heating\troom contact number")
        #for each key of the dictioanry
        for k in room.keys():
            #make a lsit of the elements in each key
            lstRmoom=room[k]
            #display the contents of the dictionary
            print("  ",k,"\t\t" , lstRmoom[0],"    \t",lstRmoom[1],"\t\t",lstRmoom[2])
    #if addchk is not 1
    else:
        #display no record was entered 
        print("No record exist")
#define function that search the room record
def search_room():
    #if addchk is 1 the record will exist
    if room:
        while True:
            try:
                #prompt the user to enter the room ID he want to search the record for
                search=eval(input("enter the room ID you want to search: "))
                break
            except:
                print("something wrong in the input")
        #no room ID is found here so found become false
        found=False
        #for each key of the dictioanry
        for k in room.keys():
            #if search is present in the dictionary,room
            if search in room:
                #make the list of elements of each key of the dictionary,room
                lstRmoom=room[k]
                #room ID is found here so found become true
                found=True
                #break the loop
                break
        #if searched element is found in dictionary
        if found==True:
            #display record is found
            print("record found")
            #display the heading of the table
            print("room id\t room floorNumber\troom heating\troom contact number")
            #display the contents of the dictionary
            print("  ",search,"\t\t" , lstRmoom[0],"    \t",lstRmoom[1],"\t\t",lstRmoom[2])
        #if searched element is not found in the dictionary
        else:
            #display record is not found
            print("record not found")
    #if addchk is not 1
    else:
        #display no record was entered
        print("No record exist")
#define function that edit the room record
def edit_room():
    #if addchk is 1
    if room:
        while True:
            try:
                #prompt the user to enter the room ID for which he want to edit the record
                edit=eval(input("enter the room ID for which you want to edit the record: "))
                break
            except:
                print("something wrong in the input")
        #no room ID is found here so found become false
        found=False
        #for each key in dictionary
        for k in room.keys():
            #if room ID for which you want to edit record exist in the dictioanry
            if edit in room:
                #prompt the user to enter the new floorNumber of the room
                new_floorNumber=input("enter the updated floorNumber of the room: ")
                #prompt the user to enter the new heating of the room
                new_heating=eval(input("enter the updated heating of the room: "))
                #prompt the user to enter the new contact number of the room
                new_furnitureType=input("enter the updated furniture type of the room: ")
                #make a new list of the key new elements for which the record is edited
                room[edit]=[new_floorNumber,new_heating,new_furnitureType]
                #room ID is found here so found become true
                found=True
                #break the loop
                break
        #if element you want the record to be edited for is found in dictionary
        if found==True:
            #display the record is edited
            print("record is edited")
            #display the heading of the table 
            print("room id\t room floorNumber\troom heating\troom contact number")
            #for each key of dictioanry
            for k in room.keys():
                #make a list of each of the elements of teh list 
                lstRmoom=room[k]
                #print the contents of the table
                print("  ",k,"\t\t" , lstRmoom[0],"    \t",lstRmoom[1],"\t\t",lstRmoom[2])
        #if element which you want to edit is not found in the dictionary
        else:
            #display no such element exist
            print("no such room ID exit for which the record is to be deleted")
    #if addchk is not 1
    else:
        #dispaly no record was entered
        print("No record exist")
    
#define function that delete the room record
def delete_room():
    #if addchk is 1
    if room:
        while True:
            try:
                #prompt the user to enter the room ID for which he want to delete the record
                delete=eval(input("enter the room ID for which you want to delete the record: "))
                break
            except:
                print("something wrong in the input")
        #no room ID is found here so found become false
        found=False
        #for each key of the dictioanry
        for k in room.keys():
            #if deleted element is present in dictionary
            if delete in room:
                #make the list of elements of each key of the dictionary,room
                lstRmoom=room[k]
                #room ID is found here so found become true
                found=True
                #break the loop
                break
        #if element you want to delete is found in dictionary
        if found==True:
            #del that specific key 
            del room[delete]
            #display the record is deleted
            print("record is deleted")
            #print the heading of the table
            print("room id\t room floorNumber\troom heating\troom contact number")
            #for each key of dictionary
            for k in room.keys():
                #make the list of elements of each key of the dictionary,room
                lstRmoom=room[k]
                #print the body of the table
                print("  ",k,"\t\t" , lstRmoom[0],"    \t",lstRmoom[1],"\t\t",lstRmoom[2])
        #if element which you want to delete is not found in the dictionary
        else:
            #display no such ID exist
            print("no such ID exist for which the record is to be deleted")
    #if addchk is not 1
    else:
        #display no record was entered
        print("No record exist")
#define a function that displays the menu
def menu2():
    while True:
        #print the heading of menu
        print("Hotel Management system:-")
        while True:
            try:
                #prompt the user to enter the function he want to perform 
                menu2=eval(input("1) add room \n2)view room \n3)search room \n4)edit room \n5)delete room \n6)exit \nenter your choice"))
                break
            except:
                print("something wrong in the input")
        #if user enters 1
        if menu2==1:
            #call the add function
            add_room()
        #if user enters 1
        elif menu2==2:
            #call the view function
            view_room()
        #if user enters 1
        elif menu2==3:
            #call the search function
            search_room()
        #if user enters 1
        elif menu2==4:
            #call the edit function
            edit_room()
        #if user enters 1
        elif menu2==5:
            #call the delete function
            delete_room()
        #if user enters 1
        elif menu2==6:
            #break the loop and exit 
            break
        #if user enters anything other than 1 to 6
        else:
            #print enter number from 1 to 6
            print("invalid input,please enter a number from 1 to 6")
#creating empty dictionary
roomReserve={}
#creating empty list which is global and will add all reserved room
lstR=[]
lstG=[]
#defining def function
def add_roomReserve():
    #checking is their is data in guest and room dictionaries
    if guest and room:
        while True:
            #checking i if in room keys
            for i in room.keys():
                if i in lstR:
                    #if i is been found in lstR list allRR will become true
                    allRR=True
                    #will skip this statement and return to for loop
                    continue
                else:
                    #if its false it will exit the loop
                    allRR=False
                    break
            for j in guest.keys():
                if j in lstG:
                    found=True
                    continue
                else:
                    found=False
                    break
            if found==True and allRR==True:
                print("all rooms are reserved and all guests have also reserved the room")
                break
            if allRR==True:
                #if found is equal to true display rooms are reserved
                print("all rooms are reserved")
                break
            if found==True:
                print("all guests have reserved one rooms")
                break
            while True:
                try:
                    #ask user to enter guest id
                    y=eval(input("enter ID of guest for whom you want to reserve the room: "))
                    break
                except:
                    #in except statement tell user that something is wrong in your input
                    print("something wrong in the input")
            #checking guest id in guest keys
            if y in guest.keys():
                if y in lstG:
                    print("this guest has already reserved the room")
                    continue
                else:
                    lstG.append(y)
                    while True:
                        while True:
                            try:
                                #ask user to tell the room id you want to reserve
                                x=eval(input("enter ID of the room you want to reserve: "))
                                break
                            except:
                                #in except statement tell user that something is wrong in your input
                                print("something wrong in the input")
                        #if room id is found in room keys
                        if x in room.keys():
                            if x in lstR:
                                #display that all your rooms are reserved
                                print("the room is already reserved..please enter another room ID")
                                continue
                            else:
                                lstRoom=room[x]
                                #append the entered room id in list lstR
                                lstR.append(x)
                                #equalizing room id to lstRm
                                R_ID=x
                                #equalizing guest id to guests asked for room reservation
                                G_ID=y
                                #enter the date when room is reserved
                                date=input("enter the date when room is reserved: ")
                                while True:
                                    try:
                                        #ask user to enter the room reservation id
                                        RR_ID=eval(input("enter the room reservation id: "))
                                        #if RR_id id present in roomrevervation keys
                                        if RR_ID in roomReserve.keys():
                                            #display the room id is reserved you should enter another key
                                            print("this room reservation ID already exist..enter new room reservation ID")
                                            #again ask for the room reservation id
                                            RR_ID=eval(input("enter the room reservation id: "))
                                        break
                                    except:
                                        print("something wrong in the input")
                                #giving list as a value to dictionary key
                                roomReserve[RR_ID]=[R_ID,G_ID,date,lstRoom[1]]
                                #display you room or rooms are reserved
                                print("your room/rooms is reserved now")
                                break
                        else:
                            #display your room or rooms are reserved
                            print("no such room exist")
                            continue
            else:
                #display no such record exist
                print("no such guest exist for whom you want to reserve the room")
                continue
            break
    else:
        if not guest:
            #no record for in guest dictionary exist
            print("enter the guest record first")
        if not room:
            #no record for in guest dictionary exist
            print("enter the room record first")
            
    
def view_roomReserve():
    
    #checking if record for roomreservation for guest for room exist
    if roomReserve and guest and room :
        #display record in tabular form
        print("room reserve ID\t room ID's\t guest ID\t assigning date\t room heating")
        for i in roomReserve.keys():
            lstRoomreserve=roomReserve[i]
            #printing data in tabular form
            print(i,"\t         ",lstRoomreserve[0],"      \t",lstRoomreserve[1],"        \t",lstRoomreserve[2],"\t        ",lstRoomreserve[3])
    else:
        if not roomReserve:
            #display the room reservation record doesnot exist
            print("enter the room reservation record")
        if not guest:
            #display the guest record doesnot exist
            print("enter the guest record first")
        if not room:
            #display the room record doesnot exist
            print("enter the room record first")
def menu3():
    while True:
        #print the heading of menu
        print("Hotel Management system:-")
        while True:
            try:
                #prompt the user to enter the function he want to perform 
                menu3=eval(input("1) add room reservation \n2)view room reservation \n3)exit\nenter your choice" ))
                break
            except:
                print("something wrong in the input")
        #if user enters 1
        if menu3==1:
            #call the add function
            add_roomReserve()
        #if user enters 1
        elif menu3==2:
            #call the view function
            view_roomReserve()
        elif menu3==3:
            #break the loop and exit 
            break
        #if user enters anything other than 1 to 3
        else:
            #print enter number from 1 to 6
            print("invalid input,please enter a number from 1 to 3")
def menu():
    while True:
        #print the heading of menu
        print("Hotel Management system:-")
        while True:
            try:
                #prompt the user to enter the function he want to perform 
                check=eval(input("1)guest menu \n2)room menu  \n3)room reservation menu \n4)exit \nenter your choice" ))
                break
            except:
                print("something wrong in the input")
        #if user enters 1
        if check==1:
            #call the add function
            menu1()
        #if user enters 1
        elif check==2:
            #call the view function
            menu2()
        elif check==3:
            menu3()
        elif check==4:
            #break the loop and exit 
            break
        #if user enters anything other than 1 to 3
        else:
            #print enter number from 1 to 6
            print("invalid input,please enter a number from 1 to 4")
menu()
