import pyttsx3 as vc

engine = vc.init()

##
##
##Intro.append(["HEllO Sanket, I Am your Automated Interviewer. Lets Begin, Shall we?"])
##
##print(Intro[0])
##
##engine.say(Intro[0])
##
##engine.runAndWait()
##
##import time
##
##time.sleep(5)
##
##Intro.append(["Firstly, what is the purpose of your visit?"])
##
##print(Intro[1])
##
##engine.say(Intro[1])
##
##engine.runAndWait()

Intro = [["HEllO Sanket, I Am your Automated Interviewer. Lets Begin, Shall we?"],
         ["Firstly Good morning, How are you doing today?"],
         ["Firstly, what is the purpose of your visit?"],
         ["Have you given any competitive Examinations for your appliction?"],
         ["How many universities have you applied to, and how many accepts or rejects have you gotten?"],
         ["Name the universities:"],
         ["Why this degree at this University?"],
         ["Isnt this degree offered in India, why not in India?"],
         ["Who is sponsoring you?"],
         ["How will you manage your expenses?"],
         ["How did you prepare for this interview?"],
         ["tell me about your academic background"],
         ["What will you do after your Masters?"]]

Time = [1,1,2,2,2,3,5,6,6,5,3,3]

Introdic = { 'Question': ['How are you doing?','What time is it?'], 'Time': [3,4]
    }

Introdict = {'Question': Intro, 'Time': Time}


ans = "Y"
i = 0
import time

while ans == "Y" or ans == "R" and i in range(len(Introdict["Question"])):
    print(Introdict['Question'][i])
    engine.say(Introdict['Question'][i])
    engine.runAndWait()
    time.sleep(Introdict['Time'][i])
    ans = input("Continue?(Y/N/Redo(R))")
    if ans == "Y":
        i+=1
    elif ans == "N":
        break
#TODOs: Record voice and replay at choice.

