import Question
class Quiz:
    def  __init__(self,_TopicList,_AllQuestions):
        Quiz.AllQuestions = _AllQuestions #list of Question objects
       # Quiz.YearGroups = Years
        Quiz.TopicList = _TopicList
       # Quiz.Schools = Schools
        Quiz.QuesitonList = []

    def SetupQuiz(self):
        print(Quiz.TopicList)
        print(Quiz.AllQuestions)
        for i in Quiz.AllQuestions:
            print (i.Topics)
        print("setup quiz entered")
        for q in Quiz.AllQuestions:
            print("for q entered")
            for t in Quiz.TopicList:
                print("topic list entered")
                if t == q.Topics:
                    print("if t entered")
                    if q not in Quiz.QuestionList:
                        Quiz.QuesitonList.append(q)
        print(Quiz.QuesitonList[0].Topics)
        #This takes the topic list and uses it to determine which Questions are in the Quiz
        #It uses this to create a bank of quesitons which can be used by the quiz
        #Saved as Quiz.QuestionList

    def TakeQuiz(self):
        print("TakeQuiz entered")
        #SetupQuiz()
        EndQuiz = False;
        while EndQuiz == False:
            for q in Quiz.QuesitonList:
                print("'E' to exit")
                print(q.QuestionAsked)
                print("A: " + q.AnswersDict["A"])
                print("B: " + q.AnswersDict["B"])
                print("C: " + q.AnswersDict["C"])
                print("D: " + q.AnswersDict["D"])

                UserAnswer = input("Answer(A,B,C,D): ")
                if UserAnswer.upper() == p.CorrectAnswer:
                    print("Correct")
                elif UserAnswer.upper() == "E":
                    EndQuiz = True
                    break 
                else:
                    print("Incorrect")

                print(q.Explanation)
            EndQuiz = True
        #Generates a quesiton one by one from the Question List and compares them to the right answers and provides and Explanation as a string

    #def SaveStats(self):
        #Creates a stats attrribute with varios stats that can be saved / looked at / accessed
        #
