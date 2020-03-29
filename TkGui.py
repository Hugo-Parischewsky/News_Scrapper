from tkinter import *
from tkinter import scrolledtext

import webbrowser

from Scrap import *

LARGE_FONT= ("Verdana", 20)
button_font = ('Arial',18,'bold')


pag_list = ['https://www.biobiochile.cl',
            'https://www.semana.com',
            'https://ciperchile.cl',
            'https://www.elsur.cl/impresa/2020/03/03/papel/',
            'https://www.eldesconcierto.cl/'] 

# Lista  de los links que se obtuvieron en la busqueda (x.dup)
busqueda_list = []


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self) 

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


# Clase para la pagina de inicio        
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Pagnia principal", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        
        button = Button(self, text="Buscador",
                            font = button_font,
                            command=lambda: controller.show_frame(PageOne))
        button.place(x = 20, y = 20)
        button.config(height = 3, width = 12)

        button2 = Button(self, text="Info App",
                            font = button_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x = 20, y = 90)
        button2.config(height = 3, width = 12)
        
        button3 = Button(self, text="Filtrar",
                            font = button_font,
                            command=lambda: controller.show_frame(PageThree))
        button3.place(x = 160, y = 20)
        button3.config(height = 3, width = 12)
        
        button4 = Button(self, text="Salir",
                            font = button_font,
                            command=quit)
        button4.place(x = 160, y = 90)
        button4.config(height = 3, width = 12)

        
# Clase para hacer la primera pagina
## En esta pagina se encuentra el buscador
class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Buscador", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
                                ###########
                                # Botones #
                                ###########
                    
        button = Button(self, text="Buscador",
                            font = button_font,
                            command=lambda: controller.show_frame(PageOne))
        button.place(x = 20, y = 20)
        button.config(height = 3, width = 12)

        button2 = Button(self, text="Info App",
                            font = button_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x = 20, y = 90)
        button2.config(height = 3, width = 12)
        
        button3 = Button(self, text="Filtrar",
                            font = button_font,
                            command=lambda: controller.show_frame(PageThree))
        button3.place(x = 160, y = 20)
        button3.config(height = 3, width = 12)
        
        button4 = Button(self, text="Salir",
                            font = button_font,
                            command=quit)
        button4.place(x = 160, y = 90)
        button4.config(height = 3, width = 12)

        # Cuadro de scroll texto


                                #######################
                                # Cuerpo de la pagina #
                                #######################
                    
                    
        txt1 = Label(self,
                    text = 'Ingresar palabras a buscar ')
        txt1.place(x = 670, y = 50)

        # texto de ayuda para la busqueda
        texto_ayuda = [ 
                    ' ',
                    ' - Se buscaran las noticias que contengan las palabras ingresadas.',
                    ' - Puede ser ingresada mas de una palabra, deben ser separadas por un espacio.',
                    ' - Reemplazar la "ñ" por una "n" al hacer la busqueda.',
                    ' - Presionar el boton "Buscar" y esperar a que aparezcan los resultados abajo. '
                    ]

        lb2 = Listbox(self)
        x = 0
        for word in texto_ayuda:
            x += 1
            lb2.insert(x,word)
        lb2.place(x = 1050, y = 20)
        lb2.config(height = 6, width = 65, font = ('Arial',13))

 


        # texto de entrada que ira dentro del cajon
        entry1 = Entry(self,
                        width = 40)
        entry1.place(x = 590,y = 90)

        def clean_list(lista):
            lista[:] = []
            return lista

        def get_text():
            clean_list(busqueda_list)
            kwlist = []
            kw = entry1.get()

            for word in kw.split(' '):
                kwlist.append(word)
            #print(kwlist)

            x = scraper(url,kwlist)

            x.separator()


            # Cuadro de scroll texto

            text_scroll = scrolledtext.ScrolledText(self,
                                                    width = 210,
                                                    height = 30)
            text_scroll.place(x = 60 , y = 200)
            for n in range(0,len(x.dup) - 1):
                text_scroll.insert(INSERT,'\n' + '\n' + str(x.dup[n]), str('\n'))
                busqueda_list.append(x.dup[n])
            #for n in range(0,len(x.dup) -1):
            #    text_scroll.insert(INSERT, str('\n') + str(x.header[n]) + str('\n') + str(x.dup[n]), str('\n'))

            # Cuadro de texto con numero de resultados de busqueda
        
            txt2 = Label(self,
                        text = 'Resultados de Busqueda :   ' + str(len(x.dup) - 1))
            txt2.place(x = 690, y = 130)

            return


        
        # Boton para buscar ( al ser clickeado llama a la funcion del scraper)
        button1 = Button(self,
                        text = 'Buscar',
                        command = lambda: get_text() )
        button1.place(x = 970, y = 93)
        


    

