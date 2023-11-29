def main():
    number = RandomNumber()
    guess = input("Enter a number")
    print(CheckUserGuess(number, guess))


def RandomRandom():
    return None

def CheckUserChoice(number, guess):
    if guess = number:
        return true
    elif -1 <= number-guess <= 1:
        return "Very close"
    elif -2 <= number-guess <= 2:
        return "Close"
    else:
        return "Wrong"
    

main()