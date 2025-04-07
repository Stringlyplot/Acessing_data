menu = True


def read_file(file_data):
    #this is to open the data
    with open(file_data, "r") as file:
        #Gets rid of excess things
        data = file.readlines(1)
        #prints all the data
        print("HERE >>>>", data)
        #gives user_data a value
        return data
#gives the function a input/vaule
user_data = read_file("input.txt")
#This is to format when printed its not evenlly spread out its all connected in one line
def data_format(format):
    for x in format:
        print(x)
        pass
data_format(user_data)

#Will print out the id and username only
def id_username():
    print("Hello World")
    pass
#This will be the outcome of the 3 options they can pick
menu_options = {1 : id_username, 2 : "2- Print username total before and total after discount", 3 : menu == menu == False}

def menu_choice():
    print("1- Print Transaction ID and username\n2- Print username total before and total after discount\n3- Quit")
    return

while menu == True:
    menu_choice()
    decision = int(input(">>> "))
    menu_options[decision]()

    

