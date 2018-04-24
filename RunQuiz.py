from Question import Question
from Quiz import Quiz
from Stats import Stats
import AmendQuestions
import Setup
import csv


def MainMenu():

	QuestionList = ReadQuestionList()
	while True:
		print("Main Menu")
		print("1. Run Quiz")
		print("2. Change/ Delete Questions")
		print("3. Add new Question")
		print("4. Change topic")
		print("5. Add to list of schools attending")
		print("6. Stats")
		print("7. Exit")
		#print("4. View Stats")
		menu = input()
		#ReadQuestionList()
		if menu == "1": #run quiz

			settings = Setup.load_settings()
			print("please select a topic:")
			Topic = Setup.select_topic()
			UserQuiz = Quiz(Topic)

			UserQuiz.TakeQuiz(Topic)

		elif menu =="2": #Alice Change / Delete Questions
			if Verify() == True:
				QuestionList = ReadQuestionList()
				AmendQuestions.main()

		elif menu =="3":	 # Add a new question
			if Verify() == True:
				AddQuestion(QuestionList)
		elif menu =="4": #Change the topic
			if Verify() == True:
				Topic = Setup.select_topic()
		elif menu == "5": #change attending schools
			if Verify() == True:
				Setup.enterSchool()
		elif menu =="6":
			if Verify() == True:
				for q in QuestionList:
					with open('questions.csv', 'r') as csvfile:
						rdr = csv.reader(csvfile)
						for row in rdr:
							print("Question " + row[0])
							s= Stats(int(row[8]),int(row[9]),int(row[10]))
							pc = s.CalcPercentCorrect()
							pq = s.CalcPercentQuit()
							print("Percentage of time answered correct: " + str(pc) + "%")
							print("Percentage of time quiz is quit on this question: " + str(pq) + "%")

		elif menu =="7":
			break
			#False
		else:
			print("invalid input")
def Verify():
	print("Enter password")
	checkpass = input()
	if checkpass =="staff":
		return True
	else:
		print("Incorrect password")
		return False
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

def AddQuestion(QuestionList):
	d = {"A":"","B":"","C":"","D":""}
	q = input("Enter the question: ")
	A = input("Enter answer A: ")
	d.update({'A': A })
	B= input("Enter answer B: ")
	d["B"] = B

	C =input("Enter answer C: ")
	d["C"] = C

	D= input("Enter answer D: ")
	d["D"] = D

	CorrectAnswer = input("Enter the correct answer (A,B,C,D)")

	t = input("Enter a topic: ")
        #x = Question()
	#QuestionList.append(Question(len(QuestionList),q,d,CorrectAnswer,ex,t))
	QuestionList.append(Question(len(QuestionList),q,d,t,CorrectAnswer,0,0,0))
	#Question.SaveQ(QuestionList)
	with open(r"questions.csv",'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([len(QuestionList),q,d["A"],d["B"],d["C"],d["D"],t,CorrectAnswer,1,0,0])

MainMenu()
