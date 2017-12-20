class Quesion:
    def  __init__(self,QuestionStr,AnswersDict, CorrectAnswerInt, ExplanationStr,TopicList):
        Question.QuestionAsked = QuestionStr
        Question.Answers = AnswersDict
        Question.CorrectAnswer = CorrectAnswerInt
        Question.Explanation = ExplanationStr
        Question.Topics = TopicList



    def AddQuestion(self):
        #Allows the user to enter a quesiton to be added to the Questions List,
        #topics need to be selected from a list of them to avoid errors



    def AmmendQuestion(self):
        #Allows the user to change a specific quesion



    def DeleteQuestion(self):
        #Allows the user to remove any question
