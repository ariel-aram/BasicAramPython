# Author: Jeo Boden
# Dementia Machine Level 6
# Projektus: The Tkinter GUI

# Import the entire bible itself
import customtkinter  # type: ignore

# Prepare to witness the creation of my peak appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Parameters of the windows
rootGUI = customtkinter.CTk()
rootGUI.geometry("600x300")
rootGUI.title("Graphic Interface for Educational Purposes")
rootGUI.resizable(False, False)

# My beloved GUI Whitelabol from TEMU
labelIntro = customtkinter.CTkLabel(
    rootGUI, text="Graphic Interface", text_color="green"
)
labelIntro.pack(padx=10, pady=10)  # type: ignore


# Calculus Terrainus
def calc():
    try:
        result = int(labelWidth.get()) * int(labelLength.get())
        if result >= 50:
            labelResult = customtkinter.CTkLabel(
                rootGUI,
                text=f"I've calculated!1!1!1! The result is {result}",
                text_color="green",
            )
            labelResult.pack(padx=10, pady=10)  # type: ignore
        else:
            labelResult = customtkinter.CTkLabel(
                rootGUI,
                text=f"The result is {result}, OMG UR TERRAIN IS SMALL WTF",
                text_color="yellow",
            )
            labelResult.pack(padx=10, pady=10)  # type: ignore
        print("Jervis, find out who asked ❗")
    except ValueError:
        labelResult = customtkinter.CTkLabel(
            rootGUI,
            text="Error 003: Too bad mister, you need to suffer, how dare u not input the numbers",
            text_color="red",
        )
        labelResult.pack(padx=10, pady=10)  # type: ignore


# Note: CustomTkinter has its own calculation methods instead of the common Python strategy

# Inputting and entering
labelWidth = customtkinter.CTkEntry(
    rootGUI,
    placeholder_text="Terrain Width:",
    corner_radius=30,
    width=300,
)
labelLength = customtkinter.CTkEntry(
    rootGUI,
    placeholder_text="Terrain Length:",
    corner_radius=30,
    width=300,
)
labelWidth.pack(padx=10, pady=10)  # type: ignore
labelLength.pack(padx=10, pady=10)  # type: ignore

# Do the button
labelButton = customtkinter.CTkButton(
    rootGUI,
    text="Confirm input",
    fg_color="green",
    hover=True,
    hover_color="#105000",
    command=calc,
)
labelButton.pack(padx=10, pady=10)  # type: ignore

# Rendering the silly windows
rootGUI.mainloop()  # type: ignore
