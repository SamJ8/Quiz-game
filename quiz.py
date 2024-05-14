import time
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
import random

print(Fore.YELLOW + """



███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗     ███████╗     ██████╗██╗  ██╗ ██████╗ ██╗ ██████╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║     ██╔════╝    ██╔════╝██║  ██║██╔═══██╗██║██╔════╝██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║     █████╗      ██║     ███████║██║   ██║██║██║     █████╗      ██║   ██║██║   ██║██║  ███╔╝ 
██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║     ██╔══╝      ██║     ██╔══██║██║   ██║██║██║     ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗███████╗    ╚██████╗██║  ██║╚██████╔╝██║╚██████╗███████╗    ╚██████╔╝╚██████╔╝██║███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
""") ## added some ASCII art for some creativity

print(Fore.LIGHTBLACK_EX + "===================================== All things python =====================================\n".upper())
print("For every question answered correctly, you will score 5 points! For every question answered incorrectly you will lose 2 points!")



questions = ["How is a close block indicated in Python?",
             "Which of the following types of loops are not supported in Python?",
             "Python is known as:?",
             "Which of the following is a valid Python comment?",
             "Python is a:",
             "Which of these data types does Python not natively support?",
             "Which of the following is a mutable data type in Python?",
             "What data type would you use to store a whole number in Python?",
             "Which function is used to read input from the console?",
             "Which function in Python is used to display data as output" ## All the questions I have set in a list to be asked, I got my questions and answers from Google.
             ]

choices = [["A. Brackets", "B. Indentation", "C. Key", "D. None of the above"],
           ["A. for", "B. while", "C. do-while", "D. None of the above"],
           ["A. A compiled language", "B. An interpreted language", "C. A machine language", "D. An assembly language"],
           ["A. <!----->", "B. /**/", "C. #", "D. //"],
           ["A. High-level language", "B. Middle level language", "C. Low-level language", "D. Machine-level language"],
           ["A. Lists", "B. Tuples", "C. Dictionaries", "D. Arrays"],
           ["A. List", "B. Tuple", "C. String", "D. Integer"],
           ["A. float", "B. int", "C. str", "D. bool"],
           ["A. read()", "B. scan()", "C. input()", "D. getInput()"],
           ["A. display()", "B. show()", "C. output()", "D. print()"]] ## set my choices to choose from in a list of lists

answers = ("B", "C", "B", "C", "A", "D", "A", "B", "C", "D") ## these are all the answers to the questions


replay_again = "Y" ## replay variable set to Y
score = 0 ## Score variable set to 0
question_ = 0 ## question number starting from 0

while replay_again == "Y": ## while loop used so that when user hits 'Y', the program restarts
    print(input("\nAre you ready? The timer will count down from 5 when you are. Press enter to start! ")) ## user to hit enter so that the timer counts down
    score = 0 ## score will have to be set back to 0
    for seconds in range(5, 0 , -1):
        print(seconds)
        time.sleep(1) ## For more creativity, I used import time so a countdown will start once user hits enter

    random_order = list(range(len(questions))) ## I used ChatGPT to implement a random question that correlates with the correct answer.
    random.shuffle(random_order) ## this will be randomising the order of the list we set in questions


    for question_ in random_order: ## ChatGPT also changed my while loop that I originally had here to loop through my questions, to a for loop to loop through the questions in a randomised order.
        print("__________________________________________________\n")
        print(Fore.BLUE + questions[question_]) ## displays current question
        for choice in choices[question_]: ## displays current option for the current question
            print(choice) 

        while True: ## while loop to be used so that it will ask user to enter answer for every question
            guess = input("\nEnter A, B, C or D: ").upper() ## used the .upper() method so it will convert the answer from user to uppercase so it is accepted
            if guess in ["A", "B", "C", "D"]: ## A, B, C or D are the only acceptable answers
                break
            else:
                print("Invalid input. Please enter A, B, C, D") ## will print if input is not A, B, C or D

        if guess == answers[question_]: ## this will check the answer against the question
            score += 5 ## for every question answered 5 points will be awarded
            print(Fore.LIGHTGREEN_EX + "\nCorrect! 5 points!") 
        else:
            score -= 2 ## for every wrong question answered 2 points will be deducted
            print(Fore.RED + "\nIncorrect! Minus 2 points!")
        question_ += 1 ## question number will increment by 1

    print("__________________________________________________")
    print(Fore.RED + f"\n\nYOUR FINAL SCORE: {score}/50.")
    if score == 50: ## if statement will be used so if user hits maximum score then print statement will display and program will end, if not the it will ask user if they want to play again
        print("\nWOW! Congratulations, you're a Python genius!")
        break

    play_again = input(Fore.GREEN + "\n\nWould you like to play again? Y/N? ").capitalize() ## The play_again variable will be called if user input is 'Y' which will restart the while loop
    if play_again != "Y": ## if satement used so that if the player hits anything other than 'Y' then program ends and print message below will display
        break
    print(Fore.RESET)
    question_ = 0 ## question variable set back to 0

