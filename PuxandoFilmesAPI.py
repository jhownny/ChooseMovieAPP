# functions of interaction of the user:
# - need an option menu for choose the gener of the movie;
# - need an input dialog for choose de year of the movie;
# - need a button for exit and random functions.

# functions of processing information of the API:
# - search the movie of the user choose with the year and gener selected;
# - present the name and exactly year information of the random movie of system choose;

import PuxandoFilmesAPI
from API_Functions import *
from customtkinter import *
from API_Functions.SearchingMovie import *

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
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

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # configure "ChooseMovie" tab
        self.tabview = CTkTabview(self, width=550)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="ns")
        self.tabview.add("ChooseMovie")
        self.tabview.tab("ChooseMovie").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        # configure movie genre option menu
        self.optionmenu = CTkOptionMenu(self.tabview.tab("ChooseMovie"), dynamic_resizing=False, values=API_Movie())
        self.optionmenu.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.label = CTkLabel(self.tabview.tab("ChooseMovie"), text="...", fg_color="transparent")
        self.label.grid(row=2, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")

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

    def change_label_information(self):
        self.label.configure(text="...")  # Clear the label first
        genre = self.optionmenu.get()
        self.label.configure(text=f"Você selecionou: {genre}")

    def open_input_dialog_event(self):
        dialog = CTkInputDialog(text="Escolha o ano do filme:", title="Ano do Filme")
        self.year = dialog.get_input()
        self.label.configure(text=f"Ano selecionado: {self.year}")

    def validaEntradas(self):
        self.vcmd = (self.register(self.validade_entry), '%p')

    def entrythings(self):
        valuething = int(self.entry.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
