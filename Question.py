class Question:
    def  __init__(self,QuestionStr,AnswersDict, CorrectAnswer, ExplanationStr,TopicList):
        Question.QuestionAsked = QuestionStr
        Question.Answers = AnswersDict #{A:answera,B:anserB etc}
        Question.CorrectAnswer = CorrectAnswer #could be a string ("a","b","c","d") or int (1,2,3,4)
        Question.Explanation = ExplanationStr ##explanation of the answer
        Question.Topics = TopicList #topics this question relates too



   # def AddQuestion(self):
        #Allows the user to enter a quesiton to be added to the Questions List,
        #topics need to be selected from a list of them to avoid errors
        #remove this i think?


    #def AmmendQuestion(self):
        #Allows the user to change a specific quesion



    #def DeleteQuestion(self):
        #Allows the user to remove any question
