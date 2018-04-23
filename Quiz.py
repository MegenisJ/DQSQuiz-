import Question
class Quiz: ##for creating and running a quiz with a list of topics and Question
    def  __init__(self,_TopicList,_AllQuestions):
        Quiz.AllQuestions = _AllQuestions #list of Question objects
        Quiz.TopicList = _TopicList
        Quiz.QuesitonList = []

    def SetupQuiz(self): ##Needs finsishing
        for q in Quiz.AllQuestions:
            for i in q.Topics:
                for t in Quiz.TopicList:
                    if i == t:
                        if q not in Quiz.QuestionList:
                            Quiz.QuesitonList.append(q)
        #This takes the topic list and uses it to determine which Questions are in the Quiz
        #It uses this to create a bank of quesitons which can be used by the quiz
        #Saved as Quiz.QuestionList



    def TakeQuiz(self,QL): #Pass in a list of QuestionObjects
        EndQuiz = False;
        while not EndQuiz:
            for q in QL:
                print("'E' to exit")
                print(q.QuestionAsked)
                print("A: " + q.Answers["A"])
                print("B: " + q.Answers["B"])
                print("C: " + q.Answers["C"])
                print("D: " + q.Answers["D"])

                UserAnswer = input("Answer(A,B,C,D): ")
                if UserAnswer == q.CorrectAnswer:
                    print("That answer is Correct")
                elif UserAnswer == "E":
                    EndQuiz = True
                    break 
                else:
                    print("That answer is Incorrect")

                    print("The answer is " + q.CorrectAnswer + " because " +  q.Explanation)
            EndQuiz = True

            ##exit and and point to view stats and then jump back


        #Generates a quesiton one by one from the Question List and compares them to the right answers and provides and Explanation as a string
        ##gets school name and year group 