# Clase para hacer la segunda pagina
## Esta pagina muestra la informacion de la app 
class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Info App", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

                                ###########
                                # Botones #
                                ###########
        button = Button(self, text="Buscador",
                            font = button_font,
                            command=lambda: controller.show_frame(PageOne))
        button.place(x = 20, y = 20)
        button.config(height = 3, width = 12)

        button2 = Button(self, text="Info App",
                            font = button_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x = 20, y = 90)
        button2.config(height = 3, width = 12)
        
        button3 = Button(self, text="Filtrar",
                            font = button_font,
                            command=lambda: controller.show_frame(PageThree))
        button3.place(x = 160, y = 20)
        button3.config(height = 3, width = 12)
        
        button4 = Button(self, text="Salir",
                            font = button_font,
                            command=quit)
        button4.place(x = 160, y = 90)
        button4.config(height = 3, width = 12)
        
                                #######################
                                # Cuerpo de la pagina #
                                #######################
                    
        
        txt3 = Label(self,
                       text = 'Paginas donde se ubsca la informacion',
                       font = LARGE_FONT)
        txt3.place(x = 30, y = 210)
        lb1 = Listbox(self)
        x = 0
        for pag in pag_list:
            x += 1
            lb1.insert(x,pag)
        lb1.place(x = 50, y = 245)
        lb1.config(height = 20, width = 40, font = ('Arial',15))
        

# Clase para hacer la tercera pagina
## Esta pagina busca dentro de los resultados principales ( Filtro )
class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Filtrar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
                                        ###########
                                        # Botones #
                                        ###########



                    
        button = Button(self, text="Buscador",
                            font = button_font,
                            command=lambda: controller.show_frame(PageOne))
        button.place(x = 20, y = 20)
        button.config(height = 3, width = 12)

        button2 = Button(self, text="Info App",
                            font = button_font,
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(x = 20, y = 90)
        button2.config(height = 3, width = 12)
        
        button3 = Button(self, text="Filtrar",
                            font = button_font,
                            command=lambda: controller.show_frame(PageThree))
        button3.place(x = 160, y = 20)
        button3.config(height = 3, width = 12)
        
        button4 = Button(self, text="Salir",
                            font = button_font,
                            command=quit)
        button4.place(x = 160, y = 90)
        button4.config(height = 3, width = 12)






        
        
                                    #######################
                                    # Cuerpo de la pagina #
                                    #######################
        
        # Caja de entrada de texto para filtro 1
        entry_filtro1 = Entry(self,
                                width = 50)
        entry_filtro1.place(x = 60, y = 200)

        # Caja de entrada de texto para filtro 2
        entry_filtro2 = Entry(self,
                                width = 50)
        entry_filtro2.place(x = 60, y = 500)
        
        def callback(event):
            webbrowser.open_new(event.widget.cget('text'))


        def get_filer(self,num):
            text_scroll = scrolledtext.ScrolledText(self,
                        width = 210,
                        height = 13)
            text_scroll.bind('<Button-1>', callback)
            #kw = entrada.get()
            #filter_num = entrada.split('-')[-1]
            #filtro = 'filtro_' + str(filter_num)

            #for link in busqueda_list:
            #    if link.find(str(kw)) != -1:
            #        filtro.append(link)

            if num == 1:
                text_scroll.place(x = 60, y = 250)  
                kw = entry_filtro1.get()
                for link in busqueda_list:
                    if link.find(str(kw)) != -1:
                        #print(link.find(str(kw)))
                        text_scroll.insert(INSERT,'\n \n' + str(link)te, str('\n'))


                

            elif num == 2:
                text_scroll.place(x = 60, y = 550)
                kw = entry_filtro2.get()
                for link in busqueda_list:
                    if link.find(str(kw)) != -1:
                        #print(link.find(str(kw)))
                        text_scroll.insert(INSERT,'\n \n' + str(link), str('\n'))


            return

        # Boton de filtro 1
        boton_filtro_1 = Button(self,
                                text = 'Filtrar',
                                command = lambda: get_filer(self,1))
        boton_filtro_1.place(x = 540, y = 203)
        # Boton de filtro 2
        boton_filtro_2 = Button(self,
                        text = 'Filtrar',
                        command = lambda: get_filer(self,2))
        boton_filtro_2.place(x = 540, y = 503)







