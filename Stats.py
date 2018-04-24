
class Stats:
    def __init__(self,Total,Correct, QuitFreq):
        Stats.TotalAnswered = Total
        Stats.TotalCorrect = Correct
        Stats.QuitFrequency = QuitFreq
   # def SetupStats(self):
        #This takes the topic list and uses it to determine which Questions are in the Stats
        #It uses this to create a bank of quesitons which can be used by the Stats
        #Saved as Stats.QuestionList

    #def TakeStats(self):
        #Generates a quesiton one by one from the Question List and compares them to the right answers and provides and Explanation as a string

    #def SaveStats(self):
        #Creates a stats attrribute with varios stats that can be saved / looked at / accessed

    #def TimesAnswered(self):
        #Stats.TotalAttempted

    def CalcPercentCorrect(self):
        return((Stats.TotalCorrect/Stats.TotalAnswered)*100)

    def CalcPercentQuit(self):
        return((Stats.QuitFrequency/Stats.TotalAnswered)*100)