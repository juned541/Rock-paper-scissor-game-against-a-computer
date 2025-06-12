import random


options = ["Rock","Paper", "Scissor" ]
play = "No"

def main():
    compare()


def compare(): 
    computer_choice = computer_choices()
    user_chioce = user_choices()
    # print(f"You have selected {user_chioce} ")
    # print(f"computer choose {computer_choice}")
    
    if computer_choice == user_chioce :
        print(f"Computer chose {computer_choice}")
        print(f"You chose {user_chioce}")
        print("It is a draw")
        print()
        play = input("Do you want to play again? (Yes/No): ").strip().title()
        if play == "No":
            print("Thanks for playing!")
            return
        else:
            return compare()    

    else: 
        if computer_choices == "Rock":
            if user_chioce =="Paper":
                print(f"Computer chose {computer_choice}")
                print(f"You chose {user_chioce}")

                print("Computer won!, You lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()                    


            elif user_chioce == "Scissor":
                print(f"Computer chose {computer_choice}")
                print(f"You chose {user_chioce}")
                print("Computer won!, You lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()    

            
        elif computer_choice == "Paper":
            if user_chioce == "Scissor":
                print(f"computer chose {computer_choice}")
                print(f"You chose {user_chioce}")
                print("You win!, computer lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()    

            elif user_chioce == "Rock":
                print(f"Computer chose {computer_choice}")
                print(f"You chose {user_chioce}")
                print("You win!, computer lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()    

            
        elif computer_choice == "Scissor":
            if user_chioce == "Rock":
                print(f"Computer chose {computer_choice}")
                print(f"You chose {user_chioce}")
                print("You win!, computer lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()    


            elif user_chioce == "Paper":
                print(f"Computer chose {computer_choice}")
                print(f"You chose {user_chioce}")
                print("Computer won!, You lose!")
                print()
                play = input("Do you want to play again? (Yes/No): ").strip().title()
                if play == "No":
                    print("Thanks for playing!")
                    return
                else:
                    return compare()    



def user_choices():
    user_choice = input(
        "Select your option from the list\n" 
        "Rock\n"
        "Paper\n"
        "Scissor\n"
        ": " 
    ).strip().title()
    return user_choice


def computer_choices():
    computer_selected = random.choice(options)
    return computer_selected





if __name__ == "__main__":
    main()