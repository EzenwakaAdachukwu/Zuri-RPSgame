
import random
comp_tied = 0
comp_lose = 0
comp_wins = 0
player_wins = 0
player_tied = 0
player_lose = 0


def Choose_Option() :
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"] :
        player_choice = "R"

    elif player_choice in ["Paper", "paper", "p", "P"] :
        player_choice = "P"
        
    elif player_choice in ["Scissors", "scissors", "s", "S"] :
        player_choice = "S"   
    else:
        print("Error, try again.") 
        Choose_Option ()
    return player_choice  

def Computer_Options() :
    comp_choice = random.randint (1,3)
    if comp_choice ==1:
        comp_choice = "R"
    elif comp_choice ==2:
        comp_choice = "P"
    else: 
        comp_choice == "S"
    return comp_choice 
while True:
    print("") 
    player_choice = Choose_Option()
    comp_choice = Computer_Options()
    print("")

    if player_choice == "R":
        if comp_choice == "R":
            print ("Player(Rock) : CPU(Rock) You tied, Game repeat.")
            print("") 
            player_choice = Choose_Option()
            comp_choice = Computer_Options()
            print("")

        elif comp_choice == "P":
            print("Player(Rock) : CPU(Paper) You lose and CPU wins, Game ends.")
            comp_wins += 1 
            
            
        elif comp_choice == "S":
            print("Player(Rock) : CPU(Scissor) You win and CPU lose, Game ends.") 
            player_wins += 1 


    elif player_choice == "P": 
        if comp_choice == "R":
           print("Player(Paper) : CPU(Rock) You win and CPU lose, Game ends.")  
           player_wins += 1 

        elif comp_choice == "P" :
           print("Player(Paper) : CPU(Papper) You tied, Game repeat.")
           print("") 
           player_choice = Choose_Option()
           comp_choice = Computer_Options()
           print("")

        elif comp_choice == "S" :
             print("Player(Paper) : CPU(Scissor) You lose and CPU wins, Game ends.") 
             comp_wins += 1
             

    elif player_choice == "S" :
        if comp_choice == "R":
             print("Player(Scissor) : CPU(Rock) You lose and CPU wins, Game ends.")  
             comp_wins += 1 
            

        elif comp_choice == "P" :
             print("Player(Scissor) : CPU(Paper) You win and CPU lose, Game ends.") 
             player_wins += 1  
            #  player_tied += 0 

        elif comp_choice == "S" :
             print("Player(Scissor) : CPU(Scissor) You tied, Game repeat.") 
             print("") 
             player_choice = Choose_Option()
             comp_choice = Computer_Options()
             print("")
             
    if player_tied and comp_tied:
           print("Game repeat") 
    else:
        break       
    # elif player_lose and comp_wins:
        #    print("Game ends")
    # elif player_wins or comp_lose:    
        # print("Game ends")
    # else:
        # break  
    

             
