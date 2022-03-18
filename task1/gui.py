from re import template
from tkinter import *
from tkinter import ttk
from turtle import left
import numpy as np
import cv2
# loading Python Imaging Library
from PIL import ImageTk, Image

 
# To get the dialog box to open when required
from tkinter import filedialog
from tkinter.tix import NoteBook


color = (255, 0, 0)

def openFile():
    global img
    global cimg
    global cimg2
    imgPath = filedialog.askopenfilename(title = 'open')
    img = ImageTk.PhotoImage(Image.open(imgPath).resize((400,300)))
    cimg = cv2.imread(imgPath, 2)
    cimg2 = cimg.copy()
    my_image_label = Label(tab1, image = img, width=400, height=300).pack(side=LEFT)
    # myImgLabel = Label(tab2, image = img, width = 400, height=300).pack(side=LEFT)

def openFileVJ():
    global vimg
    global vcimg
    global vcimg2
    imgPath = filedialog.askopenfilename(title = 'open')
    vimg = ImageTk.PhotoImage(Image.open(imgPath).resize((400,300)))
    vcimg = cv2.imread(imgPath)
    vcimg2 = vcimg.copy()
    vJImgLabel = Label(tab2, image = vimg, width=400, height=300).pack(side=LEFT)

def change():
    global result_image
    w, h = ctemplate.shape[::-1]
    if r_var.get() == 1:
        cimg = cimg2.copy()
        method = eval('cv2.TM_SQDIFF')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, color, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)
    elif r_var.get() == 2:
        cimg = cimg2.copy()
        method = eval('cv2.TM_SQDIFF_NORMED')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, 255, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)
    elif r_var.get() == 3:
        cimg = cimg2.copy()
        method = eval('cv2.TM_CCORR')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, 255, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)
    elif r_var.get() == 4:
        cimg = cimg2.copy()
        method = eval('cv2.TM_CCORR_NORMED')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, 255, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)
    elif r_var.get() == 5:
        cimg = cimg2.copy()
        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, 255, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)
    elif r_var.get() == 6:
        cimg = cimg2.copy()
        method = eval('cv2.TM_CCOEFF_NORMED')
        res = cv2.matchTemplate(cimg,ctemplate,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cimg,top_left, bottom_right, 255, 2)
        cv2.imwrite("task1/images/result.jpg", cimg)
        result = Image.open('task1/images/result.jpg')
        result = result.resize((400,300))
        result_image = ImageTk.PhotoImage(result)
        result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)

def violaJones():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    image = vcimg
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]
    cv2.imwrite("task1/images/vresult.jpg", img)
    global v_result_image
    result = Image.open('task1/images/vresult.jpg')
    result = result.resize((400,300))
    v_result_image = ImageTk.PhotoImage(result)
    result_label = Label(tab2, image = v_result_image).pack(side=LEFT, padx=100)


def openTemplate():
    global template
    global ctemplate
    templatePath = filedialog.askopenfilename(title = 'open')
    template_label = Label(tab1, text = templatePath)
    template = ImageTk.PhotoImage(Image.open(templatePath).resize((200,200)))
    ctemplate = cv2.imread(templatePath, 0)
    my_template_label = Label(tab1, image = template, width=200, height=200).pack(side=LEFT,padx=10)

def tm_result():
    global result_image
    result = Image.open('task1/images/result.jpg')
    result = result.resize((400,300))
    result_image = ImageTk.PhotoImage(result)
    result_label = Label(tab1, image = result_image).pack(side=LEFT, padx = 10)


root = Tk()
root.title('task1')
root.geometry('1000x700')
frm = ttk.Frame(root, padding=10)
# frm.grid()

tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text = 'TemplateMatching')
tab_parent.add(tab2, text = 'WiolaJones')



# === ВИДЖЕТЫ ДЛЯ ПЕРВОЙ ВКЛАДКИ
r_var = IntVar()
r_var.set(0)


r0 = Radiobutton(tab1, text = 'Not chosen', variable=r_var, value=0)
r1 = Radiobutton(tab1, text = 'TM_SQDIFF', variable=r_var, value=1)
r1n = Radiobutton(tab1, text = 'TM_SQDIFF_NORMED', variable=r_var, value=2)
r2 = Radiobutton(tab1, text = 'TM_CCORR', variable=r_var, value=3)
r2n = Radiobutton(tab1, text = 'TM_CCORR_NORMED', variable=r_var, value=4)
r3 = Radiobutton(tab1, text = 'TM_CCOEFF', variable=r_var, value=5)
r3n = Radiobutton(tab1, text = 'TM_CCOEFF_NORMED', variable=r_var, value=6)
buttonopen = Button(tab1, text = 'Open image', command = openFile)
buttontemplate = Button(tab1, text = 'Open template', command= openTemplate)
button = Button(tab1, text="Start", command=change)
# label = Label(tab1, width=20, height=10)

r1.pack(anchor=W)
r1n.pack(anchor=W)
r2.pack(anchor=W)
r2n.pack(anchor=W)
r3.pack(anchor=W)
r3n.pack(anchor=W)
buttonopen.pack(side=TOP)
buttontemplate.pack(side=TOP)
button.pack(side=TOP)

r0 = Entry(tab1)
r1 = Entry(tab1)
r1n = Entry(tab1)
r2 = Entry(tab1)
r2n = Entry(tab1)
r3 = Entry(tab1)
r3n = Entry(tab1)
# button = Entry(tab1)
buttonopen = Entry(tab1)
buttontemplate = Entry(tab1)
tab_parent.pack(expand=1, fill='both')

button = Button(tab2, text='Open image', command=openFileVJ).pack()
button = Button(tab2, text='Get result', command=violaJones).pack()
button
root.mainloop()

