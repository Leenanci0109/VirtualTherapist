from tkinter import *
from PIL import ImageTk
import PIL.Image
from stot3 import *
from emoimage import *
import webbrowser
import pyttsx3

sug={"sad":["https://youtu.be/tBGvOmUhhq4","https://youtu.be/zzfREEPbUsA","https://youtu.be/af3Dmfsotbc",
            "https://www.bestcounselingdegrees.net/resources/depression-self-help-books/",
            "https://youtu.be/mQZWmxtdQ9E"],
     "happy":["https://youtu.be/eAnkDcH1mfw","https://youtu.be/pp9LuMD_IFk","https://youtu.be/oHv6vTKD6lg","https://youtu.be/ZbZSe6N_BXs","https://youtu.be/nfWlot6h_JM"],
     "angry":["https://youtu.be/uLCOnkLnJ-0","https://youtu.be/ie5yjNGLxfQ","https://www.psychologytoday.com/us/blog/chill-pill/201501/10-tips-reducing-anger",
     "https://www.helpguide.org/articles/relationships-communication/anger-management.htm","https://youtu.be/MIr3RsUWrdo"]
     }
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))
def suggestions(x):
    if (x == "female_sad" or x == "sad" or x == "male_sad"):
        y="sad"

    elif(x == "female_happy" or x == "happy" or x == "male_happy"):
        y="happy"

    elif(x == "female_angry" or x == "angry" or x == "male_angry"):
        y="angry"

    voice = "It seems you are "+str(y)+ " today." +" These are some suggestions. Click here to alleviate your mood!!"
    engine = pyttsx3.init()
    engine.setProperty('rate',180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  #0-male 1-female
    engine.say(voice)
    engine.runAndWait()
    link=[]
    img=[]
    pi=[]
    #y="happy"#remove
    #x=randint()
    for i in range(0,3):
        #f = "pics/" + y[0] + str(i + 1) + ".png"
        #img = PIL.Image.open(f)
        #img = img.resize((150, 75), PIL.Image.ANTIALIAS)
        #photoImg = ImageTk.PhotoImage(img)
        #lab = Label(project, image=photoImg, text=sug[y][i],pady=10)
        #lab.pack()
        #lab.bind("<Button-1>", callback)
        f="pics/"+y[0]+str(i+1)+".png"
        #print(f)
        z=PIL.Image.open(f)
        z=z.resize((250, 175), PIL.Image.ANTIALIAS)
        pimg=ImageTk.PhotoImage(z)
        #lab1 = Label(project, image=pimg, text=sug[y][i])

        #pi.append(ImageTk.PhotoImage(img[i]))
        w=Label(project, image=pimg, text=sug[y][i])
        w.photo=pimg
        #link.append(Label(project, text=sug[y][i], fg="blue",bg='#856ff8', cursor="hand2", font=("Arial Bold", 25),pady=10))
        #link[i].pack()
        w.pack(pady=10,padx=10,side=LEFT)
        w.place(x=225+i*270,y=350)
        w.bind("<Button-1>", callback)
        link.append(w)
    j=0
    for i in range(3,5):
        #f = "pics/" + y[0] + str(i + 1) + ".png"
        #img = PIL.Image.open(f)
        #img = img.resize((150, 75), PIL.Image.ANTIALIAS)
        #photoImg = ImageTk.PhotoImage(img)
        #lab = Label(project, image=photoImg, text=sug[y][i],pady=10)
        #lab.pack()
        #lab.bind("<Button-1>", callback)
        f="pics/"+y[0]+str(i+1)+".png"
        #print(f)
        z=PIL.Image.open(f)
        z=z.resize((250, 175), PIL.Image.ANTIALIAS)
        pimg=ImageTk.PhotoImage(z)
        #lab1 = Label(project, image=pimg, text=sug[y][i])

        #pi.append(ImageTk.PhotoImage(img[i]))
        w=Label(project, image=pimg, text=sug[y][i])
        w.photo=pimg
        #link.append(Label(project, text=sug[y][i], fg="blue",bg='#856ff8', cursor="hand2", font=("Arial Bold", 25),pady=10))
        #link[i].pack()
        w.pack(pady=10,padx=10,side=LEFT)
        w.place(x=350+j*270,y=550)
        j+=1
        w.bind("<Button-1>", callback)
        link.append(w)






def image():
    x=image1()
    y="It seems you are "+x
    label2 = Label(project, text=y,fg='white',pady=10,bg='#856ff8',font=("Courier", 25))
    label2.pack(pady=10)
    suggestions(x)
def voice():
    text1=voice1()
    x=text1[0]
    if (x == "female_sad" or x == "male_sad"):
        y="sad"

    elif(x == "female_happy"or x == "male_happy"):
        y="happy"

    elif(x == "female_angry" or x == "male_angry"):
        y="angry"
    y = "It seems you are " +y
    label1=Label(project, text=y,fg='white',pady=10,bg='#856ff8',font=("Courier", 25))
    label1.pack(pady=10)
    suggestions(text1[0])
def vt():
    global project
    project = Tk()
    project.geometry('1250x937')
    #project.place(justify="center")
    # project.configure(bg="dc39dc")
    project['background'] = '#856ff8'
    project.title(" Welcome to Virtual Therapy ")
    title =Label(project, text="Welcome to Virtual Therapy ", fg="yellow",bg='#856ff8', cursor="hand2", font=("Helvetica", 25),pady=10)
    title.pack(pady=10)
    #PILFile = Image.open("pics/im2.png")
    #Image = ImageTk.PhotoImage(PILFile)  # <---
    #ImageLabel = Label(project, image=Image)
    #ImageLabel.image = Image
    # ImageLabel.pack()
    # photo1 = PhotoImage(file = r"pics/b1.png")
    b1 = Button(project, bg='#DC39DC', text="By Voice", fg='white', command=voice, width=15, height=1)
    b1.configure(font=('Sans', '20', 'bold'))
    b1.pack(pady=10)
    # photo2 = PhotoImage(file = r"pics/b2.png")
    b2 = Button(project, bg='#DC39DC', text="By Image", fg='white', command=image, width=15, height=1)
    b2.configure(font=('Sans', '20', 'bold'))
    b2.pack( pady=10)
    project.mainloop()



if __name__=="__main__":
    vt()
