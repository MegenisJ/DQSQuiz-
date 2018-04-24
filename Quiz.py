from Question import Question  
from Stats import Stats
import csv
class Quiz: ##for creating and running a quiz with a list of topics and Question
    def  __init__(self,_Topic):
        Quiz.AllQuestions = ReadQuestionList() #list of Question objects
        Quiz.Topic = _Topic

    def TakeQuiz(self,Topic): #Pass in a list of QuestionObjects
        #self.SetupQuiz()
        QL = Quiz.AllQuestions
        EndQuiz = False;
        while EndQuiz == False:
            print("")
            print("~~~~~New Quiz~~~~~~")
            i = 0
            with open('questions.csv', 'r') as csvfile:
                rdr = csv.reader(csvfile)

                for row in rdr:
                    
                    if row[6] == Topic:
                        print("")
                        QL[i].TimesAnswered += 1

                        print("'E' to exit")
                 #   print(q.QuestionAsked)
                        print(row[1])
                        print("A: " + row[2])
                        print("B: " + row[3])
                        print("C: " + row[4])
                        print("D: " + row[5])

                        UserAnswer = input("Answer(A,B,C,D): ")
                        if UserAnswer.upper() == row[7]:
                        #row[9] += 1
                            QL[i].CorrectAnswers +=1
                            print("That answer is Correct")

                        elif UserAnswer == "E":
                            QL[i].QuitFrequency += 1
                            break 

                        elif UserAnswer == "staff":
                            EndQuiz = True
                            break
                        else:
                            print("That answer is Incorrect")

                            print("The answer is " + row[7])

                print("~~~~Thank you for using this quiz.~~~~")
                i = input("Press any key to start the quiz")
   
        ##exit and and point to view stats and then jump back


        #Generates a quesiton one by one from the Question List and compares them to the right answers and provides and Explanation as a string
        ##gets school name and year group 
def ReadQuestionList():
    QuestionList = []
    with open('questions.csv', 'r') as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            Answers = {"A":"","B":"","C":"","D":""}
            Answers["A"] = row[2]
            Answers["B"] = row[3]
            Answers["C"] = row[4]
            Answers["D"] = row[5]
            QuestionList.append(Question(row[0],row[1],Answers,row[6],row[7],row[8],row[9],row[10]))

    return(QuestionList)