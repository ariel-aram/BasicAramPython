# Author: Harel Haram
# Date: 2026-02-14
# Description: Calculate the BMI through CustomTkinter

# Import the entire bible itself
import customtkinter  # type: ignore

# Prepare to witness the creation of my peak appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Parameters of the windows
rootGUI = customtkinter.CTk()
rootGUI.geometry("400x250")
rootGUI.title("BMI System")
rootGUI.resizable(False, False)

labelFont = customtkinter.CTkFont(family="Verdana", size=30, weight="bold")

# My beloved GUI Whitelabol from TEMU
labelIntro = customtkinter.CTkLabel(
    rootGUI, text="BMI Calculator", text_color="#0067DD", font=labelFont
)
labelIntro.pack(padx=10, pady=10)  # type: ignore


# Calculus Gynasius
def calc():
    try:
        rootGUI.geometry("450x250")

        height = float(labelHeight.get())
        weight = float(labelWeight.get())
        bmi = weight / (height**2)

        if bmi < 1.9:
            classification = "Mosquito"
        elif bmi >= 2 and bmi < 18.5:
            classification = "Taller"
        elif bmi >= 18.5 and bmi < 25:
            classification = "Normaller"
        elif bmi >= 25 and bmi < 30:
            classification = "Pre-Obesity"
        elif bmi >= 30 and bmi < 35:
            classification = "Obesity Level I"
        elif bmi >= 35 and bmi < 40:
            classification = "Obesity Level II"
        elif bmi >= 40:
            classification = "Obesity Level III"
        else:
            classification = "Unknown"

        labelResult.configure(  # type: ignore
            text=f"Your BMI is {bmi:.2f}, and ur classified as {classification}",
            text_color="#71B3FF",
        )
    except ValueError:
        rootGUI.geometry("600x250")

        labelResult.configure(  # type: ignore
            text="Error 003: Too bad mister, my recommendation for you is to feel the wrath of Napoleon, you punk",
            text_color="#B30000",
        )
    pass


# Note: CustomTkinter has its own calculation methods instead of the common Python strategy

# Inputting and entering
labelWeight = customtkinter.CTkEntry(
    rootGUI,
    placeholder_text="Body Weight:",
    corner_radius=30,
    width=300,
    placeholder_text_color="#BFD5FF",
)
labelHeight = customtkinter.CTkEntry(
    rootGUI,
    placeholder_text="Body Height:",
    corner_radius=30,
    width=300,
    placeholder_text_color="#BFD5FF",
)
labelWeight.pack(padx=10, pady=10)  # type: ignore
labelHeight.pack(padx=10, pady=10)  # type: ignore

# Do the button
labelButton = customtkinter.CTkButton(
    rootGUI,
    text="Confirm input",
    fg_color="#0067DD",
    hover=True,
    hover_color="#002857",
    command=calc,
)
labelButton.pack(padx=10, pady=10)  # type: ignore

labelResult = customtkinter.CTkLabel(rootGUI, text="")
labelResult.pack(padx=10, pady=10)  # type: ignore

# Rendering the silly windows
rootGUI.mainloop()  # type: ignore
