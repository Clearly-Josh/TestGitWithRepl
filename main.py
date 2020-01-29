def showMem():
  #here are our column numbers for our memory display
  print("     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15")
  print("-----------------------------------------------------------------------------------")
  print("0 ",ram0)
  print("1 ",ram1)
  print("2 ",ram2)
  print("3 ",ram3)
  print("4 ",ram4)
  print("5 ",ram5)
  print("6 ",ram6)
  print("7 ",ram7)
  print("-----------------------------------------------------------------------------------")

#and here is the empty matrix of arrays, making up our representation of RAM
#testing master branch
ram0 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ram7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

file1=["A","l","l","_","w","e","_","h","a","v","e","_","t","o","_","d"]
file2=["e","c","i","d","e","_","i","s","_","w","h","a","t","_","t","o"]
storage=[file1,file2]

a=1
while a<6:
  print("")
  print("Welcome to the world's freaking best Memory Simulator.")
  print("")
  print("1 - View the current memory state!")
  print("2 - Load a program or file, obviously.")
  print("3 - Let's edit a file in memory.")
  print("4 - Can we delete a file?")
  print("5 - Time to save and close this thing.")
  print("6 - I'm done here. Quit Program.")
  print("")
  a=int(input("What would you like to do? "))
  print("")
  if 1==a:
    showMem()
  elif 2==a:
    print("Current files in storage are: ",storage)
    b=input("Which file would you like to load? ")
    if b=="file1" or b=="1":
      ram0=file1
      storage.pop(0)
      #for c in storage:
       # if c == file1:
        #  storage.pop(c)
    elif b=="file2" or b=="2":
      ram1=file2
      if storage[1] != None:
        storage.pop(1)
      else:
        storage.pop(0)
  elif 3==a:
    edit = int(input("Would you like to edit a row (1) or a single character (2)? "))
    if edit==1:
      currentRow=int(input("Which row would you like to edit? "))
      if(currentRow==0):
        currentRow=ram0
      elif(currentRow==1):
        currentRow=ram1
      elif(currentRow==2):
        currentRow=ram2
      elif(currentRow==2):
        currentRow=ram3
      elif(currentRow==4):
        currentRow=ram4
      elif(currentRow==5):
        currentRow=ram5
      elif(currentRow==6):
        currentRow=ram6
      elif(currentRow==7):
        currentRow=ram7
      print("The row currently shows: ",currentRow)
      change=input("Enter the new row: ")
      i=0
      for l in change:
        print(i)
        print(currentRow[i])
        print(change[i])
        currentRow[i]=change[i]
        i+=1
    elif edit==2:
      c = 0
      d = 0
      while c < 8 and d < 16:
        print("Please enter the grid you'd like to edit. Enter out-of-bounds coordinates to exit the editor.")
        currentRow = int(input("Row? "))
        d = int(input("Column? "))
        change=input("What would you like to change it to? ")
        if(currentRow==0):
          currentRow=ram0
        elif(currentRow==1):
          currentRow=ram1
        elif(currentRow==2):
          currentRow=ram2
        elif(currentRow==2):
          currentRow=ram3
        elif(currentRow==4):
          currentRow=ram4
        elif(currentRow==5):
          currentRow=ram5
        elif(currentRow==6):
          currentRow=ram6
        elif(currentRow==7):
          currentRow=ram7
          print(currentRow)
        if c < 8 and d < 16:
          currentRow[d] = change
  elif 4==a:
    currentRow=int(input("Which row would you like to delete? "))
    if currentRow < 8:
      if(currentRow==0):
        ram0= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==1):
        ram1= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==2):
        ram2= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==2):
        ram3= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==4):
        ram4= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==5):
        ram5= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==6):
        ram6= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==7):
        ram7= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        print(currentRow)
    else:
      print("Invalid row.")
  elif 5==a:
    currentRow=int(input("Which row contains the file you'd like to save & close? "))
    if currentRow < 8:
      if(currentRow==0):
        ram0= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==1):
        ram1= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==2):
        ram2= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==2):
        ram3= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==4):
        ram4= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==5):
        ram5= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==6):
        ram6= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
      elif(currentRow==7):
        ram7= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        print(currentRow)
    else:
      print("Invalid row.")
  elif 6==a:
    print("Aight this has been fun.  Peace.")
