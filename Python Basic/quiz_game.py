def new_game() :
    guesses=[]
    correct_guesses=0
    question_num=1
    for key,value in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        answer= None
        if answer !="A" or answer!="B":
            answer= input("What is your answer?A or B").upper()
        guesses.append(answer)
        question_num+=1

#----------------------
def check_answer():
    pass
#----------------------
def display_score():
    pass
#----------------------
def play_again():
    pass

questions ={
    "Who loves you the most?":"A",
    "What created FaceBook?":"B"
}

options=[["A.Mom","B.Dad"],
        ["A.Elon Musk","B.Mark Zuckerberg"]]

new_game()