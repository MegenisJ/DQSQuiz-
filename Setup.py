import csv
import pickle

#Bartosz Borne
topic_index = 6 #index of the topic attribute in the questions csv file

settings = {
    "topic": "",
    "schools_attending": [],
    "year_groups_attending": []
}

def save_settings():
    with open("settings.pickle", "wb") as file:
        pickle.dump(settings, file, pickle.HIGHEST_PROTOCOL)

def load_settings():
    with open("settings.pickle", "rb") as file:
        pickle.load(file)
        return (settings)


def select_topic():
    #Create list of unique topics
    topics = []
    with open("questions.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[topic_index] not in topics:
                topics.append(row[topic_index])

    while True:
        #Display list of topics
        for i in range(len(topics)):
            print(str(i+1) + ". " + topics[i])
        try:
            choice = int(input("0. Cancel\n\nSelect topic number: "))
            if choice == 0:
                break
            elif choice in range(1, len(topics)+1):
                chosen_topic = topics[choice-1]
                settings["topic"] = chosen_topic
                print("The topic is now set to: " + chosen_topic)
                break
            else:
                print("Invalid command.")
        except:
            print("Invalid command. Enter a digit.")

    save_settings()
    return(chosen_topic)
#Ianto Jones
def enterSchool():
    schoolsAttending = []
    newList = []
    newListName = []
    for school in (settings["schools_attending"]):
        print(school)
    endofSchool = False
    

    while endofSchool == False:
        endInput = False
       
        print("1. Enter School, enter 0 when you want to stop.")
        print("2. Delete School.")

        schoolChoice = input("Select choice number: ")
        if schoolChoice == "0":
            endofSchool = True
            break
        elif schoolChoice == "1":
            while endInput == False:
                schoolname = input("Enter School's name: ")
                inList = False
                while inList == False:
                    validYear = False
                    if schoolname == "0":
                        endInput = True
                        break
                    elif schoolname == "":
                        print("Must input a School name")
                        schoolname = input("Enter School name: ")
                        print("---")
                        inList = False
                    # elif schoolname in schoolsAttending:
                    #     print("Already entered: " + schoolname + " - Enter a different School name.")
                    #     schoolname = input("Enter School name: ")
                    #     print("---")
                    #     inList = False
                    else:
                        while validYear == False:
                            schoolYear = (input("Enter YearGroup of school: "))
                            if schoolYear == "":
                                print("Year must be between 1 and 13.")
                            elif int(schoolYear) < 1:
                                print("Year must be between 1 and 13.")
                            elif int(schoolYear) > 13:
                                print("Year must be between 1 and 13.")
                            else:
                                schoolsAttending.append((schoolname, int(schoolYear)))
                                print("Entered: " + schoolname)
                                print("---")
                                inList = True
                                validYear = True
                                break
                        
        elif schoolChoice == "2":
            deleteSchool = input("Enter School's name you wish to remove: ")
            newList = [i for i in schoolsAttending if i[0] != deleteSchool]
            print("Deleted: " + deleteSchool)
            schoolsAttending = newList
        else:
            print("Invalid command.")
            print("---")

    settings["schools_attending"] = schoolsAttending  
    save_settings()
    #
    #FOR TESTING WHATS IN THE LIST
    #  
    #for school in (settings["schools_attending"]):
    #    print(school)
#
#FOR TESTING CODE
#
#enterSchool()
#select_topic()