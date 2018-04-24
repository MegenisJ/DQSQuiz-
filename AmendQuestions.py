##Alice Edwards
import csv
#index 0 = id
#index 1 = question
#index 2 = answer 1
#index 3 = answer 2
#index 4 = answer 3
#index 5 = answer 4
#index 6 = theme
#index 7 = correct answer

def save(records):
	with open('questions.csv', 'w', newline = '') as wcsvfile:
		wtr = csv.writer(wcsvfile)
		for record in records:
			wtr.writerow(record)
	
	#csvfile.seek(0)
	#for row in rdr:
	print("File written")
def alterQuestion(question):
	with open('questions.csv', 'r') as csvfile:
		rdr = csv.reader(csvfile)
		csvfile.seek(0)
		records = []
		newQ = input("What would you like to change the question to?")
		for row in rdr:
			if int(row[0]) == question:
				row[1] = newQ
			records.append(row)
	save(records)

def alterAnswers(question):
	with open('questions.csv', 'r') as csvfile:
		rdr = csv.reader(csvfile)
		records = []
		csvfile.seek(0)

		for row in rdr:
		
			if int(row[0]) == question:
			
				print("The current answers are: ")
				print(row[2])
				print(row[3])
				print(row[4])
				print(row[5])
				print("With " + str(row[7]) + " as the correct answer.")
				answer = int(input("Which answer would you like to replace: 1, 2, 3, or 4? Alternatively enter 5 to change which answer is stored as correct."))
				if answer == 1 or answer == 2 or answer == 3 or answer == 4:
					row[answer+1] = input("What would you like to replace it with?")
				elif answer == 5:
					row[7] = int(input("What would you like to replace it with?"))
				else:
					print("Incorrect input.")
					alterAnswers(question)
			records.append(row)
	save(records)

def alterTheme(question):
	with open('questions.csv', 'r') as csvfile:
		rdr = csv.reader(csvfile)
		records = []
		csvfile.seek(0)
		for row in rdr:
			if int(row[0]) == question:
				print("The current theme is: ")
				print(row[6])
				newTheme = input("What would you like to replace it with?")
				row[6] = newTheme
			records.append(row)
		save(records)
def deleteQuestion(question):
	records = []
	csvfile.seek(0)
	for row in rdr:
		if int(row[0]) != question:
			if int(row[0]) > question:
				row[0] = int(row[0]) - 1 
			records.append(row)

	save(records)


def main():
	menu = True
	with open('questions.csv', 'r') as csvfile:
		rdr = csv.reader(csvfile)
		while menu == True:
			csvfile.seek(0)
			print("Menu:")
			print("What question would you like to alter?")
			for row in rdr:
				print(str(row[0]) + ": " + str(row[1]))#outputs all the questions
				
			question = int(input("Type the question number: "))
			print("")
			print("1. To alter question")
			print("2. Alter its answers")
			print("3. Alter its theme")
			print("4 Delete the Question")
			print("5. To quit")
			Qno = input("")
			if Qno == "1":
				alterQuestion(question)
			elif Qno == "2":
			
				alterAnswers(question)
			elif Qno == "3":
			
				alterTheme(question)
			elif Qno == "4":
				deleteQuestion(question)
			elif Qno == "5":
			
				menu = False
			else:
				print("Incorrect input.")

#quit()