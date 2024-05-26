import json
import time
import msvcrt
import sys
import os

def load_questions():  #Loads questions
    with open('questions.json', 'r', encoding='utf-8') as file:
        questions_data = json.load(file)
    return questions_data

def show_question(question_index, question):  #Shows questions for the test
    print(f"Question {question_index + 1}: {question['question']}")
    for i, option in enumerate(question['options'], start=1):
        print(f"{chr(64 + i)}. {option}")
        

def timer(start_time): #Timer inside the test. Reloads after user input
    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = 20 * 60 - elapsed_time
    if remaining_time <= 0:
        print("Time's up!")
        finish_test()
    else:
        os.system('cls')
        print(f"Time left: {int(remaining_time) // 60} minutes {int(remaining_time) % 60} seconds")

def user_input(question_index):  #User input 
    user_answer = msvcrt.getwch().upper()
    if user_answer not in ['A', 'B', 'C', 'D']:
        print("Please, press press one of these keys: 'A', 'B', 'C' or 'D' ")
        user_input(question_index)
    else:
        user_answers[question_index] = user_answer

def finish_test():  #Finishing test when all the answers recieved, shows how many answers are correct and asks to try again. 
    correct_answers = 0
    for i, question in enumerate(questions):
        if user_answers[i] == question['correctAnswer']:
            correct_answers += 1
    if correct_answers >= 15:
        print("Congratulations! You've passed the test.")
    else:
        print("Unfortunately you haven't reached the minimum of correct answers to pass the test.")
    print(f"Amount of correct answers: {correct_answers}/20")
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
    print(f"Time spend on the test: {minutes:02d} minutes, {seconds:02d} seconds")
    print("Would you like to try again? (Y/N)")
    while True:
        choice = msvcrt.getwch().upper()
        if choice == 'Y': #Restart test
            test()
        elif choice == 'N': #Kill programm
            print("Bye!")
            sys.exit()   
        else:
            print("You've pressed a wrong key.")
            continue

def test():
    global questions, user_answers, start_time
    reset_answers()  # Reset of all the user answers before test start
    questions = load_questions()
    start_time = time.time()
    for i, question in enumerate(questions):
        show_question(i, question)
        user_input(i)
        timer(start_time)
    finish_test()

def reset_answers():
    global user_answers
    user_answers = [''] * len(questions)

questions = load_questions()
user_answers = [''] * len(questions)
start_time = 0

print("Welcome to the test about Hollywood stars!")
print("To start the quest - press 'Y': ")
ready = msvcrt.getwch().upper()
if ready == "Y":
    test()
else:
    print("You've pressed a wrong key.")
    sys.exit()