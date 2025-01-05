# TODO 1: add a functioning side bar
# TODO 2: add a functioning menu bar
# TODO 3 : add the main app GUI for creating custom fields for passwords
# TODO 4: add the file handling logic to store the passwords
# TODO 5: use cryptography module to store the credentials as hashes

#import tkinter as tk
import customtkinter as ctk

# functions
def close_welcome_label():
    loading_label.destroy()

def close_welcome_screen():
    welcome_label.destroy()  # Closes the welcome screen
    main_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Show main frame
    root.after(1500, close_welcome_label)

# Basic theming
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("900x480")
root.title("Locksmith")
root.resizable(width=False, height=False)

# Configure root grid to support main_frame resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Add content to the welcome screen
welcome_label = ctk.CTkLabel(
    root, 
    text="Welcome to Locksmith!", 
    font=ctk.CTkFont("Arial", size=24, weight="bold")
)
welcome_label.grid(row=0, column=0, pady=100)  # Use grid instead of pack()

loading_label = ctk.CTkLabel(
    root, 
    text="Loading, please wait...", 
    font=ctk.CTkFont("Arial", size=16, weight="normal")
)
loading_label.grid(row=1, column=0, pady=10)  # Use grid instead of pack()

# Schedule the screen to close after 3 seconds (3000 milliseconds)
root.after(3000, close_welcome_screen)

# main app frame after welcome screen
main_frame = ctk.CTkFrame(master=root, width=900, height=400)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure((0, 1, 2), weight=1)

# menu bar
menu_bar = ctk.CTkOptionMenu(master=main_frame)
file_menu = ctk.CTkOptionMenu(master=main_frame)
action_menu = ctk.CTkOptionMenu(master=main_frame)

# subframes
subframe_left = ctk.CTkFrame(master=main_frame, corner_radius=10)
subframe_middle = ctk.CTkFrame(master=main_frame, corner_radius=10)
subframe_right = ctk.CTkFrame(master=main_frame, corner_radius=10)

# place subframes side by side
subframe_left.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
subframe_middle.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
subframe_right.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# add labels to each subframe
label1 = ctk.CTkLabel(master=subframe_left, text="Left Frame", corner_radius=10)
label1.pack(padx=10, pady=10)

label2 = ctk.CTkLabel(master=subframe_middle, text="Middle Frame", corner_radius=10)
label2.pack(padx=10, pady=10)

label3 = ctk.CTkLabel(master=subframe_right, text="Right Frame", corner_radius=10)
label3.pack(padx=10, pady=10)

root.mainloop()
# this is a comment
