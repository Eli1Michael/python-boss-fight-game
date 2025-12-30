#Stamina is gonna change
#Health is gonna change
#Number of portions are gonna change
#strength of blow is  gonna change based on Stamina
#Supper attacking moves only appear when the Super meter builds up
#Super attacking moves are a sure hit and will give you the oportunity to use heals. 
#Loop over the exchange of blows
#loop is gonna have three results where they exchange one where two hit each other and another where none do
#To achieve those results i'll have to make two roads hit and no hit
#Outside the loop include what happens when game is over
import random
Stamina=100
Boss_Attack=0
Player_Attack=0
Boss_Health=350
Player_Health=250
Super_Meter=0
Heals=5
block=0

#the main loop
while Boss_Health>0 and Player_Health>0 and Stamina>0:
 
    #super meter
    Super_Meter = min(Super_Meter, 100)

    #Player status
    print(f"Your health:{Player_Health} | Boss_Health:{Boss_Health}")
    print(f"Stamina:{Stamina} ")
    print(f"SuperMeter:{Super_Meter}")
    print(f"{Heals} portions left")

    # strength of Block
    if Stamina >= 70:
      block = 60
    elif Stamina >= 40:
      block = 40
    else:
      block = 20

    #Strength of attack
    Player_Attack = random.choice([0, 50, 100])
    Boss_Attack   = random.choice([0, 50, 100])
   
    #What to print if supermeter is available
    print("Choose one before the boss hits you")
    if Super_Meter==100:
      print("Do you wanna hit the supermove, attack or block the boss")
    else:
      print("Do you wanna  attack or block the boss")
 
    #Player choosing attack
    aCtion=input("What move do you wanna hit?").lower()
  
    #Player choosing super move
    if "super" in aCtion and Super_Meter == 100:
       Boss_Health -= 100
       Super_Meter = 0
  

    # What to do after super move
       if Heals > 0:
         choice = input("Boss is staggered! Heal? ").lower()

         if "yes" in choice:
              Heals -= 1
              Player_Health += 150
              Player_Health = min(Player_Health, 250)
         print(f"You have healed up to {Player_Health} hp")
 
    #What to do after attack
    elif "attack" in aCtion: 
       Boss_Health -= Player_Attack
       Super_Meter += 20
       Stamina -= random.randint(1,20)
       Player_Health -= Boss_Attack
       # now explain to the player
       print(f"You dealt {Player_Attack} damage")
       print(f"The boss dealt {Boss_Attack} damage")
       if Player_Attack == 100:
         print("CRITICAL — you rocked him!")
         Super_Meter += 30
       elif Player_Attack == 0:
         print("You completely whiffed. Air punch 😭")
         Super_Meter -= 20
   
    #What to do after block
    elif "block" in aCtion:
       Damage=max(Boss_Attack-block,0)
       Player_Health -= Damage
       Super_Meter += 25
       Stamina -= random.randint(1,10)

    #What to do if not known
    else:
      print("What did you say?")
      continue

#what to do when the game ends
if Boss_Health<=0 and Player_Health<=0:
  print("You have both died")   
elif Boss_Health<=0 :
  print("Victory")  
else:
  print("You died") 