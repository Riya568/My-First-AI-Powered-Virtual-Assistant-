import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# listener = aa.Recognizer()
# machine = pyttsx3.init()

# def talk(text):
#     machine.say(text)

#     machine.runAndwait()

#     def input_instruction():
#         global instruction

# try:
#          with aa.microphone() as origin:
#             print("listening")
#             speech = listener.listen(origin)
#             instruction = listener.recognize_goggle(speech)
#             instruction = instruction.lower()
#             if "jarvis" in instruction:
#                   instruction = instruction.replace('jarvis', '')
#                   print(instruction)
            

            

#       except:
#          pass
#       return instruction


def play_Jarvis():

   # instruction = input_instruction() 
   instruction="how are you"
   print(instruction) 
   if "play" in instruction:
       song = instruction.replace('play', "")
      #  talk("playing" + song)
       pywhatkit.playonyt(song)


   elif 'time' in instruction:
       time = datetime.datetime,now().strftime('%I:%M%P')
      #  talk('current time'+ time)

   elif 'date' in instruction:
       date = datetime.datetime,now(),strftime('%d /%m /%Y')
      #  talk("Today's date " + date)

   elif 'how are you' in instruction:
       print("I am fine, how about you")
      #  talk('I am fine, how about you')

   elif 'What is your name' in instruction:
       print("i am Jarvis, What can I do for you?")
      #  talk('i am Jarvis, What can I do for you?')

   elif 'who is' in instruction:
       human = instruction.replace('who is', "")
       info = wikipedia.summary(human,1)
       print(info)
      #  talk(info)


   else:
       pass
      #  talk('please repeat')      
play_Jarvis()     



