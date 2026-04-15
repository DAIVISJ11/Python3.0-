import random

attempts_list = []

def show_score():
    if len(attempts_list)  <= 0:
        print("Let's set a highscore")
    else:
        print("Your current highscore us {} attemprs".format(min(attempts_list)))

def start_game() :
    random_number = random.randint(1,10)
    print("Welcome to the Guessing Game ")

    player_name = input("Enter your name :")
    wanna_play = input(f"hi, {player_name}, would you like to play (yes/no)")

    attempts = 0
    show_score()

    while wanna_play.lower()== "yes":
        try:
            guess = int(input(" pick a number between 1 and 10: "))
            if guess < 1 or guess>10:
                raise ValueError("Please give the number betwee the given range")
            if guess == random_number:
                print(" Congratulation you just set a high score")
                attempts +=1
                attempts_list.append(attempts)

                print("It took you {} attempts" .format(attempts))
                play_again = input("Do you want to play again")
                attempts = 0
                show_score()

                random_number = random.randint(1, 10)


                if play_again.lower() == "no":
                    print("That's Cool have a nice day")
                    break
            elif guess < random_number:
                print("Thats higher")
                attempts += 1

            else:
                print( "It is lower")
                attempts += 1

        except ValueError as err:
            print("That is a invalid answer")
            print(f"({err})")

    else:
        print("that is okay")
if __name__=='__main__':
    start_game()




