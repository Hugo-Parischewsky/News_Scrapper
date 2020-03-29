from tkinter import *
from tkinter import scrolledtext

from Scrap import *

LARGE_FONT= ("Verdana", 20)
button_font = ('Arial',18,'bold')


pag_list = ['https://www.biobiochile.cl',
            'https://www.semana.com',
            'https://ciperchile.cl',
            'https://www.elsur.cl/impresa/2020/03/03/papel/',
            'https://www.eldesconcierto.cl/'] 




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
        txt1.place(x = 730, y = 50)
        
        # texto de entrada que ira dentro del cajon
        entry1 = Entry(self,
                        width = 40)
        entry1.place(x = 620,y = 90)

        def get_text():
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
            #for n in range(0,len(x.dup) -1):
            #    text_scroll.insert(INSERT, str('\n') + str(x.header[n]) + str('\n') + str(x.dup[n]), str('\n'))

            # Cuadro de texto con numero de resultados de busqueda
        
            txt2 = Label(self,
                        text = 'Resultados de Busqueda :   ' + str(len(x.dup) - 1))
            txt2.place(x = 710, y = 130)
            return


        
        
        # boton que aun no se como darle la funcion
        button1 = Button(self,
                        text = 'Buscar',
                        command = lambda: get_text() )
        button1.place(x = 1000, y = 93)
        


    

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
        





