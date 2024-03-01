from random import choice
import os
import time
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def control_card(user_cards,computer_cards):
    other_card=input("Type \'y\' for other card , or \'n\' to stop  ").lower()
    if other_card== "n" :
            computer_sum=sum(computer_cards)
            user_sum=sum(user_cards)
            while computer_sum < 17 :
                computer_cards.append(choice(cards))
                computer_sum=sum(computer_cards)
            print(f"user={user_sum}, computer={computer_sum} ")
            if computer_sum > 21 :
                print(f"Computer has {computer_cards} over 21 , you win ")
            elif computer_sum> user_sum :
                print("You lose ")
            elif computer_sum== user_sum :
                print("Egalisation , it \' s a draw ")
            else :
                print(f"{user_cards} You win ")
            end_choice=True
            
            
            
    else :
            user_cards.append(choice(cards))
            user_sum=sum(user_cards)
            end_choice=False
    return end_choice


def play_game():

    user_cards, computer_cards=[],[]
    for card in range (2):
        user_cards.append(choice(cards))
        computer_cards.append(choice(cards))
    end_choice=False
    user_sum=0
    while not end_choice :
        user_sum=sum(user_cards)
        computer_sum=sum(computer_cards)
        print(f"user={user_cards}, computer_first card  {computer_cards[0]} ")
        if user_sum==21 :
            print(f"You have a black Jack {user_cards} , you win")
            end_choice=True
        elif computer_sum== 21:
            print(f"Computer has a Black Jack {computer_cards}  , you lose ")
            end_choice=True
            
        elif user_sum > 21 :
            if 11 in user_cards :
                
                for i in range (len(user_cards)):
                    if user_cards[i]==11:
                        user_cards[i]=1
                        
                        
                user_sum=sum(user_cards)
                
                if user_sum > 21 : 
                    print(f"Over 21 , you have {user_cards} You lose ")
                    end_choice=True
                else: 
                    end_choice=control_card(user_cards,computer_cards)
            else :
                print(f"Over 21 , you have {user_cards} , you lose ")
                end_choice=True

        else :
            end_choice=control_card(user_cards,computer_cards)
    
while input("\n\nDo you what to play  game ? Guess \'y\' or \'n\' ").lower()=="y":
     time.sleep(0.0001)
     os.system("cls")
     play_game()