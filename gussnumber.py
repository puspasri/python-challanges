import random
number = random.randint(1,100)

def intro ():
    pass
    name = input("What is your name ?")
    print(name,"We will guess the number till 1 to 100.")
    if number%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")

    print("guess a number")


def pick():
     guesstaken = 0


     while guesstaken<6:
         enter = input("Enter the gussed number.")

        try:
             guess=int(enter)

            if guess<=100 and guess>=1:
             gussestaken=gussestaken+1
                if guess>number:
                    print("too high")
                if guess<number:
                  print("too low")

        except:
               print("Enter a number :")

          

             




play="yes"

while play=="yes":
    intro()
    print("Do you want to play again ")
    play=input()


