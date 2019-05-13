from difficulty import *
from os import system, name
print("Welcome")
print("Enter your name and choose your difficulty. You will be shown a string of integers to memorise. After a few seconds you will be asked to enter the string integer by integer. If you do so correctly your points will increase and you will proceed to next level. If you enter the incorrect string, you will lose and the game will end. Good Luck!")
cont=1
while(cont==1):

    player=input("Enter Your name ")

    print("Hello ", player, " choose your difficulty ")
    dif=int(input("1. Easy 2. Intermediate 3. Hard "))
    if(dif==1):
        easy()
    elif(dif==2):
        medium()    
    elif(dif==3): 
        hard()
    
    else: 
        print("Invalid")
    
    res=input(("Do you wish to play again?(Y/N)"))
    if(res=='Y' or res=='y'):
        cont=1

    else:
        cont=0




