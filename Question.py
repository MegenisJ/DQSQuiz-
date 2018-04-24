import csv
class Question:
	def  __init__(self,QuestionNum,QuestionStr,AnswersDict,StrTopic, CorrectAnswer,AnsFreq,CorrectFreq,QuitFreq):
		Question.QuestionNumber = QuestionNum
		Question.QuestionAsked = QuestionStr
		Question.Answers = AnswersDict #{"A":answera,B:anserB etc}
		Question.CorrectAnswer = CorrectAnswer #could be a string ("a","b","c","d") or int (1,2,3,4)
		#Question.Explanation = ExplanationStr ##explanation of the answer
		Question.Topic = StrTopic #topics this question relates too
		Question.TimesAnswered = int(AnsFreq)
		Question.CorrectAnswers = int(CorrectFreq)
		Question.QuitFrequency = int(QuitFreq)

	def SaveQ(QuestionList):
		with open('questions.csv', 'w', newline = '') as wcsvfile:
			wtr = csv.writer(wcsvfile)
			for q in QuestionList:
				wtr.writerow(Question)
