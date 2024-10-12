import os
from PIL import Image
from customtkinter import *
from API_Functions import API_GenerMovie, API_YearMovie

set_appearance_mode("Dark")  # Modos: "System", "Dark", "Light"
set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"


class App(CTk):

    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.title("Choose Movie APP")
        self.geometry(f"{1100}x{580}")

        # Configuração da Grid
        self.grid_columnconfigure(0, weight=1)  # Coluna à esquerda (Sidebar)
        self.grid_columnconfigure(1, weight=2)  # Coluna central (Área de conteúdo)
        self.grid_columnconfigure(2, weight=1)  # Coluna à direita (TabView)
        self.grid_rowconfigure(0, weight=1)

        # Caminho da imagem (logo)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "APP_Functions/Images")
        self.logo_image = CTkImage(Image.open(os.path.join(image_path, "Logo.png")), size=(100, 100))

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "APP_Functions/Images")
        self.Capa_Image = CTkImage(Image.open(os.path.join(image_path, "CapaFilmeTeste.jpg")), size=(245.33, 306.66))

        # Sidebar com logo e OptionMenus dentro de um Frame (esquerda)
        self.Sidebar_frame = CTkFrame(self, corner_radius=10)
        self.Sidebar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.Sidebar_frame_label = CTkLabel(self.Sidebar_frame, text="", image=self.logo_image, compound="top")
        self.Sidebar_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Menu de seleção de gênero
        self.MovieOptionMenu = CTkOptionMenu(self.Sidebar_frame, values=API_GenerMovie())
        self.MovieOptionMenu.grid(row=1, column=0, padx=20, pady=10)

        # Menu de seleção de ano
        self.YearOptionMenu = CTkOptionMenu(self.Sidebar_frame, values=API_YearMovie())
        self.YearOptionMenu.grid(row=2, column=0, padx=20, pady=10)

        # Frame Central com Label e botões abaixo
        self.Center_frame = CTkFrame(self, corner_radius=10)
        self.Center_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Label central (com lorem ipsum)
        self.LoremLabel = CTkLabel(self.Center_frame, text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                                            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n" * 50),
                                   wraplength=400, justify="left")
        self.LoremLabel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Botões (random e exit) abaixo do Frame central
        self.Button_frame = CTkFrame(self)
        self.Button_frame.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.Button_frame.grid_columnconfigure((0, 1), weight=1)

        self.RandomButton = CTkButton(self.Button_frame, text="Random", command=self.randomize_movie)
        self.RandomButton.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.ExitButton = CTkButton(self.Button_frame, text="Exit", command=self.quit)
        self.ExitButton.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        # TabView à direita com Frame centralizado e Label abaixo
        self.TabView_frame = CTkTabview(self)
        self.TabView_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

        # Adicionando uma aba ao TabView com o nome inicial
        self.current_tab_name = "Movie Tab"  # Nome inicial da aba
        self.TabView_Self = self.TabView_frame.add(self.current_tab_name)

        # Configurando a imagem e os detalhes do filme na aba
        self.TabView_Capa = CTkLabel(self.TabView_frame.tab(self.current_tab_name), text="", image=self.Capa_Image,
                                     compound="top")
        self.TabView_Capa.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.Inner_frame = CTkFrame(self.TabView_frame.tab(self.current_tab_name), corner_radius=10)
        self.Inner_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.DetailsLabel = CTkLabel(self.TabView_frame.tab(self.current_tab_name), text="Detalhes do Filme",
                                     font=CTkFont(size=15))
        self.DetailsLabel.grid(row=1, column=0, padx=20, pady=10, sticky="n")

        # Botão para mudar o nome da aba
        self.ChangeTabButton = CTkButton(self.Sidebar_frame, text="Alterar Nome da Aba",
                                         command=self.change_tabview_title)
        self.ChangeTabButton.grid(row=3, column=0, padx=20, pady=10)

    def randomize_movie(self):
        # Função de randomizar filme
        selected_genre = self.MovieOptionMenu.get()  # Obtém o gênero selecionado
        print(f"Filme selecionado: {selected_genre}")

    def change_tabview_title(self):
        # Atualiza o nome da aba no TabView com o gênero selecionado
        selected_genre = self.MovieOptionMenu.get()  # Obtém o gênero selecionado

        # Remover a aba antiga
        self.TabView_frame.delete(self.current_tab_name)

        # Criar nova aba com o novo nome
        self.current_tab_name = selected_genre
        self.TabView_Self = self.TabView_frame.add(self.current_tab_name)

        # Recriar o conteúdo da aba
        self.TabView_Capa = CTkLabel(self.TabView_frame.tab(self.current_tab_name), text="", image=self.Capa_Image,
                                     compound="top")
        self.TabView_Capa.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.Inner_frame = CTkFrame(self.TabView_frame.tab(self.current_tab_name), corner_radius=10)
        self.Inner_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.DetailsLabel = CTkLabel(self.TabView_frame.tab(self.current_tab_name), text="Detalhes do Filme",
                                     font=CTkFont(size=15))
        self.DetailsLabel.grid(row=1, column=0, padx=20, pady=10, sticky="n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
