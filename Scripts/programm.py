# -*- coding: utf-8 -*-
"""
@author:
Алина Пахомова
Екатерина Агафонова
Алиса Алёшина
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


movies=pd.read_excel("movies.xlsx")
rating=pd.read_excel("ratings.xlsx")
all_movie = rating.merge(movies)
rating_mean = pd.pivot_table(rating, values='rating', index=['movieId'],
                             aggfunc={'rating': np.mean})
films_with_mean_rating = rating_mean.merge(movies, left_on='movieId',
                                           right_on='movieId')

LARGEFONT = ("Verdana", 35)


"""
 @author: Алина Пахомова
 Основа интерфейса приложения, переключение между страничками
"""

class tkinterApp:
    """
     @author: Алина Пахомова
     Создается окно в котором мы будем работать и выстраиваются все параметры
    """
    root = tk.Tk()
    root.title('HSE.Films')
    root.geometry('1050x750+100+0')
    root.config(bg = '#121413')
    root.resizable(False, True)
    photo = tk.PhotoImage(file = './pin/logo.png')
    root.iconphoto(False, photo)

    def __init__(self):
        container = tk.Frame(tkinterApp.root)
        container.pack()

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1,  minsize = 1050)

        self.frames = {}
        for F in (StartPage, what_watch, selection, statistics):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)
        tkinterApp.root.mainloop()

    def show_frame(self, cont):
        print(cont)
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """
     @author: Алина Пахомова
     Данное поле открывается когда программа начинает работать
    """
    def __init__(self, parent, controller):
        """
        @author: Алина Пахомова
        Данная функция создает 3 окна: 'Что посмотреть', 'Подборки',
        'Статистика'

        """

        tk.Frame.__init__(self, parent,  bg = '#121413')

        label = tk.Label(self, text ="Startpage", font = LARGEFONT, bg =
                         '#121413', fg = '#ffffff')
        label.grid(row = 2, column = 4, padx = 10, pady = 10)

        main_menu = ['Что посмотреть', 'Подборки', 'Статистика']

        # НЕ РАБОТАЕТ!!! command  = statistics постоянно, не знаю почему

        # main_command = [what_watch, selection, statistics]
        # for i in range(3):
        #     print(controller.show_frame(main_command[i]))
        #     tk.Button(self, text = main_menu[i],
        #                font = ('Raleway', 20, 'bold'),
        #                bg = '#ffffff', fg = '#121413',
        #                activeforeground = '#a784e3',
        #                command = lambda: controller.show_frame(main_command
        # [i])).grid(row = 0, column = i, stick = 'snwe')
        #     self.grid_columnconfigure(i, minsize = 350)
        # self.grid_rowconfigure(0, minsize = 100)

        tk.Button(self, text = main_menu[0],
                        font = ('Raleway', 20, 'bold'),
                        bg = '#ffffff', fg = '#121413',
                        activeforeground = '#a784e3',
                        command = lambda: controller.show_frame(what_watch
                                )).grid(row = 0, column = 0, stick = 'snwe')
        tk.Button(self, text = main_menu[1],
                        font = ('Raleway', 20, 'bold'),
                        bg = '#ffffff', fg = '#121413',
                        activeforeground = '#a784e3',
                        command = lambda: controller.show_frame(selection
                                )).grid(row = 0, column = 1, stick = 'snwe')
        tk.Button(self, text = main_menu[2],
                        font = ('Raleway', 20, 'bold'),
                        bg = '#ffffff', fg = '#121413',
                        activeforeground = '#a784e3',
                        command = lambda: controller.show_frame(statistics
                                )).grid(row = 0, column = 2, stick = 'snwe')
        self.grid_columnconfigure(0, minsize = 350)
        self.grid_columnconfigure(1, minsize = 350)
        self.grid_columnconfigure(2, minsize = 350)
        self.grid_rowconfigure(0, minsize = 100)


class what_watch(tk.Frame):
    """
     @author: Алина Пахомова
    Фрейм открывается при нажатии кнопки "Что посмотреть"
    Здесь реализуется подбор фильмов для конкретного пользователя
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#121413')
        main_menu = ['Что посмотреть', 'Подборки', 'Статистика']
        main_command = [what_watch, selection, statistics]

        tk.Button(self, text=main_menu[1],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command[1]
                                        )).grid(row=0, column=1, stick='snwe')
        tk.Button(self, text=main_menu[2],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command[2]
                                    )).grid(row=0, column=2, stick='snwe')

        tk.Button(self, text=main_menu[0],
                  font=('Raleway', 30, 'bold'),
                  bg='#ffffff', fg='#a784e3',
                  command=lambda: controller.show_frame(main_command[0]
                                    )).grid(row=0, column=0, stick='snwe')

        lbl_1 = tk.Label(self, text='Выберите жанр',
                         font=('Raleway', 20),
                         fg='#ffffff', bg='#121413',
                         width=20, height=3)
        lbl_1.grid(row=2, column=1)

        self.grid_columnconfigure(0, minsize=350)
        self.grid_columnconfigure(1, minsize=350)
        self.grid_columnconfigure(2, minsize=350)
        self.grid_rowconfigure(0, minsize=100)
        self.yea_destroy = []
        self.genre_for_you = ''
        self.films_for_you = []
        self.decade_for_you = ''
        self.table_films = pd.DataFrame()
        self.dic_user = {}
        self.film_destroy = []

        genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy',
                  'Crime', 'Documentary', 'Film-Noir', 'Drama', 'Fantasy',
                  'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                  'Thriller', 'War', 'Western']

        years = ('2015-2020', '2010-2015', '2005-2010', '2000-2005',
                 '1995-2000', '1990-1995', '1985-1990', '1980-1985',
                 '1975-1980', '1970-1975', '1965-1970', '1960-1965',
                 '1955-1960', '1950-1955', '1945-1950', '1940-1945',
                 '1935-1940', '1930-1935', '1925-1930')
        i = 0
        k = 4
        p = 0

        list_gen = []
        for j in range(19):
            list_gen.append(tk.IntVar())

        list_yea = []
        for j in range(20):
            list_yea.append(tk.IntVar())

        list_film = []
        for j in range(5000):
            list_film.append(tk.IntVar())

        def what_to_see(year, genre):

            year = year.split("-")
            f1 = movies[movies["genre 1"] == genre]
            f2 = movies[movies["genre 2"] == genre]
            f3 = movies[movies["genre 3"] == genre]
            f4 = movies[movies["genre 4"] == genre]
            f5 = movies[movies["genre 5"] == genre]
            f6 = movies[movies["genre 6"] == genre]
            f7 = movies[movies["genre 7"] == genre]
            f8 = movies[movies["genre 8"] == genre]
            f9 = movies[movies["genre 9"] == genre]
            f10 = movies[movies["genre 10"] == genre]
            genreall = pd.concat([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10],
                                 sort=False, axis=0)
            new_movies = genreall[genreall["year"] > int(year[0])]
            new1 = new_movies[new_movies["year"] <= int(year[1])]
            new1 = pd.concat([new1['title']])
            b = new1
            b = list(b)
            return b

        def click4():
            '''
 @author: Алиса Алешина
 функция суммирует все рейтинги по данному жанру и фильмам которые понравились
 пользователю, затем выдает список фильмов, предложенных пользователю,
 по определенному критерию
             '''

            for mid in self.table_films:
                d = rating[rating['movieId'] == mid]
                for u in d['userId']:
                    d_user = u
                    r = d[d['userId'] == d_user]
                    d_rate = r['rating'].sum()
                    self.dic_user[d_user]=self.dic_user.get(d_user, 0)+d_rate
            maxim = 0
            for key in self.dic_user:
                maxim = max(maxim, self.dic_user[key])
                if self.dic_user[key] == maxim:
                    main_user = key
            for fi in self.film_destroy:
                fi.destroy()

            genre = self.genre_for_you
            year = self.decade_for_you
            user = main_user
            year = year.split("-")
            f1 = all_movie[all_movie["genre 1"] == genre]
            f2 = all_movie[all_movie["genre 2"] == genre]
            f3 = all_movie[all_movie["genre 3"] == genre]
            f4 = all_movie[all_movie["genre 4"] == genre]
            f5 = all_movie[all_movie["genre 5"] == genre]
            f6 = all_movie[all_movie["genre 6"] == genre]
            f7 = all_movie[all_movie["genre 7"] == genre]
            f8 = all_movie[all_movie["genre 8"] == genre]
            f9 = all_movie[all_movie["genre 9"] == genre]
            f10 = all_movie[all_movie["genre 10"] == genre]
            new1 = pd.concat([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10],
                             sort=False, axis=0)

            fim = new1[new1['userId'] == main_user]
            fim2 = fim[fim['rating'] >= 5]
            fim2 = pd.concat([fim2['title']])
            # fim2.reset_index(drop=True, inplace=True)
            b = fim2

            if b.empty:
                lbl = tk.Label(self, text='Ничего не найдено',
                               font=('Raleway', 14),
                               fg='#ffffff', bg='#121413',
                               width=20, height=3)
            else:
                # lbl = tk.Label(self, text=b, font=('Raleway', 14, 'italic'),
                # bg='#ffffff', fg='#a784e3')
                # lbl.grid(column=0, row=4, columnspan = 2, stick = "w")

                sb = tk.Scrollbar(self)
                sb.grid(row=4, column=2, rowspan = 3, stick = 'nse')
                mylist = tk.Listbox(self, yscrollcommand = sb.set, font=
                    ('Raleway', 14, 'italic'), bg='#ffffff', fg='#a784e3')
                for line in b:
                    mylist.insert(tk.END, str(line))
                mylist.grid(column=0, row=4, columnspan=2, stick = "we",
                            padx = 15)
                sb.config( command = mylist.yview )

            lbl_2 = tk.Label(self, text='Фильмы для Вас',
                             font=('Raleway', 20),
                             fg='#ffffff', bg='#121413',
                             width=20, height=3)
            lbl_2.grid(row=2, column=1)

        def click3():

            '''
 @author: Алиса Алешина
 функция обрабатывает кнопки на которые нажал пользователь по фильмам
             '''

            list_of_films = []
            my_films = []
            for i in range(len(list_film)):
                list_of_films.append(list_film[i].get())

            endbut = tk.Button(self, text='Завершить выбор',
                               font=('Raleway', 14, 'bold'),
                               bg='#a784e3', fg='#121413',
                               activeforeground='#a784e3',
                               command=click4)
            ############################
            endbut.grid(column=0, row=2)
            ###############################################
            for m in range(len(list_of_films) - 1):
                if list_of_films[m] == 1:
                    my_films.append(self.films_for_you[m - 3])

            # print(my_films)
            table_films_filter = movies[movies['title'].isin(my_films)]
            self.table_films = table_films_filter['movieId']
            # print(self.table_films)
            return self.table_films

            fil = []
            for m in my_films:
                fil.append(movies[movies['title'] == m]['title'])

        def click2():
            '''
 @author: Алиса Алешина
 функция генерирует список фильмов которые предлагаются пользователю на выбор
             '''

            list_of_values_years = []
            for i in range(20):
                list_of_values_years.append(list_yea[i].get())

            for y in range(len(list_of_values_years) - 1):
                if list_of_values_years[y] == 1:
                    self.decade_for_you = years[y - 1]
            for ye in self.yea_destroy:
                ye.destroy()
            lbl_2 = tk.Label(self, text='Выберите фильмы ',
                             font=('Raleway', 20),
                             fg='#ffffff', bg='#121413',
                             width=20, height=3)
            lbl_2.grid(row=2, column=1)
            self.films_for_you = what_to_see(self.decade_for_you,
                                          self.genre_for_you)
            i = 3
            ########################################
            for fil_f_u in self.films_for_you:
                fil = tk.Checkbutton(self, text=fil_f_u,
                                     font=('Raleway', 12, 'bold'),
                                     bg='#a784e3', fg='#121413',
                                     activeforeground='#a784e3', indicatoron=0,
                                     variable=list_film[i],command=click3)
                self.film_destroy.append(fil)
                fil.grid(column=0, row=i, columnspan=2, stick='w', padx=15)
                i += 1

        ################################################

        def click1():
            '''
 @author: Алиса Алешина
 функция обрабатывает год и жанр которые выбрал пользователь
             '''
            list_of_values = []
            for i in range(19):
                list_of_values.append(list_gen[i].get())
            for g in range(len(list_of_values) - 1):
                if list_of_values[g] == 1:
                    self.genre_for_you = genres[g - 1]
            p = 0
            j = 0
            i = 0
            k = 4
            for des in gen_dectroy:
                des.destroy()
            ########################################################Добавила
            lbl_2 = tk.Label(self, text='Выберите год',
                             font=('Raleway', 20),
                             fg='#ffffff', bg='#121413',
                             width=20, height=3)
            lbl_2.grid(row=2, column=1)
            ##################################################################
            for year in years:
                p += 1
                yea = tk.Checkbutton(self, text=year,
                                     font=('Raleway', 14, 'bold'),
                                     bg='#a784e3', fg='#121413',
                                     activeforeground='#a784e3', indicatoron=0,
                                     variable=list_yea[p], command=click2)
                self.yea_destroy.append(yea)
                yea.grid(column=i, row=k)
                i += 1
                j += 1
                if j % 3 == 0:
                    k += 1
                    i = 0

        gen_dectroy = []
        for genre in genres:
            p += 1
            gen = tk.Checkbutton(self, text=genre,
                                 font=('Raleway', 14, 'bold'),
                                 bg='#a784e3', fg='#121413',
                                 activeforeground='#a784e3', indicatoron=0,
                                 variable=list_gen[p], command=click1)
            gen_dectroy.append(gen)
            gen.grid(column=i, row=k)
            i += 1
            j += 1
            if j % 3 == 0:
                k += 1
                i = 0


