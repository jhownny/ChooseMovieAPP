# functions of interaction of the user:
# - need an option menu for choose the gener of the movie;
# - need an input dialog for choose de year of the movie;
# - need a button for exit and random functions.

# functions of processing information of the API:
# - search the movie of the user choose with the year and gener selected;
# - present the name and exactly year information of the random movie of system choose;

import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

a = "chuleta"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=550)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="ns")
        self.tabview.add("ChooseMovie")
        self.tabview.tab("ChooseMovie").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("ChooseMovie"), dynamic_resizing=False,
                                                        values=["Aleatorio", "Aventura", "Terror", "Ação", "Suspense"])
        self.optionmenu_1.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.label = customtkinter.CTkLabel(self.tabview.tab("ChooseMovie"), text="...", fg_color="transparent")
        self.label.grid(row=2, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")

        self.entry = customtkinter.CTkEntry(self.tabview.tab("ChooseMovie"), placeholder_text="Digite o Ano do Filme")
        self.entry.grid(row=1, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")

        self.RandomButton = customtkinter.CTkButton(self.tabview.tab("ChooseMovie"), text="Aleatorizar", fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"), command=self.change_label_information)
        self.RandomButton.grid(row=3, column=0, padx=(20, 20), pady=(150, 20), sticky="sw")

        self.ExitButton = customtkinter.CTkButton(master=self.tabview.tab("ChooseMovie"), text="Exit", fg_color="transparent", border_width=2,
                                                     text_color=("gray10", "#DCE4EE"))
        self.ExitButton.grid(row=3, column=2, padx=(20, 20), pady=(150, 20), sticky="se")

        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("ChooseMovie"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

    def change_label_information(self):
        label = customtkinter.CTkLabel(self.tabview.tab("ChooseMovie"), text=(f"{a}"), fg_color="transparent")
        label.grid(row=2, column=1, padx=(5, 0), pady=(20, 10), sticky="ns")


if __name__ == "__main__":
    app = App()
    app.mainloop()