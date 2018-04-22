from Question import Question
from Quiz import Quiz
import csv
##This is the main running of the program, Will be basic calls to other methods and UI mainly

#def QuizLoop():
 #   while EndProgram != False: # This needs to have end conditions
        #Main menu function called
def WriteQuestions(QuestionList):
    with open("Questions.csv",'w',newline = '') as csvfile:
        writer = csv.writer(csvfile)
   #     print(QuestionList)
       # for  x in range(0,len(QuestionList)):
        #    a1 = QuestionList[x].Answers["A"]
         #   a2 = QuestionList[x].Answers["B"]
          #  a3 = QuestionList[x].Answers["C"]
           # a4 = QuestionList[x].Answers["D"]
            #data = [QuestionList[x].QuestionAsked,a1,a2,a3,a4,QuestionList[x].CorrectAnswer,QuestionList[x].Explanation,QuestionList[x].Topics]
            #writer.writerow(data)

        for  x in QuestionList:
            a1 = x.Answers["A"]
            a2 = x.Answers["B"]
            a3 = x.Answers["C"]
            a4 = x.Answers["D"]
            data = [x.QuestionAsked,a1,a2,a3,a4,x.CorrectAnswer,x.Explanation,x.Topics]
            writer.writerow(data)
            
def ReadQuestions():
    QList = []
    with open("Questions.csv","r") as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            #print(row) #QuestionList 
            #Q = row[0]
            #print(row)
            A = {}
            A.update({"A":row[1]})
            A.update({"B":row[2]})
            A.update({"C":row[3]})
            A.update({"D":row[4]})


            QList.append(Question(row[0],A,row[5],row[6],row[7]))
    #        print(QList[0].QuestionAsked)
     #       print(QList[0].Answers)
      #      print(QList[0].CorrectAnswer)
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
        if Menu == 1:
            QuestionList = ReadQuestions()
            ChangeQuestions(QuestionList)
            #WriteQuestions(QuestionList)
        elif Menu ==2:
           # QuestionList = ReadQuestions()
            UserQuiz = Quiz(['work'],QuestionList) ##Create the topic list
            #UserQuiz.SetupQuiz()
           # print(QuestionList[0])
            UserQuiz.TakeQuiz(QuestionList)
        elif Menu ==3:
            EndProgram = True
      #  print(UserQuiz.AllQuestions)
   # elif Menu ==3:






    #load all questions into the program from csv file
    # Options (More can be added)
    #1 Log in as admin to change stuff
    #2 GenerateQuiz (call Quiz.Quiz.SetupQuiz())
    #3 Run With all Q's in random order (call Quiz.Quiz.SetupQuiz())




    #Once Games over return to 3/4 depending on which was selected
def ChangeQuestions(QuestionList): #Alice

    print("1 to add new question")
    QuestionOption = input("Answer: ")
    #print(QuestionOption)
    #d = {}
    if QuestionOption == 1:
        d = {"A":"","B":"","C":"","D":""}

        q = raw_input("Enter the question: ")
      
        A= raw_input("Enter answer A: ")
        d.update({'A': A })
        
        B= raw_input("Enter answer B: ")
        d["B"] = B
        
        C =raw_input("Enter answer C: ")
        d["C"] = C
        
        D= raw_input("Enter answer D: ")
        d["D"] = D

        CorrectAnswer = raw_input("Enter the correct answer (A,B,C,D)")
        ex = raw_input("Enter an explination for your answer: ")
        t = raw_input("Enter list of topics seperated by SPACE").split()
        #x = Question()
        QuestionList.append(Question(q,d,CorrectAnswer,ex,t))

        with open("Questions.csv",'w',newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([q,d["A"],d["B"],d["C"],d["D"],CorrectAnswer,ex,t])

    else:

        print("Invalid input")


   
    #Allows quesitons to be changed/ added / deleted
    #Using Question class basically
    #def Verify(FUNCT):
    #Ensures a COMSC staff member is there to run
    #a function
    #Verify .....
        #if verified
            #FUNCT()
MainMenu()#

