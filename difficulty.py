from random import randint
from time import sleep
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def easy():
    game(5, 10, 1)

def medium():
    game(3, 25, 2)

def hard():
    game(2, 50, 4)


def game(sleeptime, maxval, n):
    
    str1=[]
    
    for i in range(0,20):
        print("Welcome to level ", i+1)
        new=randint(1,maxval-1)
        str1.append(new)
        print("memorise the values you have ", sleeptime," seconds", str1)
        sleep(sleeptime)
        cls()
        str2=[]
        print("Enter the values in the exact same order")
        for j in range(0,i+1):
            temp=int(input("Value "))
            str2.append(temp)    
        print("System String: ",str1, "Your input ", str2)
        if(str1==str2):
            print("Correct. Proceed to next level")
            print("Score =", n*(i+1))
            cls()
    
        else:
            print("You lose. Final Score =", n*(i))
            break
