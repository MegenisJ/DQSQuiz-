from Question import Question
from Quiz import Quiz
import csv
def WriteQuestions(QuestionList): ##Can be removed 
    with open("Questions.csv",'w',newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for  x in QuestionList:
            a1 = x.Answers["A"]
            a2 = x.Answers["B"]
            a3 = x.Answers["C"]
            a4 = x.Answers["D"]
       
            writer.writerow(x.QuestionAsked,a1,a2,a3,a4,x.CorrectAnswer,x.Explanation,x.Topics)
                                    ##whole function


def ReadQuestions(QuestionList):
    QList = []
    with open("Questions.csv",newline = '') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
          #  print(row) #QuestionList 
            A = {"A":"","B":"","C":"","D":""}
            A.update({"A":row[1]})
            A.update({"B":row[2]})
            A.update({"C":row[3]})
            A.update({"D":row[4]})
            qs = row[0]
            print(qs)
            ca = row[5]
            ex = row[6]
            t = row[7] #eval this
            QList.append(Question(qs,A,ca,ex,t))
    return(QList)

def MainMenu(): 
    QuestionList = []
    EndProgram = False
    while EndProgram ==False:
        print("Menu: ")
        print("1 new question")
        print("2 Run Quiz")
        print("3 Exit program")
        Menu = input()
        QuestionList = ReadQuestions(QuestionList)
        if Menu == "1":
            QuestionList = ReadQuestions()
            ChangeQuestions(QuestionList)
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

def ChangeQuestions(QuestionList): #Alice

    print("1 to add new question")
    QuestionOption = input("Answer: ")
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

        with open(r"Questions.csv",'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([q,d["A"],d["B"],d["C"],d["D"],CorrectAnswer,ex,t])

    else:

        print("Invalid input")
MainMenu()#

