import random


def game():

    answer = random.randint(1, 20)
    print("i am thinking of num")

    numbness = 3
    while numbness > 0:
        print(f"u have {numbness}guesses")
        guess = int(input('make a guess'))
        numbness -= 1

        if guess==answer:
            print("that's it")
            return
        elif numbness == 0:
            break

        elif answer>guess:
            print("guess higher")
        else:
            print("guess lower")

    print("the number was{}".format(answer))
    return


game()