print(Fore.MAGENTA + "\nThanks for playing!") ## print statement shown if player doesn't want to play or if they achieve the maximum score
    

#! -------------------------- ORIGINAL CODE BEFORE CHATGPT ------------------------------------------

# import time
# from colorama import Fore, Back, Style
# from colorama import init
# init(autoreset=True)
# import random

# print(Fore.YELLOW + """



# ███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗     ███████╗     ██████╗██╗  ██╗ ██████╗ ██╗ ██████╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
# ████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║     ██╔════╝    ██╔════╝██║  ██║██╔═══██╗██║██╔════╝██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
# ██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║     █████╗      ██║     ███████║██║   ██║██║██║     █████╗      ██║   ██║██║   ██║██║  ███╔╝ 
# ██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║     ██╔══╝      ██║     ██╔══██║██║   ██║██║██║     ██╔══╝      ██║▄▄ ██║██║   ██║██║ ███╔╝  
# ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗███████╗    ╚██████╗██║  ██║╚██████╔╝██║╚██████╗███████╗    ╚██████╔╝╚██████╔╝██║███████╗
# ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
# """) ## added some ASCII art for some creativity

# print(Fore.LIGHTBLACK_EX + "===================================== All things python =====================================\n".upper())
# print("For every question answered correctly, you will score 5 points! For every question answered incorrectly you will lose 2 points!")



# questions = ["How is a close block indicated in Python?",
#              "Which of the following types of loops are not supported in Python?",
#              "Python is known as:?",
#              "Which of the following is a valid Python comment?",
#              "Python is a:",
#              "Which of these data types does Python not natively support?",
#              "Which of the following is a mutable data type in Python?",
#              "What data type would you use to store a whole number in Python?",
#              "Which function is used to read input from the console?",
#              "Which function in Python is used to display data as output" ## All the questions I have set in a list to be asked
#              ]

# choices = [["A. Brackets", "B. Indentation", "C. Key", "D. None of the above"],
#            ["A. for", "B. while", "C. do-while", "D. None of the above"],
#            ["A. A compiled language", "B. An interpreted language", "C. A machine language", "D. An assembly language"],
#            ["A. <!----->", "B. /**/", "C. #", "D. //"],
#            ["A. High-level language", "B. Middle level language", "C. Low-level language", "D. Machine-level language"],
#            ["A. Lists", "B. Tuples", "C. Dictionaries", "D. Arrays"],
#            ["A. List", "B. Tuple", "C. String", "D. Integer"],
#            ["A. float", "B. int", "C. str", "D. bool"],
#            ["A. read()", "B. scan()", "C. input()", "D. getInput()"],
#            ["A. display()", "B. show()", "C. output()", "D. print()"]] ## set my choices to choose from in a list of lists

# answers = ("B", "C", "B", "C", "A", "D", "A", "B", "C", "D") ## these are all the answers to the questions


# replay_again = "Y" ## replay variable set to Y
# score = 0 ## Score variable set to 0
# question_ = 0 ## question number starting from 0

# while replay_again == "Y": ## while loop used so that when user hits 'Y', the program restarts
#     print(input("\nAre you ready? The timer will count down from 5 when you are. Press enter to start! "))
#     score = 0 ## score will have to be set back to 0
#     for seconds in range(5, 0 , -1):
#         print(seconds)
#         time.sleep(1) ## For more creativity, I used import time so a countdown will start once user hits enter

#     while question_ < len(answers): ## while loop to run through every question, incrementing every time using the question_number variable
#         print("__________________________________________________\n")
#         print(Fore.BLUE + questions[question_]) ## displays current question
#         for choice in choices[question_]: ## displays current option for the current question
#             print(choice) 

#         while True: ## while loop to be used so that it will repeatedly ask user to enter answer for every question
#             guess = input("\nEnter A, B, C or D: ").upper()
#             if guess in ["A", "B", "C", "D"]: ## A, B, C or D are the only allowed answers
#                 break
#             else:
#                 print("Invalid input. Please enter A, B, C, D") ## will print if input is not A, B, C or D

#         if guess == answers[question_]: ## this will check the answer against the question number
#             score += 5 ## for every question answered 5 points will be awarded
#             print(Fore.LIGHTGREEN_EX + "\nCorrect! 5 points!") 
#         else:
#             score -= 2 ## for every wrong question answered 2 points will be deducted
#             print("\nIncorrect! Minus 2 points!")
#         question_ += 1 ## question number will increment by 1

#     print("__________________________________________________")
#     print(Fore.RED + f"\n\nYOUR FINAL SCORE: {score}/50.")
#     if score == 50: ## if statement will be used so if user hits maximum score then print statement will display and program will end
#         print("\nWOW! Congratulations, you're a Python genius!")
#         break

#     play_again = input(Fore.GREEN + "\n\nWould you like to play again? Y/N? ").capitalize() ## variable will be used again so they can replay if they hit yes
#     if play_again != "Y":
#         break
#     print(Fore.RESET)
#     question_ = 0 ## question variable set back to 0

# print(Fore.MAGENTA + "\nThanks for playing!")           

# FIRST VERSION ^^^^^