# importing all the required
# libraries used in project 
from cmath import exp
from tkinter import *
from gtts import *
from PIL import ImageTk, Image

 
# this here helps to
# play the converted audio 
import os
 
# creating gui(tkinter window)
root = Tk()

# styling the frame which helps to 
# make our background stylish
frame1 = Frame(root,bg = "#2C3639",height = "200")
# place the widget in gui window
frame1.pack(fill = X)


#loading image 
img = (Image.open("abhi.png"))
#resizing image
resized_image = img.resize((600,300), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

#inserting image in Label
panel1 = Label(frame1, image=new_image)
panel1.pack(fill="both", expand="no")

 
 #inserting frame 2 in root window
frame2 = Frame(root,bg = "#F2D7D9",height = "750")
frame2.pack(fill=X)
 
 
# styling the label which show the text 
# in our tkinter window
label = Label(frame1, text = "Text to Speech Converter",
              font = "italic 30",
              bg = "#5694FE")
label.place(x = 100, y = 250)
 
 
 
# entry is used to enter the text 
entry = Entry(frame2, width = 45, bd = 4, font = 14)
 
entry.place(x = 90, y = 52)
entry.insert(0, "")
 
# define a function which can
# get text and convert into audio
def play():
 
    # Language in which you want to convert 
    language = "en"
 
    #creating a object to communicate
    #with gTTS api
 
    myobj = gTTS(text = entry.get(),
                lang = language,
                slow = False)
 
 
 
    # give the name as you want to 
    # save the audio
    myobj.save("convert.mp3")
    os.system("convert.mp3")
 
# a button which holds
# our play function using command = play
btn = Button(frame2, text = "Convert",
             width = "15", pady = 12,
             font = "bold, 15",
             command = play, bg='#B25068')

#geometry of button
btn.place(x = 230,
          y = 130)
 
# give  title to root/ window opened
root.title("text_to_speech_convertor")
 
 
# starting the gui
root.mainloop()