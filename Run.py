##This is the main running of the program, Will be basic calls to other methods and UI mainly
def InitializeQuiz():
    #calls Question.AddQuestion from a QuestionBanks.csv file to add all of them to the program

    #Loads previous stats from a PreviousStats.csv file

def QuizLoop():
    while EndProgram == False: # This needs to have end conditions
        #Main menu function called

def MainMenu():
    # Options (More can be added)
    #1 Log in as admin to change stuff
    #2 GenerateQuiz (call Quiz.Quiz.SetupQuiz())
    #3 Run With all Q's in random order (call Quiz.Quiz.SetupQuiz())




    #Once Games over return to 3/4 depending on which was selected
def ChangeQuestions():
    #Allows quesitons to be changed/ added / deleted
def Verify(FUNCT):
    #Ensures a COMSC staff member is there to run
    #a function
    #Verify .....
        #if verified
            #FUNCT()
