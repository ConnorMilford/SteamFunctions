import tkinter as tk
import customtkinter as ctk
import SteamFunctions
import tkinter.messagebox


# https://developer.valvesoftware.com/wiki/Steam_Web_API

# https://www.youtube.com/watch?v=02_Z8OC7Dlk


class Window(ctk.CTk):
    def __init__(self):
        super(Window, self).__init__()

        # -- Theme settings --
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # -- Properties --
        self.title('Steam Functions')
        self.geometry('600x600')
        self.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.iconbitmap('lqSteam.ico')
        self.resizable(False, False)

        # -- Create frames --
        self.leftBar = ctk.CTkFrame(self, width=160)
        self.leftBar.grid(row=0, column=0, sticky='nswe', )

        self.mainFrame = ctk.CTkFrame(self, width=410, height=600)
        self.mainFrame.grid(row=0, column=1, sticky='nswe', padx=20)
        self.mainFrame.grid_propagate(0)

        # -- Configure rows and cols for left frame --
        self.leftBar.grid_rowconfigure(0, minsize=10)
        self.leftBar.grid_rowconfigure(5, weight=1)
        self.leftBar.grid_rowconfigure(8, minsize=20)
        self.leftBar.grid_rowconfigure(11, minsize=10)

        # -- Right frame --
        self.mainFrame.rowconfigure((0, 1, 2, 3), weight=1)
        self.mainFrame.rowconfigure(7, weight=10)
        self.mainFrame.columnconfigure((0, 1), weight=1)
        self.mainFrame.columnconfigure(2, weight=0)

        # -- Widgets for compare games --

        # -- Labels --
        self.compareGamesLabel = ctk.CTkLabel(master=self.mainFrame, text='Compare Games:')
        self.compareGamesLabel.grid(row=0, column=1, sticky='sw')
        
        self.user1IDLabel = ctk.CTkLabel(master=self.mainFrame, text='Enter the first steam ID') # Label for id 1 entry
        self.user1IDLabel.grid(row=1, column=1, sticky="nw")
        self.user1IDEntry = ctk.CTkEntry(master=self.mainFrame) # entry box for steam id 1
        self.user1IDEntry.grid(row=1, column=1, sticky="w", pady=10)

        self.user2IDLabel = ctk.CTkLabel(master=self.mainFrame, text='Enter the second steam ID') # label for id 2 entry
        self.user2IDLabel.grid(row=2, column=1, sticky="nw")
        self.user2IDEntry = ctk.CTkEntry(master=self.mainFrame) # entry box for steam id 2
        self.user2IDEntry.grid(row=2, column=1, sticky="sw")

        # -- Buttons --
        self.IdButton = ctk.CTkButton(master=self.mainFrame, text='Compare Games', command=self.compareGamesSubmit)  # button for game comparison
        self.IdButton.grid(row=3, column=1, sticky="w")

        # -- Widgets for compare friends --

        self.compareFriendsLabel = ctk.CTkLabel(master=self.mainFrame, text='Compare friends:')
        self.compareFriendsLabel.grid(row=4, column=1, sticky='w')

        self.compareFriendsButton = ctk.CTkButton(master=self.mainFrame, text='Compare Friends', command=self.compareFriendsSubmit)
        self.compareFriendsButton.grid(row=4, column=1, sticky='sw')

    def compareGamesSubmit(self):
        user1ID = self.user1IDEntry.get()
        user2ID = self.user2IDEntry.get()
        games = SteamFunctions.compareGames(user1ID, user2ID)
        tk.messagebox.showinfo(title='Compare Games', message=games)

    def compareFriendsSubmit(self):
        user1ID = self.user1IDEntry.get()
        user2ID = self.user2IDEntry.get()
        friends = SteamFunctions.compareFriends(user1ID, user2ID)
        tk.messagebox.showinfo(title='Compare Friends', message=friends)


    def onClosing(self):
        self.destroy()

    def run(self):
        self.mainloop()
        self.submit()
