import random as r
Choice=["STONE","PAPER","SCISSOR"]
class S:
    player_score=0
    bot_score=0
obj=S()
def game():
    print("----------------RESULT-------------")
    print("Your choice       : ",player.upper())
    print("Computer's choice : ",bot)
    if bot==player.upper():
        print("GAME DRAW")
    elif bot.upper()=="STONE" and player.upper()=="PAPER": #STONE - PAPER => PAPER
        print("YOU WON")
        obj.player_score=obj.player_score+1
    elif bot.upper()=="STONE" and player.upper()=="SCISSOR": 
        print("BOT WON")
        obj.bot_score=obj.bot_score+1
    elif bot.upper()=="PAPER" and player.upper()=="STONE":
        print("BOT WON")
        obj.bot_score=obj.bot_score+1
    elif bot.upper()=="PAPER" and player.upper()=="SCISSOR":
        print("YOU WON")
        obj.player_score=obj.player_score+1
    elif bot.upper()=="SCISSOR" and player.upper()=="PAPER":
        print("BOT WON")
        obj.bot_score=obj.bot_score+1
    elif bot.upper()=="SCISSOR" and player.upper()=="STONE":
        print("YOU WON")
        obj.player_score=obj.player_score+1
    print("----------------SCORE-------------")
    print("Your Score          :",obj.player_score)
    print("Computer's Score    :",obj.bot_score)
    print("-----------GAME COMPLTED-----------")
    print()
while True:
    bot=r.choice(Choice)
    while True:
        player=input("Enter your choice (STONE / PAPER /SCISSOR): ")
        if player.upper() in Choice:
            break
    game()
    y=input("Press Y for Continue..... ")
    if y.upper()!="Y":
        print()
        break
print("-------------OVERALL SCORE-------------")
print("Your Score          :",obj.player_score)
print("Computer's Score    :",obj.bot_score)