import os
import shutil

def write_a_diary_notes_file():
    diary = 0
    while diary != 4:
      print("\n ---WELCOME TO YOUR DIARY---\n")
      print("1. Write/overwrite to your diary")
      print("2.Append to your diary")
      print("3.Read your diary")
      print("4.Exit diary")
      try:
         diary = int(input("what do you want to do ? "))
      except ValueError:
          print("Please enter a viable number (1-4)")
      if diary == 1:
            with open('diary.txt','w') as f:
                 things =input("Ok I'm ready lay it on me\n")
                 f.write(things +'\n')


      elif diary == 2:
            with open('diary.txt','a') as f:
                 things = input("Ok I'm ready lay it on me\n") 
                 f.write(things + '\n')


      elif diary == 3:
            with open('diary.txt','r') as f:
                 content = f.read()
                 print(content)

      elif diary ==4:
           print("We hope you were relieved")
           print("Goodbye and take care")
           print("We hope to see you again")          
write_a_diary_notes_file()
#print("your diary is ready")
#print("enjoy")
#print("If problems arise take it up with my creator")
