import os

#add more function to allow user to repeat
def add_more():
    again = input('Would you like to go again? ')
    if again in yes_list:
        print()
        main()
    elif again in no_list:
        print("Thanks for using the program.")
        print('Have a nice day!')
        quit()
    else:
        print('You did not provide a valid option.'
              'Please try again')
        input("Press any key to continue...")
        print()
        print()
        add_more()

def main():
 #get file and directory name from user
    fileName = input("Please enter file name:\n")
    directory = input("Please enter directory:\n")
    fileName = f'{fileName}.txt'
     #check if directory exists
    if os.path.isdir(directory):
        completePath = directory + fileName
        name = input("Please enter your name:\n")
        address= input("Please enter your address:\n")
        number= input("Please enter your phone number:\n")
        #append file with new info
        with open(completePath, 'a') as f:
            f.write(name + ', ' + address + ", " + number)
            f.close()
         #read info from file
        with open(completePath, 'r') as f:
            data = f.read()
            print(data)
            f.close()
            add_more()
     #create directory if it does not exist, append with info and read it
    elif not os.path.isdir(directory):
        print("directory not found.")
        print('creating directory...')
        os.mkdir(directory)
    with open(completePath, 'a') as f:
        f.write(name + ', ' + address + ", " + number)
        f.close()
    with open(completePath, 'r') as f:
        data = f.read()
        print(data)
        f.close()
    add_more()


quit_list = ['quit', 'q', 'end', 'no', 'n']
yes_list = ['yes', 'yeah', 'y', 'ok', 'k']
no_list = quit_list

main()

