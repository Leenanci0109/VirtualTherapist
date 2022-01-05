#import l1
#def h1():
 #   l1.hi()
#l1.hi()
from PIL import Image
import PIL.Image
from PIL import ImageTk
from tkinter import *
import webbrowser
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))
sug={"sad":["https://youtu.be/tBGvOmUhhq4","https://youtu.be/zzfREEPbUsA","https://youtu.be/af3Dmfsotbc",
            "https://www.bestcounselingdegrees.net/resources/depression-self-help-books/",
            "https://youtu.be/mQZWmxtdQ9E"],
     "happy":["https://youtu.be/eAnkDcH1mfw","https://youtu.be/pp9LuMD_IFk","https://youtu.be/oHv6vTKD6lg","https://youtu.be/ZbZSe6N_BXs","https://youtu.be/nfWlot6h_JM"],
     "angry":["https://youtu.be/uLCOnkLnJ-0","https://youtu.be/ie5yjNGLxfQ","https://www.psychologytoday.com/us/blog/chill-pill/201501/10-tips-reducing-anger",
     "https://www.helpguide.org/articles/relationships-communication/anger-management.htm","https://youtu.be/MIr3RsUWrdo"]
     }
project = Tk()
project.geometry('1250x937')
# project.configure(bg="dc39dc")
project['background'] = '#856ff8'
label2 = Label(project, text="hii",pady=10,bg='#856ff8')
label2.pack()
y="happy"
link=[]
project = Tk()
project.geometry('1250x937')
#project.place(justify="center")
    # project.configure(bg="dc39dc")
project['background'] = '#856ff8'
project.title(" Welcome to Virtual Therapy ")
title =Label(project, text="Welcome to Virtual Therapy ", fg="yellow",bg='#856ff8', cursor="hand2", font=("Helvetica", 25),pady=10)
title.pack( pady=10)
    #PILFile = Image.open("pics/im2.png")
    #Image = ImageTk.PhotoImage(PILFile)  # <---
    #ImageLabel = Label(project, image=Image)
    #ImageLabel.image = Image
    # ImageLabel.pack()
    # photo1 = PhotoImage(file = r"pics/b1.png")
b1 = Button(project, bg='#DC39DC', text="By Voice", fg='white', width=15, height=1)
b1.configure(font=('Sans', '20', 'bold'))
b1.pack(pady=10)
    # photo2 = PhotoImage(file = r"pics/b2.png")
b2 = Button(project, bg='#DC39DC', text="By Image", fg='white',width=15, height=1)
b2.configure(font=('Sans', '20', 'bold'))
b2.pack(pady=10)


for i in range(0, 3):
    # f = "pics/" + y[0] + str(i + 1) + ".png"
    # img = PIL.Image.open(f)
    # img = img.resize((150, 75), PIL.Image.ANTIALIAS)
    # photoImg = ImageTk.PhotoImage(img)
    # lab = Label(project, image=photoImg, text=sug[y][i],pady=10)
    # lab.pack()
    # lab.bind("<Button-1>", callback)
    f = "pics/" + y[0] + str(i + 1) + ".png"
    # print(f)
    z = PIL.Image.open(f)
    z = z.resize((150, 75), PIL.Image.ANTIALIAS)
    pimg = ImageTk.PhotoImage(z)
    # lab1 = Label(project, image=pimg, text=sug[y][i])

    # pi.append(ImageTk.PhotoImage(img[i]))
    w = Label(project, image=pimg, text=sug[y][i])
    w.photo = pimg
    # link.append(Label(project, text=sug[y][i], fg="blue",bg='#856ff8', cursor="hand2", font=("Arial Bold", 25),pady=10))
    # link[i].pack()
    w.pack(pady=10, padx=10,side=LEFT)
    w.place(x=200+2*i,y=200+2*i)
    w.bind("<Button-1>", callback)
    link.append(w)
j = 0

for i in range(3, 5):
    # f = "pics/" + y[0] + str(i + 1) + ".png"
    # img = PIL.Image.open(f)
    # img = img.resize((150, 75), PIL.Image.ANTIALIAS)
    # photoImg = ImageTk.PhotoImage(img)
    # lab = Label(project, image=photoImg, text=sug[y][i],pady=10)
    # lab.pack()
    # lab.bind("<Button-1>", callback)
    f = "pics/" + y[0] + str(i + 1) + ".png"
    # print(f)
    z = PIL.Image.open(f)
    z = z.resize((150, 75), PIL.Image.ANTIALIAS)
    pimg = ImageTk.PhotoImage(z)
    # lab1 = Label(project, image=pimg, text=sug[y][i])

    # pi.append(ImageTk.PhotoImage(img[i]))
    w = Label(project, image=pimg, text=sug[y][i])
    w.photo = pimg

    # link.append(Label(project, text=sug[y][i], fg="blue",bg='#856ff8', cursor="hand2", font=("Arial Bold", 25),pady=10))
    # link[i].pack()
    w.pack(pady=10, padx=10,side=LEFT)
    w.place(x=200 + 2 * i, y=200 + 2 * i)
    j += 1
    w.bind("<Button-1>", callback)
    link.append(w)
project.mainloop()