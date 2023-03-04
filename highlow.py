low = 1
high = 10000

print("Please think of a number between {} and {}".format(low, high))
input("Please press the ENTER key to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h (higher) or l (lower), or c if my guess is correct: "
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")

    guesses +=1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))