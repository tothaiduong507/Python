import sys
def new_game() :
    question_num = 1
    correct_guess = 0
    for key,value in questions.items():
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        answer= input("What is your answer?A or B").upper()
        correct_guess+=check_answer(value,answer)
        question_num += 1
    display_score(correct_guess)
    play_again()

#----------------------
def check_answer(answer,guess):
    if (answer == guess):
        return 1
    else:
        return 0
#----------------------
def display_score(correct_guess):
   print("Your score is "+ str(correct_guess))
#----------------------
def play_again():
    print("Do you want to play a again? YES/ NO")
    ans= input().upper()
    if ans=='YES':
        new_game()
    else :
        sys.exit()

questions ={
    "Who loves you the most?":"A",
    "What created FaceBook?":"B"
}

options=[["A.Mom","B.Dad"],
        ["A.Elon Musk","B.Mark Zuckerberg"]]

new_game()