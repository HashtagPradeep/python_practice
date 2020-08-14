print("Welcome to my Smarty gamer")
name = input("what is your name? ")
age = int(input("what is your age? "))

print("Hello", name, "you are", age,"years old huhh!! ")

health = 10

if age >= 18:    
    print("You are allowed to play the game!!")
    
    print("You are starting with", health, "health")

    wanna_play = input("Do you want to play smarty? ").lower()
    if wanna_play == "yes":
        print("Great, Let's play!")

        left_or_right = input("There are two roads, choose one for your journey.. (left/right)? ")

        if left_or_right == "left":
            answer = input("Nice, you choose a path to the lake... Do you want to swim or go around (across/around)? ")

            if answer == "around":
                print("You went around and reached the other side of the lake..")

            elif answer == "across":
                print("You choose to swim across and you got bit by a aligator and managed to save your ass but lost 5 health. ")
                health -= 5

                ans = input("you notice a house and a river, which do you got to(river/house)? ")
                if ans == "house":
                    print("you go to the house and find out the house is haunted and you lose 5 points")
                    health -=5
                
                if health<= 0:
                    print("you now have 0 health and you lose the game...")
                else:
                    print("you won!!!")
            
            else:
                print("You fell in the river and been eaten by an aligator..")
        else:
            print("You lost!!..")

    else:
        print("cya...!")

elif age >= 14:
    print("You can play under supervision!")

    Elders_Around = input("Do you have anyone who can supervise?  ")
    if Elders_Around == "yes":
        print("Wola, You are good to go!")
    
    else:
        print("Oops sorry you can't continue!!")

else:
    print("Oops you are under aged!!")   
