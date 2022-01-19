def main():
    print()
    print("This program is an implementation of the Rosenberg\
        \nSelf-Esteem Scale. This program will show you ten\
        \nstatements that you could possibly apply to yourself.\
        \nPlease rate how much you agree with each of the\
        \nstatements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.\
        \nd means you disagree with the statement.\
        \na means you agree with the statement.\
        \nA means you strongly agree with the statement.")

    scale = scaleCalc()

    if scale <= 15:
        print(f"Your current esteem scale is {scale}")
        print("You may have a problematic low self-esteem.")
    else:
        print(f"Your current esteem scale is {scale}")

def scaleCalc():
    answer1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.")
    answer2 = input("2. I feel that I have a number of good qualities.")
    answer3 = input("3. All in all, I am inclined to feel that I am a failure.")
    answer4 = input("4. I am able to do things as well as most other people.")
    answer5 = input("5. I feel I do not have much to be proud of.")
    answer6 = input("6. I take a positive attitude toward myself..")
    answer7 = input("7. On the whole, I am satisfied with myself.")
    answer8 = input("8. I wish I could have more respect for myself.")
    answer9 = input("9. I certainly feel useless at times.")
    answer10 = input("10. At times I think I am no good at all.")
    
    scale = convertAnswer(answer1) + convertAnswer(answer2) + convertAnswer(answer3) + convertAnswer(answer4) + convertAnswer(answer5) + convertAnswer(answer6) + convertAnswer(answer7) + convertAnswer(answer8) + convertAnswer(answer9) + convertAnswer(answer10)

    return scale

def convertAnswer(answer):
    if answer == 'A':
        return 3
    elif answer == 'a':
        return 2
    elif answer == 'd':
        return 1
    elif answer == 'D':
        return 0

main()