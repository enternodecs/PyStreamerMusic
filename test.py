"""
This file provides test functions for use during development and may be omitted from any build safely.
"""

from tkinter import *
from tkinter.tix import *
from tkinter.ttk import *
from PIL import Image, ImageTk


class GUI(Frame):
    def __init__(self, master: Tk=None):
        super().__init__(master)
        self.master = master
        self.notebook = Notebook(master)
        self.pack(fill=BOTH)

        self.menu = Menu(self.master)

        self.filemenu = self.menu_file()
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.player_frame = self.tab_player()
        self.notebook.add(self.player_frame, text="Player")
        self.playlist_frame = self.tab_playlists()
        self.notebook.add(self.playlist_frame, text="Playlists")
        self.settings_frame = self.tab_sources()
        self.notebook.add(self.settings_frame, text="Sources")
        self.notebook.pack(fill=BOTH, expand=True)

        self.master.config(menu=self.menu)
        self.master.minsize(450, 450)

    def tab_sources(self) -> Frame:
        settings_window = Frame(self.notebook)
        sources_frame = Frame(settings_window)
        sources_options = Frame(sources_frame)
        add = Button(master=sources_options, text="✓", width=2)
        add.grid(column=0, row=0)
        remove = Button(master=sources_options, text="✕", width=2)
        remove.grid(column=0, row=1)
        sources_options.pack(side=RIGHT)


        scroll_sources = Scrollbar(sources_frame)
        scroll_sources.pack(side=RIGHT, fill=Y)
        sources = Listbox(sources_frame, yscrollcommand=scroll_sources.set)
        # Debug
        for i in range(50):
            sources.insert(END, "Source " + str(i))
        sources.pack(side=LEFT, fill=BOTH, expand=True)
        scroll_sources.config(command=sources.yview)
        sources_frame.pack(fill=BOTH, expand=True, side=LEFT)


        return settings_window

    def tab_player(self) -> Frame:
        player_window = Frame(self.notebook)
        volume_frame = Frame(player_window)
        volume_label = Label(master=volume_frame, text="♫")
        volume_label.pack()
        volume_slider = Scale(master=volume_frame, from_=100, to=0, orient=VERTICAL)
        volume_slider.set(100)
        volume_slider.pack(fill=Y, expand=True)
        volume_slider.update()
        volume_frame.pack(side=RIGHT, fill=Y)

        albumimg = Image.open("Untitled.png")
        albumimg = albumimg.resize((400, 400), Image.ANTIALIAS)
        albumtk = ImageTk.PhotoImage(albumimg)
        albumart = Label(player_window, image=albumtk)
        albumart.image = albumtk
        albumart.pack(fill=BOTH, expand=True)

        buttons = Frame(player_window)
        previous = Button(buttons, text="↩", width=2)
        previous.grid(row=0, column=0)
        pause = Button(buttons, text="►", width=2)
        pause.grid(row=0, column=1)
        stop = Button(buttons, text="◼", width=2)
        stop.grid(row=0, column=2)
        next = Button(buttons, text="↪", width=2)
        next.grid(row=0, column=3)
        buttons.pack()
        return player_window

    def tab_playlists(self) -> Frame:
        playlist_window = Frame(self.notebook)
        playlist_window.columnconfigure(0, weight=1)
        playlist_window.rowconfigure(1, weight=1)

        playlists = Combobox(playlist_window, values=["Playlist {}".format(i) for i in range(20)], state="readonly")
        playlists.grid(column=0, row=0, sticky="EW")

        songs_frame = Frame(playlist_window)
        scroll_songs = Scrollbar(songs_frame)
        scroll_songs.pack(side=RIGHT, fill=Y)
        songs = Listbox(songs_frame, yscrollcommand=scroll_songs.set)
        # Debug
        for i in range(50):
            songs.insert(END, "Song " + str(i))
        songs.pack(side=LEFT, fill=BOTH, expand=True)
        scroll_songs.config(command=songs.yview)
        songs_frame.grid(column=0, row=1, sticky="NESW")

        song_options = Frame(playlist_window)
        up = Button(master=song_options, text="↑", width=2)
        up.grid(column=0, row=0)
        down = Button(master=song_options, text="↓", width=2)
        down.grid(column=0, row=1)
        add = Button(master=song_options, text="✓", width=2)
        add.grid(column=0, row=2)
        remove = Button(master=song_options, text="✕", width=2)
        remove.grid(column=0, row=3)
        song_options.grid(column=1, row=1)

        return playlist_window

    def menu_file(self) -> Menu:
        menu = Menu(self.menu, tearoff=0)
        menu.add_command(label="Create Playlist", command=None)
        return menu


if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    window.mainloop()
