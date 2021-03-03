import random as r
animals=["lion","tiger","lioness","tigeress","dog","buffalo","liger","squireel",
         "panda","elephant","jaguar","cheetah","rhinoceros","hippopotamus","gorrila"]
com=r.choice(animals)

print("You have 6 attempts. ")
guess=""
trial=6
for i in com:
    print("-",end="")
print()
while True:
    human=input("Enter letter of your choice : ")
    guess+=human
    if human in com:
        new=""
        for i in com:
            if i in guess:
                new+=i
            else:
                new+="-"
        print(new)
        if new==com:
            print("Congratualtions! You Won")
            break
    else:
        trial-=1
        if trial==0:
            print("You lost")
            break
        print("Wrong Choice")
        print(trial," attempts left")
        

        
        
        
