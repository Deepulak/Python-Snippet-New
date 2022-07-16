import pendulum
import pyttsx3

def speak(text):
	engine = pyttsx3.init()
	engine.setProperty("rate", 170)
	voices = engine.getProperty("voices")
	engine.setProperty("voice", voices[1].id)
	engine.say(text)
	engine.runAndWait()

speak("Hello! I will convert time into deesired timezones.")

d1 = pendulum.now()

dt1 = str(d1).split(".")
speak("Here's your current timezone with current date and time")
print(f"Current timezone : {d1.timezone_name}")
print(f"Current date and time : {dt1[0]}")
speak("Now enter the zone you wish to see the time!")
i = input("Enter here : ")

try:
	d2 = pendulum.now(i)
	dt2 = str(d2).split(".")
	speak("Here's desired details")
	print(f"Current date and time for {d2.timezone_name} : {dt2[0]}")

except Exception as e:
	speak("Looks like you have entered the incorrect timezone!")
	speak("Please check it and try again!")
