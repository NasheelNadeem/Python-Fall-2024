from random import randrange


def check_guess(guess,answer):
    difference= guess - answer

    if guess == answer:
        print("you guessed the answer")
        return 0
    elif guess > answer:
        print(f"your guess is {difference} away from the answer")
        return difference
    else:
        difference = answer - guess
        print(f"your guess was {difference} away from the number")
        return difference
def main():
    answer= randrange(1,10)
    guess= int(input("Pick a number betwenn 1-10"))
    result= check_guess(guess,answer)
    return result

if __name__ == "__main__":
    main()