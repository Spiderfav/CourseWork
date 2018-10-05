import os
import getpass
admin_usr = 0

def input_usr():
        #Ask the user their useruser
        user = input("Enter useruser: ")
        try:
                # Look for their file user
                os.path.isfile(user+".txt")
                load_usr( user )
        except IOError:
                #If not found, say user not found
                print("User not found!")
                #Go to create a user
                create_usr()




def load_usr( user ):

        #Read the file and check if admin or not
        global admin_usr
        #Set the admin usr global
        in_file = open(user+".txt")
        read_text = in_file.read()
        #print (read_text)
        in_file.close()

        for line in read_text:
                try:
                        if '1' in line:
                            #If 1 is in their file input the pswd
                            print ("What is the password?")
                            password = getpass.getpass('Password:')
                            if password == "Admin":
                               #If they input correct pswd set admin to 1
                               print ("You are my primary user!")
                               admin_usr = 1
                               break
                            else:
                                #Else send them to input usr
                                print ("Password Incorrect.")
                                input_usr()
                                break

                        elif '2' in line:
                            #If 2 in line then admin set 2
                            print ("You are my secondary user!")
                            admin_usr = 2
                            break


                except IOError:
                    print("User not found!")
                    create_usr()
                    pass

def create_usr():

    #Ask the user if they want an account
    print ("You don't have an account. Do you want to create one?")
    answer = input()
    #If not:
    if answer.upper() == "NO":
            #Set them to guest user
            print ("You are now a guest user.")
            print ("To create an account after, follow steps restart and types in user.")

    #If answer is yes:
    elif answer.upper() == "YES":
            #Ask their user
            user = input("Type your user in here please: ")
            #Create file
            out_file = open(user+".txt", "wt")
            out_file.write("2")
            out_file.close()

            print ("Hello "+ user +".I have set you as my secondary user.")