class selection(tk.Frame):
    """
     @author: Алина Пахомова
    Фрейм открывается при нажатии кнопки "Подборки"
    Здесь реализуется возможность составить фильмы по определенным жанрам и
    году с учетом рейтинга
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#121413')
        main_menu = ['Что посмотреть', 'Подборки', 'Статистика']
        main_command = [what_watch, selection, statistics]
        tk.Button(self, text=main_menu[0],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command
                                [0])).grid(row=0, column=0, stick='snwe')
        tk.Button(self, text=main_menu[2],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command
                                [2])).grid(row=0, column=2, stick='snwe')

        tk.Button(self, text=main_menu[1],
                  font=('Raleway', 30, 'bold'),
                  bg='#ffffff', fg='#a784e3',
                  command=lambda: controller.show_frame(main_command
                                [1])).grid(row=0, column=1, stick='snwe')

        self.grid_columnconfigure(0, minsize=350)
        self.grid_columnconfigure(1, minsize=350)
        self.grid_columnconfigure(2, minsize=350)
        self.grid_rowconfigure(0, minsize=100)

        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                          {'configure':
                                           {'selectbackground': '#a784e3',
                                            'fieldbackground': '#a784e3',
                                            'background': '#ffffff'}}})
        combostyle.theme_use('combostyle')

        genres = ('Жанр', 'Adventure', 'Animation', 'Children', 'Comedy',
                  'Crime', 'Documentary','Drama', 'Fantasy', 'Sci-Fi',
                  'Thriller', 'War', 'Western')
        years = ("Год", '2015-2020', '2010-2015', '2005-2010', '2000-2005',
                 '1995-2000', '1990-1995', '1985-1990', '1980-1985',
                 '1975-1980', '1970-1975', '1965-1970', '1960-1965',
                 '1955-1960', '1950-1955', '1945-1950', '1940-1945',
                 '1935-1940', '1930-1935', '1925-1930')
        sorts = ('Сортировать по...', 'От лучшего к худшему',
                 'От худшего к лучшему')
        genre = ttk.Combobox(self, values=genres,
                             font=("Raleway Thin", 18, "bold"))
        year = ttk.Combobox(self, values=years, font=
                            ("Raleway Thin", 18, "bold"))
        sort = ttk.Combobox(self, values=sorts, font=
                            ("Raleway Thin", 18, "bold"))
        genre.current(0)
        year.current(0)
        sort.current(0)
        genre.grid(row=1, column=0)
        year.grid(row=1, column=1)
        sort.grid(row=1, column=2)
        self.grid_rowconfigure(1, minsize=100)

        def podborki(year, genre, sort):
            """


            @author: Катя Агафонова
            Функция принимает значения годов выпуска фильмов, их жанр и тип
            сортировки, выбранные пользователем, и возвращает таблицу DataFrame
            с названием, годом и средним рейтингом подходящих фильмов


            """
            year = year.split("-")
            f1 = movies[movies["genre 1"] == genre]
            f2 = movies[movies["genre 2"] == genre]
            f3 = movies[movies["genre 3"] == genre]
            f4 = movies[movies["genre 4"] == genre]
            f5 = movies[movies["genre 5"] == genre]
            f6 = movies[movies["genre 6"] == genre]
            f7 = movies[movies["genre 7"] == genre]
            f8 = movies[movies["genre 8"] == genre]
            f9 = movies[movies["genre 9"] == genre]
            f10 = movies[movies["genre 10"] == genre]
            genreall = pd.concat(
                [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10], sort=False, axis=0)
            print(genreall)
            rating_mean = pd.pivot_table(rating, values='rating', index=[
                                         'movieId'], aggfunc={'rating':
                                                              np.mean})
            genreall = rating_mean.merge(
                genreall, left_on='movieId', right_on='movieId')
            new_movies = genreall[genreall["year"] > int(year[0])]
            new1 = new_movies[new_movies["year"] <= int(year[1])]
            new1 = pd.concat([new1['title'], new1['year'], new1['rating']], axis=1)
            if sort == 'От лучшего к худшему':
                new2 = new1.sort_values(by='rating', ascending=False)
                b = new2
            elif sort == 'От худшего к лучшему':
                new3 = new1.sort_values(by='rating')
                b = new3
            else:
                b = new1
            b.reset_index(drop=True, inplace=True)
            return b

        def clck():
            """
            @author: Катя Агафонова
            Функция получает данные, выбранные пользователем, вызывает функцию
            преобразования этих данных в таблицу  и выводит на экран год,
            рейтинг и название подходящих фильмов

            """
            res = year.get()
            res2 = genre.get()
            res3 = sort.get()
            b = podborki(res, res2, res3)
            if b.empty:
                lbl.config(text="Ничего не найдено", font=('Raleway', 14,
        'italic'), bg='#ffffff', fg='#121413', activeforeground='#a784e3')
            else:
                sb = tk.Scrollbar(self)
                sb.grid(row=8, column=2, rowspan = 3, stick = 'nse')
                mylist = tk.Listbox(self, yscrollcommand = sb.set, font=
                    ('Raleway', 14, 'italic'), bg='#ffffff', fg='#a784e3')
                for line in range(len(b['title'])):
                    mylist.insert(tk.END, str(b['year'][line])+ "        "  +
                                  str(round(float(b['rating'][line]), 1)) +
                                  "         " + str(b['title'][line]))
                mylist.grid(column=0, row=8, columnspan=3, stick = "we",
                            padx = 15)
                sb.config( command = mylist.yview )


        lbl = tk.Label(self, text="Ищем...", font=('Raleway', 14, 'italic'))
        lbl.grid(column=0, row=8)
        bth = tk.Button(self, text='Вывод результатов', font=('Raleway', 14,
                                'italic'), bg='#ffffff', fg='#121413',
                        activeforeground='#a784e3', command=clck)
        bth.grid(column=2, row=10)

class statistics(tk.Frame):
    """
     @author: Алина Пахомова
    Фрейм открывается при нажатии кнопки "Статистика"
    Здесь реализуется возможность составлять графики
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#121413')

        main_menu = ['Что посмотреть', 'Подборки', 'Статистика']
        main_command = [what_watch, selection, statistics]
        tk.Button(self, text=main_menu[0],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command[0]
                                    )).grid(row=0, column=0, stick='snwe')
        tk.Button(self, text=main_menu[1],
                  font=('Raleway', 20, 'bold'),
                  bg='#ffffff', fg='#121413',
                  command=lambda: controller.show_frame(main_command[1]
                                    )).grid(row=0, column=1, stick='snwe')

        tk.Button(self, text=main_menu[2],
                  font=('Raleway', 30, 'bold'),
                  bg='#ffffff', fg='#a784e3',
                  activeforeground='#a784e3',
                  command=lambda: controller.show_frame(main_command[2]
                                    )).grid(row=0, column=2, stick='snwe')
        self.grid_columnconfigure(0, minsize=350)
        self.grid_columnconfigure(1, minsize=350)
        self.grid_columnconfigure(2, minsize=350)
        self.grid_rowconfigure(0, minsize=100)

        combostyle2 = ttk.Style()
        combostyle2.theme_use('combostyle')

        xcrits = ('Критерии по x', 'Жанр', '2014-2022', '2005-2013',
                  '1996-2004', '1987-1995', '1978-1986',
                 '1969-1977', '1960-1968', '1951-1959', '1942-1950')
        ycrits = ("Критерии по y","Средний рейтинг", "Количество оценок")
        xcrit = ttk.Combobox(self, values=xcrits, font=(
            "Raleway Thin", 18, "bold"))
        ycrit=ttk.Combobox(self, values=ycrits, font=(
            "Raleway Thin", 18, "bold"))
        xcrit.current(0)
        ycrit.current(0)
        xcrit.grid(row=1, column=1)
        ycrit.grid(row=1, column=0)
        def graphics(xcrit, ycrit):
            """

            @author: Катя Агафонова

            Функция принимает критерии по x(год или жанры) и критерии по y
            (средний рейтинг или количество оценок), выбранные пользователем,
            и возвращает таблицу DataFrame с нужными данными
            """
            # if rate=="Количество фильмов":
            #     z=films_with_mean_rating["rating"]
            # if rate =="Среднее число фильмов":
            #     z=films_with_mean_rating['year']
            # plt.boxplot(y, notch=True, showmeans=True) #год, в который
            # было снято среднее колво фильмов
            if ycrit=="Количество оценок":
                if xcrit!='Жанр' and xcrit!='Критерии по y':
                    xcrit=xcrit.split("-")
                    all_rating = pd.pivot_table(all_movie, index=['year'],
                                values=['rating'], aggfunc={'rating': len})
                    all_rating["year"] = all_rating.index
                    ind = np.array(range(1, 108))
                    all_rating = all_rating.set_index(ind)
                    x = all_rating[all_rating["year"] > int(xcrit[0])]
                    x = x[x["year"] <= int(xcrit[1])]
                    x = x["year"]
                    y = all_rating["rating"][x.index[0]-1:x.index[-1]]
                    z = pd.concat([x, y], axis=1)
                if xcrit=='Жанр':
                    #z=all_movie[all_movie['userId']==1]
                    v=pd.pivot_table(all_movie, index=['genre 1'], values=
                                     ['rating'], aggfunc={'rating':len})
                    v["genre 1"]=v.index
                    d=np.array(range(1,21))
                    u=v.set_index(d)
                    u=u.drop(labels = [1],axis = 0)
                    u=u.drop(labels = [2],axis = 0)
                    x=u['genre 1']
                    y=u['rating']
                    z = pd.concat([x, y], axis=1)
                    # plt.figure(figsize=(9.5,6))
            elif ycrit=='Средний рейтинг':
                if xcrit!='Жанр' and xcrit!='Критерии по y':
                    xcrit=xcrit.split("-")
                    mean_rating = pd.pivot_table(all_movie, index=['year'],
                            values=['rating'], aggfunc={'rating': np.mean})
                    mean_rating["year"] = mean_rating.index
                    ind = np.array(range(1, 108))
                    mean_rating = mean_rating.set_index(ind)
                    x = mean_rating[mean_rating["year"] > int(xcrit[0])]
                    x = x[x["year"] <= int(xcrit[1])]
                    x = x["year"]
                    y = mean_rating["rating"][x.index[0]-1:x.index[-1]]
                    z = pd.concat([x, y], axis=1)
                if xcrit=='Жанр':
                    #z=all_movie[all_movie['userId']==1]
                    v=pd.pivot_table(all_movie, index=['genre 1'], values=
                                     ['rating'], aggfunc={'rating':np.mean})
                    v["genre 1"]=v.index
                    d=np.array(range(1,21))
                    u=v.set_index(d)
                    u=u.drop(labels = [1],axis = 0)
                    u=u.drop(labels = [2],axis = 0)
                    x=u['genre 1']
                    y=u['rating']
                    z = pd.concat([x, y], axis=1)
                    # plt.figure(figsize=(9.5,6))
                    # plt.scatter(x,y, marker="^", color="#DC143C")
            return z

        def clck2():
            """

            @author: Катя Агафонова
            Функция получает данные, выбранные пользователем, вызывает функцию
            преобразования этих данных в таблицу и выводит на экран график
            зависимости этих данных друг от друга

            """
            global canvas1
            canvas1=None
            if canvas1:
                canvas1.get_tk_widget().destroy()
            res = xcrit.get()
            res2 = ycrit.get()
            data = graphics(res, res2)
            b=int(data.index[0])
            if data.columns[0]=="genre 1":
                plt.rcParams['xtick.labelsize'] = '6'
                # тоже меняет размер шрифта жанров
                # for label in ax.get_xticklabels():
                    #     label.set_fontsize(6)
                fig = Figure(figsize=(10, 4), dpi=100)
                ax = fig.add_subplot(111)
                if data["rating"][b]>6:
                    ax.set_title
                    ('График зависимости количества оценок от жанра')
                    ax.set_ylabel('Количество оценок')
                else:
                    ax.set_title
                    ('График зависимости среднего рейтинга от жанра')
                    ax.set_ylabel('Средний рейтинг')
                ax.set_xlabel('Жанр')
                ax.scatter(data["genre 1"], data["rating"], color='#a784e3',
                           marker="*")
            if data.columns[0]=="year":
                fig = Figure(figsize=(5, 4), dpi=100)
                ax = fig.add_subplot(111)
                if data["rating"][b]>6:
                    ax.set_title
                    ('График зависимости количества оценок от года')
                    ax.set_ylabel('Количество оценок')
                else:
                    ax.set_title
                    ('График зависимости среднего рейтинга от года')
                    ax.set_ylabel('Средний рейтинг')
                ax.set_xlabel('Год выпуска')
                ax.bar(data["year"], data["rating"], color='#a784e3')
            canvas1 = FigureCanvasTkAgg(fig, master=self)
            canvas1.draw()
            canvas1.get_tk_widget().grid(column=0, row=4, columnspan=3)
            self.after(200, None)
        def close():
            """


           @author: Катя Агафонова
           Функция удаляет текущий график с экрана. Обратите внимание, что
           очищение экрана необходимо проводить после каждого нового вывода
           графика!

            """
            global canvas1
            if canvas1:
                canvas1.get_tk_widget().destroy()
        canvas1 = None
        bth = tk.Button(self, text='Вывод графика', font=('Raleway', 14,
                        'italic'),bg='#ffffff', fg='#121413',
                activeforeground='#a784e3', command=clck2, padx=5, pady=5)
        bth.grid(column=2, row=1)
        bth = tk.Button(self, text='Сброс графика', font=('Raleway', 14,
                        'italic'),bg='#ffffff', fg='#121413',
                activeforeground='#a784e3', command=close, padx=5, pady=5)
        bth.grid(column=2, row=2)

# Driver Code
win = tkinterApp()
