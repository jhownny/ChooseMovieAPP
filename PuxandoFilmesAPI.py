# functions of interaction of the user:
# - need an option menu for choose the gener of the movie;
# - need an input dialog for choose de year of the movie;
# - need a button for exit and random functions.

# functions of processing information of the API:
# - search the movie of the user choose with the year and gener selected;
# - present the name and exactly year information of the random movie of system choose;

import PuxandoFilmesAPI
from PIL import Image
from API_Functions import *
from customtkinter import *
from API_Functions.SearchingMovie import *

set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Validadores:
    def validade_entry(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100

class App(CTk, Validadores):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Choose Movie APP")
        self.geometry(f"{1100}x{580}")
        self.validaEntradas()

        # Configure Grid Layout (5x5)
        '''
        #Column Configuration: Position 0 - width 0 / Position 1 - width 1 / Position 2 - width 0
        self.grid_columnconfigure((0,1,2,3,4), weight=0)
        #Row Configuration: Position 0, 1 and 2 - width 1
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        '''

        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure((1,2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Image Configuration
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "APP_Functions/Images")
        self.logo_image = CTkImage(Image.open(os.path.join(image_path, "Logo.png")),
                                                 size=(30, 30))

        # Configure Left Side Bar
        self.Sidebar_frame = CTkFrame(self, corner_radius=0)
        self.Sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="NSEW")
        self.Sidebar_frame.grid_rowconfigure(4, weight=1)

        self.Sidebar_frame_label = CTkLabel(self.Sidebar_frame, text="  ChooseMovie",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=CTkFont(size=15, weight="bold"))
        self.Sidebar_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Gener of Movies Dropdown Configurations
        self.MovieOptionMenu = CTkOptionMenu(self, dynamic_resizing=False, values=API_GenerMovie())
        self.MovieOptionMenu.grid(row=1, column=0, padx=20, pady=(20, 10))

        # Year Dropdown Configuration
        self.YearOptionMenu = CTkOptionMenu(self, dynamic_resizing=True, values=API_YearMovie())
        self.YearOptionMenu.grid(row=2, column=0, padx=20, pady=(20, 10))

        # Random Button Configuration
        self.RandomButton = CTkButton(self, text="Randomize", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.RandomButton.grid(row=4, column=1, padx=(20, 20), pady=(20,20), sticky="NSEW")

        # Exit Button Configuration
        self.ExitButton = CTkButton(master=self, text="Exit", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.destroy)
        self.ExitButton.grid(row=4, column=2, padx=(20, 20), pady=(20, 20), sticky="NSEW")

        # configure "ChooseMovie" tab
        self.MovieCoverFrame = CTkTabview(self, width=650)
        self.MovieCoverFrame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.MovieCoverFrame.add("ChooseMovie")
        self.MovieCoverFrame.tab("ChooseMovie").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.TitleLabel = CTkLabel(self.MovieCoverFrame.tab("ChooseMovie"),text="Title", compound="bottom", font=CTkFont(size=15, weight="bold"))
        self.TitleLabel.grid(row=1, column=1, padx=20, pady=20)

        '''
        self.Sidebar_logo = CTkImage(light_image=Image.open("APP_Functions/Images/Logo.png"), dark_image=Image.open("APP_Functions/Images/Logo.png") , size=(100, 100))

        # Use 'self' no lugar de 'app'
        self.Image_label = CTkLabel(self, image=self.Sidebar_logo, text="")  # display image with a CTkLabel

        
        # configure "ChooseMovie" tab
        self.tabview = CTkTabview(self, width=650)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="ns")
        self.tabview.add("ChooseMovie")
        self.tabview.tab("ChooseMovie").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        # configure movie genre option menu
        self.optionmenu = CTkOptionMenu(self.tabview.tab("ChooseMovie"), dynamic_resizing=False, values=API_Movie())
        self.optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.MovieLabel = CTkLabel(self.tabview.tab("ChooseMovie"), text="...", fg_color="transparent")
        self.MovieLabel.grid(row=2, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")

        self.YearLabel = CTkLabel(self.tabview.tab("ChooseMovie"), text="Ano", fg_color="transparent")
        self.YearLabel.grid(row=3, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")

        self.RandomButton = CTkButton(self.tabview.tab("ChooseMovie"), text="Aleatorizar", fg_color="transparent", border_width=2,
                                      text_color=("gray10", "#DCE4EE"), command=self.change_label_information)
        self.RandomButton.grid(row=3, column=0, padx=(20, 20), pady=(150, 20), sticky="sw")

        self.ExitButton = CTkButton(master=self.tabview.tab("ChooseMovie"), text="Sair", fg_color="transparent", border_width=2,
                                    text_color=("gray10", "#DCE4EE"), command=self.destroy)
        self.ExitButton.grid(row=3, column=2, padx=(20, 20), pady=(150, 20), sticky="se")

        self.year_button = CTkButton(self.tabview.tab("ChooseMovie"), text="Selecionar Ano", fg_color="transparent", border_width=2,
                                     text_color=("gray10", "#DCE4EE"), command=self.open_input_dialog_event)
        self.year_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.year = None

        # create radiobutton frame
        self.radiobutton_frame = CTkFrame(self.tabview.tab("ChooseMovie"), border_color = "green", border_width = 3)
        self.radiobutton_frame.grid(row=2, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = IntVar(value=0)
        self.label_radio_group = CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        
    def change_label_information(self):
        self.MovieLabel.configure(text="...")  # Clear the label first
        genre = self.optionmenu.get()
        self.MovieLabel.configure(text=f"Você selecionou: {genre}")

    def open_input_dialog_event(self):
        dialog = CTkInputDialog(text="Escolha o ano do filme:", title="Ano do Filme")
        self.year = dialog.get_input()
        self.YearLabel.configure(text=f"Ano selecionado: {self.year}")
    '''
    def validaEntradas(self):
        self.vcmd = (self.register(self.validade_entry), '%p')

    def entrythings(self):
        valuething = int(self.entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
