class Question:
    def  __init__(self,QuestionStr,AnswersDict, CorrectAnswer, ExplanationStr,TopicList):
        Question.QuestionAsked = QuestionStr
        Question.Answers = AnswersDict #{"A":answera,B:anserB etc}
        Question.CorrectAnswer = CorrectAnswer #could be a string ("a","b","c","d") or int (1,2,3,4)
        Question.Explanation = ExplanationStr ##explanation of the answer
        Question.Topics = TopicList #topics this question relates too

