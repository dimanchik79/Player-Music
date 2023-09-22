from customtkinter import *
from os import path
from models import PlayList
from classes import MainClass


def main():
    color = ["cornsilk4", "black"]
    root = CTk()
    root.title("MUSIC PLAYER")
    root.geometry("450x500")
    root.resizable(False, False)
    root.configure(fg_color=color)
    
    set_default_color_theme("green")

    frame_main = CTkFrame(root, height=100, width=440, border_width=1, fg_color=color[1], border_color="white")
    frame_main.place_configure(x=5, y=5)

    frame_progress = CTkFrame(root, height=35, width=250, border_width=1, border_color="white", fg_color=color[1])
    frame_progress.place_configure(x=5, y=110)

    frame_volume = CTkFrame(root, height=35, width=103, border_width=1, border_color="white", fg_color=color[1])
    frame_volume.place_configure(x=342, y=110)
    frame_volume.place()
    lbl = CTkLabel(frame_volume, text="volume", font=("Calibri", 9), height=8, fg_color="white", width=93, text_color="black")
    lbl.place_configure(x=5, y=4)

    frame_list = CTkFrame(root, height=300, width=440, border_width=1, border_color="black", fg_color=color[1])
    frame_list.place_configure(x=5, y=150)

    all_widget = MainClass(root=[root, frame_progress, frame_volume, frame_list])

    root.mainloop()
    

if __name__ == "__main__":
    if not path.exists('database/bot_base.db'):
        PlayList.create_table()
    main()
