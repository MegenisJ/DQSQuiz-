def ChangeQuestions(QuestionList): #

    print("1 to add new question")
    QuestionOption = input("Answer: ")
    if QuestionOption == "1":
        d = {"A":"","B":"","C":"","D":""}

        q = input("Enter the question: ")
      
        A= input("Enter answer A: ")
        d.update({'A': A })
        
        B= input("Enter answer B: ")
        d["B"] = B
        
        C =input("Enter answer C: ")
        d["C"] = C
        
        D= input("Enter answer D: ")
        d["D"] = D

        CorrectAnswer = input("Enter the correct answer (A,B,C,D)")
        ex = input("Enter an explination for your answer: ")
        t = input("Enter a topic: ")
        #x = Question()
        QuestionList.append(Question(len(QuestionList),q,d,CorrectAnswer,ex,t))

        with open(r"Questions.csv",'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([len(QuestionList),q,d["A"],d["B"],d["C"],d["D"],CorrectAnswer,ex,t,0,0,0])

    else:

        print("Invalid input")
