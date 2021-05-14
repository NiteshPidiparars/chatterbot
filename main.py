from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import Image, ImageTk
import pyttsx3 as pp  # pip install pyttsx3
import speech_recognition as s  # pip install speechRecognition
import threading

engine = pp.init()  # object creation
voices = engine.getProperty('voices')  # getting details of current voice
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("My Bot")
convo = [
    "Hello",
    "Hi there!",
    "What is your name ?",
    "My name is bot, i am created by nitesh.",
    "How are you ?",
    "I am doing great these days.",
    "Thank you.",
    "In which city you live ?",
    "I live in Indore.",
    "In which language you talk ?",
    "I mostly talk in English."
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer
trainer.train(convo)

# answer = bot.get_response("What is your name ?")
# print(answer)

# print("Talk to Bot")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("Bot : ", answer)

main = Tk()

main.geometry("500x650")
main.title("My Chat Bot")
image = Image.open('bot.png')
# The (450, 350) is (height, width)
image = image.resize((150, 150), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
photoL = Label(main, image=img)
photoL.pack(pady=5)

# takes query : it takes audio as input from user and convert it string.


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your Bot is Listening try to Speak....")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='en-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"


def ask_from_bot():
    # print("clicked")
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


# creating a main frame
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask From Bot", font=(
    "Verdana", 20), command=ask_from_bot)
btn.pack()

# creating a function


def enter_function(event):
    btn.invoke()


# going to bind main window with enter key....
main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
