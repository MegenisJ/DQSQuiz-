from Question import Question
from Quiz import Quiz
import csv
##This is the main running of the program, Will be basic calls to other methods and UI mainly

def WriteQuestions(QuestionList):
    with open("Questions.csv",'w',newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for  x in QuestionList:
            a1 = x.Answers["A"]
            a2 = x.Answers["B"]
            a3 = x.Answers["C"]
            a4 = x.Answers["D"]
           # data = x.QuestionAsked,a1,a2,a3,a4,x.CorrectAnswer,x.Explanation,x.Topics
            writer.writerow(x.QuestionAsked,a1,a2,a3,a4,x.CorrectAnswer,x.Explanation,x.Topics)
            
def ReadQuestions():
    QList = []
    with open("Questions.csv") as csvfile:
     
        #r = csv.reader(csvfile)
        r = csv.reader(csvfile)
        for row in r:
            print(row) #QuestionList 
            #Q = row[0]
            #print(row)
            A = {}
            #print(row[0])
            A.update({"A":row[1]})
            A.update({"B":row[2]})
            A.update({"C":row[3]})
            A.update({"D":row[4]})


            QList.append(Question(row[0],A,row[5],row[6],row[7]))
    return(QList)

def MainMenu(): 
    QuestionList = []
    EndProgram = False
    while EndProgram ==False:
        #QuestionList = []
        print("Menu: ")
        print("1 new question")
        print("2 Run Quiz")
        print("3 Exit program")
    #print("3 new question")
        Menu = input()
        QuestionList = ReadQuestions()
        if Menu == "1":
            QuestionList = ReadQuestions()
            ChangeQuestions(QuestionList)
            #WriteQuestions(QuestionList)
        elif Menu =="2":
           # QuestionList = ReadQuestions()
            UserQuiz = Quiz(['work'],QuestionList) ##Create the topic list
            #UserQuiz.SetupQuiz()
           # print(QuestionList[0])
            UserQuiz.TakeQuiz(QuestionList)
        elif Menu =="3":
            EndProgram = True
      #  print(UserQuiz.AllQuestions)
   # elif Menu ==3:






    #load all questions into the program from csv file
    # Options (More can be added)
    #1 Log in as admin to change stuff
    #2 GenerateQuiz (call Quiz.Quiz.SetupQuiz())
    #3 Run With all Q's in random order (call Quiz.Quiz.SetupQuiz())

def ChangeQuestions(QuestionList): #Alice

    print("1 to add new question")
    QuestionOption = input("Answer: ")
    #print(QuestionOption)
    #d = {}
    if QuestionOption == "1":
        d = {"A":"","B":"","C":"","D":""}

        q = input("Enter the question: ")
      
        A= input("Enter answer A: ")
        d.update({'A': A })
        
        B= input("Enter answer B: ")
        d["B"] = B
        
        C =input("Enter answer C: ")
        d["C"] = C
        
        D= input("Enter answer D: ")
        d["D"] = D

        CorrectAnswer = input("Enter the correct answer (A,B,C,D)")
        ex = input("Enter an explination for your answer: ")
        t = input("Enter list of topics seperated by SPACE").split()
        #x = Question()
        QuestionList.append(Question(q,d,CorrectAnswer,ex,t))

        with open("Questions.csv",'w',newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([q,d["A"],d["B"],d["C"],d["D"],CorrectAnswer,ex,t])

    else:

        print("Invalid input")
MainMenu()#

