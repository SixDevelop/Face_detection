from cmath import nan
import random
from tkinter import (LEFT, RIGHT, TOP, Button, Canvas, Entry, Frame, Label,
                     OptionMenu, StringVar, W, Scrollbar, VERTICAL,Y)
import cv2
from matplotlib import image

from numpy import NaN

from core.config.config import ALL_METHODS, DATA_PATH
from core.recognition import parallel_recognition, recognition, single_photo_recognition
from PIL import Image, ImageTk
from tkinter import filedialog


class ExperimentFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.consistent_frame = Frame(self)
        self.parallel_frame = Frame(self)
        self.canvas_frame = Frame(self)
        self.img = NaN

    # =============== ПОСЛЕДОВАТЕЛЬНАЯ СИСТЕМА ===============

        self.cons_label = Label(
            self.consistent_frame,
            text="Single",
            font='Times 25'
        )

        self.scroll_y = Scrollbar(self, orient=VERTICAL)

        self.method_label = Label(self.consistent_frame, text="Method: ")

        self.method = StringVar()
        self.method.set(ALL_METHODS[1])
        self.method_drop = OptionMenu(
            self.consistent_frame,
            self.method,
            *ALL_METHODS
        )
        self.method_drop.configure(width=10)

        # Параметр метода
        self.param_label = Label(self.consistent_frame, text="Param: ")
        self.p_entry = Entry(self.consistent_frame, width=7)

        # Номер, с которого будут браться шаблоны для каждого человека
        self.from_templ_label = Label(self.consistent_frame, text="From: ")
        self.from_template_entry = Entry(self.consistent_frame, width=7)

        # Номер, по который будут браться шаблоны для каждого человека
        self.to_templ_label = Label(self.consistent_frame, text="Till: ")
        self.to_template_entry = Entry(self.consistent_frame, width=7)
        self.score_label = Label(self.consistent_frame, text="Score:")
        self.score_result = Label(self.consistent_frame, text="")

        # Список классифицируемых изображений
        self.result_images = []

        self.masked_images = []

        # Список содержащий по шаблону для
        # каждого из классифицируемых изображений
        self.templates = []

        # Запуск исследования
        self.run_but = Button(
            self.consistent_frame,
            text="Start",
            command=lambda: self.consistent_experiment()
        )

    # =============== ПАРАЛЛЕЛЬНАЯ СИСТЕМА ===============
        self.parallel_label = Label(
            self.parallel_frame,
            text="Voting",
            font='Times 25'
        )

        self.addPhotoBtn = Button(self.parallel_frame, text="Add photo", command=lambda: self.open_file())

        # ПАРАМЕТРЫ

        # Histogram
        self.hist_label = Label(self.parallel_frame, text="Histogram: ")
        self.hist_entry = Entry(self.parallel_frame, width=7)

        # Scale
        self.scale_label = Label(self.parallel_frame, text="Scale: ")
        self.scale_entry = Entry(self.parallel_frame, width=7)

        # Gradient
        self.gradient_label = Label(self.parallel_frame, text="Gradient: ")
        self.gradient_entry = Entry(self.parallel_frame, width=7)

        # DFT
        self.dft_label = Label(self.parallel_frame, text="DFT: ")
        self.dft_entry = Entry(self.parallel_frame, width=7)

        # DCT
        self.dct_label = Label(self.parallel_frame, text="DCT: ")
        self.dct_entry = Entry(self.parallel_frame, width=7)

        # Число шаблонов
        self.templ_num_label = Label(self.parallel_frame, text="L: ")
        self.templ_num_entry = Entry(self.parallel_frame, width=7)

        # Запуск параллельного исследования
        self.parallel_button = Button(
            self.parallel_frame,
            text="Start",
            command=lambda: self.parallel_experiment()
        )

        self.canvas = Canvas(self.canvas_frame, width=1000, height=900)
        self.scroll_y = Scrollbar(
            self,
            orient=VERTICAL,
            command=self.canvas.yview
        )

        self.canvas.config(
            xscrollcommand=self.scroll_y.set,
            scrollregion=self.canvas.bbox("all")
        )

        self.scroll_y.config(command=self.canvas.yview)

    # =============== МЕСТОПОЛОЖЕНИЕ ВИДЖЕТОВ ===============

        self.consistent_frame.pack(side=TOP, anchor=W)
        self.parallel_frame.pack(side=TOP, anchor=W)
        self.canvas_frame.pack(side=TOP, anchor=W)

        self.scroll_y.pack(side=RIGHT, fill=Y)
        # Настройка фрейма для последовательной системы
        # self.cons_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        # self.method_label.pack(side=LEFT, anchor=W, padx=10, pady=7)
        # self.method_drop.pack(side=LEFT, anchor=W, padx=10, pady=7)

        # self.param_label.pack(side=LEFT, anchor=W, padx=10, pady=7)
        # self.p_entry.pack(side=LEFT, anchor=W, padx=10, pady=7)

        # self.from_templ_label.pack(side=LEFT, anchor=W, padx=10, pady=7)
        # self.from_template_entry.pack(side=LEFT, anchor=W, padx=10, pady=7)

        # self.to_templ_label.pack(side=LEFT, anchor=W, padx=10, pady=7)
        # self.to_template_entry.pack(side=LEFT, anchor=W, padx=10, pady=7)

        # self.run_but.pack(side=LEFT, anchor=W, padx=10, pady=7)

        # self.score_label.pack(side=LEFT, anchor=W, padx=10)
        # self.score_result.pack(side=LEFT, anchor=W)

        # Настройка фрейма для параллельной системы
        self.parallel_label.pack(side=TOP, padx=10, pady=7, anchor=W)
        self.addPhotoBtn.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.hist_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.hist_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.scale_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.scale_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.gradient_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.gradient_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.dft_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.dft_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.dct_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.dct_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.templ_num_label.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.templ_num_entry.pack(side=LEFT, padx=10, pady=7, anchor=W)
        self.parallel_button.pack(side=TOP, padx=10, pady=7, anchor=W)

        # Настройка фрейма с Canvas
        self.canvas.pack(side=TOP)

    def consistent_experiment(self) -> None:
        """
        Проведение эксперимента с последовательной системой
        и отображение результатов.
        """
        score, images, templates = recognition(
            "ORL",
            # research_method.get(),
            self.method.get(),
            int(self.p_entry.get()),
            int(self.from_template_entry.get()),
            int(self.to_template_entry.get()),
        )
        self.score_result.config(text=score)

        templ_posx = 50
        templ_posy = 50

        res_posx = 300
        res_posy = 50


        # random_indexes = [random.randrange(len(images)) for _ in range(5)]



        for index in range(len(images)):
            templ = Image.fromarray(templates[index])
            templ.resize((50, 50))
            templ = ImageTk.PhotoImage(templ)
            self.templates.append(templ)
            self.canvas.create_image(templ_posx, templ_posy, image=templ)

            templ_posy += 120

            img = Image.fromarray(images[index])
            img.resize((50, 50))
            img = ImageTk.PhotoImage(img)
            self.result_images.append(img)
            self.canvas.create_image(res_posx, res_posy, image=img)

            res_posy += 120

    def parallel_experiment(self) -> None:
        """
        Проведение эксперимента с параллельной системой
        и отображение результатов.
        """
        global img
        global templ
        global iamg

        params = [
            ('hist', int(self.hist_entry.get())),
            ('scale', int(self.scale_entry.get())),
            ('grad', int(self.gradient_entry.get())),
            ('dft', int(self.dft_entry.get())),
            ('dct', int(self.dct_entry.get()))
        ]
        if False:
            L = int(self.templ_num_entry.get())
            scores = parallel_recognition(
                db_name='ORL',
                params=params,
                templ_to=L
            )

            posx = 250
            posy = 250

            image = Image.open(
                DATA_PATH + "results/parallel_experiment_result.png"
            )
            image = image.resize((500, 300))
            image = ImageTk.PhotoImage(image)
            self.result_images.append(image)
            self.canvas.create_image(posx, posy, image=image)
        else:
            
            need_templ = single_photo_recognition(
                db_name='ORL',
                params=params,
                test_db="ORL_Cloaked",
                b = 1
            )
            masked_templ = single_photo_recognition(
                db_name='ORL',
                params=params,
                test_db="ORL_Masked",
                b = 0
            )
            need_templ.append(masked_templ[1])
            templ_posx = 50
            templ_posy = 50

            res_posx = 300
            res_posy = 50

            mask_posx = 550
            mask_posy = 50
            
            for index in range(len(need_templ[0])):
                
                
                # self.canvas.delete("all") 

                templ = Image.fromarray(need_templ[0][index])
                templ.resize((50, 50))
                templ = ImageTk.PhotoImage(templ)
                self.templates.append(templ)
                # self.canvas.create_image(templ_posx, templ_posy, image=self.templates[index])
                # self.canvas.itemconfig()

                img = Image.fromarray(need_templ[1][index])
                img.resize((50, 50))
                img = ImageTk.PhotoImage(img)
                self.result_images.append(img)
                # self.canvas.create_image(res_posx, res_posy, image=img)

                iamg = Image.fromarray(need_templ[2][index])
                iamg.resize((50, 50))
                iamg = ImageTk.PhotoImage(iamg)
                self.masked_images.append(iamg)
                # self.canvas.create_image(mask_posx, mask_posy, image=iamg)
                # self.canvas.itemconfig(self.canvas, image = iamg)

            for index in range(len(self.templates)):
                print(index)
                self.canvas.create_image(templ_posx, templ_posy, image=self.templates[index])
                self.canvas.create_image(res_posx, res_posy, image=self.result_images[index])
                self.canvas.create_image(mask_posx, mask_posy, image=self.masked_images[index])

                # self.canvas.draw()
                from time import sleep

                sleep(0.1)
                # self.canvas.delete(self.templates[index])




    def open_file(self) -> None:
        """
        Открытие фотографии выбираемой пользоваелем
        """
        imgPath = filedialog.askopenfilename(title = 'open')
        self.img = imgPath
        # self.trueImage = cv2.imread(imgPath, -1)