import os 
import shutil
def to_do_list():
    Events = 0
    while Events !=4:
        print("\n---WELCOME TO THE TO DO LIST---")
        print("1.Append to the list")
        print("2.Read the list")
        print("3.Clear the list")
        print("4.Exit the list")
        try:
          Events = int(input("what do you wish to do ?"))
        except ValueError:
            print("Please write a viable number(1-4)")
        if Events == 1:
            date = input("Enter the date for the to do ? ")
            time = input("Enter the time for the to do ? ")
            things = input("Enter the to do: ")
            with open ('to_do_list.txt','a') as f:
                 f.write(f"{date}: {time}: {things}" +'\n')

        elif  Events ==2:
            with open('to_do_list.txt','r') as f:
                 content = f.read()
                 print(content)

        elif Events ==3:
            with open('to_do_list.txt','w') as f:
                 f.write("")

to_do_list()           

