import customtkinter as ctk
from components.frames.items_frames.all_items_frame import AllItemsFrame
from components.frames.items_frames.bin_items_frame import BinItemsFrame


class ItemsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configurations
        self.grid_columnconfigure(0, weight=1)

        # Show all items by default
        self.current_frame = AllItemsFrame(self, fg_color="transparent")
        self.current_frame.grid(row=0, column=0)

    def __switch_frame(self, frame: ctk.CTkFrame):
        self.current_frame.destroy()
        self.current_frame = frame(self, fg_color="transparent")
        self.current_frame.grid(row=0, column=0)

    def show_all_items(self):
        self.__switch_frame(AllItemsFrame)

    def show_bin_items(self):
        self.__switch_frame(BinItemsFrame)
