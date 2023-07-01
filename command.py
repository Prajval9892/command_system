#----------------for exit----------------#

if command=="exit":
    conf=input("Are you sure y/n")
    if conf=="y":
        print("bye!")
        return "red"
#---------------if list is empty-----------#

        
elif command=="list":
    if len(my_list)==0:
        print("Nothing to list!")
    else:
        for i in range(len(my_list)):
            if i+1 in mark_list:
                print("[X]",str(i+1)+"."+str(my_list[i]))
            else:
                print("[]",str(i+1)+"."+str(my_list[i]))
            
#-----------------add Done command---------------#
elif command[:4]=="done":
    mark=int(command[4:])
    mark_list.append(mark)
    print(command)
            
            
            



#---------------For add command-----------------#
elif command[:3]=="add":
    my_list.append(command[3:len(command)])
   
    
#---------------For invalid command-------------#

else:
    print("OOPS! unknown command")
