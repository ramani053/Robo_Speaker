import pyttsx3
print("Welcome to RoboSpeaker 1.1 Created by Ramani")
engine = pyttsx3.init()
while True:
  x=input("Enter what you want me to speak:")
  engine.say(x)
  engine.runAndWait()
  if x.lower()=='bye':
     break
