import customtkinter as ctk
from passcheck.test import password_strength, is_password_in_dictionary, crack_time
from CTkMessagebox import CTkMessagebox
from PIL import Image

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Strength Checker")
        self.geometry("600x400")

        # Initialize progress color
        self.prog_col = "red"
        logo =  ctk.CTkImage(
            light_image=Image.open("passcheck/images/lock-svgrepo-com.png"),
            dark_image=Image.open("passcheck/images/lock-svgrepo-com.png"),
            size=(30, 30)
        )

        # Load image once during initialization
        self.image = ctk.CTkImage(
            light_image=Image.open("passcheck/images/Antu_dialog-warning.ico"),
            dark_image=Image.open("passcheck/images/Antu_dialog-warning.ico"),
            size=(30, 30)
        )
        self.image1 = ctk.CTkImage(
            light_image=Image.open("passcheck/images/sirena3-512.png"),
            dark_image=Image.open("passcheck/images/sirena3-512.png"),
            size=(30, 30)
        )

        def onclick():
            mypass = self.pass_entry.get()

            if not mypass:
                # Show a message box if the password field is empty
                CTkMessagebox(title="Warning", icon="warning", message="Do not leave the textbox empty")
                return

            # Check if the password is in the dictionary
            if is_password_in_dictionary(mypass):
                strength = password_strength(mypass) - 20  # Reduce strength by 20% if in dictionary
                self.result_label.configure(text="Password is in the dictionary. Strength reduced.")
                self.imagelabel.configure(image=self.image)
                self.imagelabel.image = self.image  # Keep a reference to avoid garbage collection
                self.imagelabel.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")  # Make sure it's visible
            else:
                strength = password_strength(mypass)
                self.result_label.configure(text="")
                self.imagelabel.configure(image=None)
                self.imagelabel.image = None  # Clear the image reference
                self.imagelabel.grid_forget()  # Hide the image label

            strength = max(strength, 0)  # Ensure strength is not negative

            # Update the progress bar value
            self.progress_b.set(strength / 100)  # Assuming strength is a percentage

            # Update progress color based on strength
            if strength < 50:
                self.prog_col = "red"
                self.image1label.configure(image=self.image1)
                self.image1label.image = self.image  # Keep a reference to avoid garbage collection
                self.image1label.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")

            elif 50 <= strength < 75:
                self.prog_col = "yellow"
                self.image1 = ctk.CTkImage(
                    light_image=Image.open("passcheck/images/siren-icon-1564x2048-dxic7rzw.png"),
                    dark_image=Image.open("passcheck/images/siren-icon-1564x2048-dxic7rzw.png"),
                    size=(30, 30)
                )

                self.image1label.configure(image=self.image1)
                self.image1label.image = self.image  # Keep a reference to avoid garbage collection
                self.image1label.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")
            else:
                self.prog_col = "green"
                self.image1 = ctk.CTkImage(
                    light_image=Image.open("passcheck/images/5174_green_siren.png"),
                    dark_image=Image.open("passcheck/images/5174_green_siren.png"),
                    size=(30, 30)
                )

                self.image1label.configure(image=self.image1)
                self.image1label.image = self.image  # Keep a reference to avoid garbage collection
                self.image1label.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")

            # Update the color of the progress bar
            self.update_progress_bar_color()

            # Update the strength and crack time labels
            self.strength_label.configure(text=f"Password strength: {strength}%")
            crack_estimate = crack_time(mypass)
            self.crack_time_label.configure(text=f"Estimated crack time: {crack_estimate}")

        # Create widgets
        self.pass_label = ctk.CTkLabel(self, text="Check Strength of Password")
        self.pass_label.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Enter Your Password")
        self.pass_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.submit_but = ctk.CTkButton(self, text="Check", command=onclick)
        self.submit_but.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # Initialize progress bar at 0
        self.progress_b = ctk.CTkProgressBar(self, progress_color=self.prog_col)
        self.progress_b.set(0)
        self.progress_b.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        # Initialize result labels
        self.imagelabel = ctk.CTkLabel(self, image=self.image, text="")
        self.imagelabel.grid(row=5, column=0, padx=20, pady=10, sticky="nsew")
        self.imagelabel.grid_forget()  # Hide the image label initially
        self.image1label = ctk.CTkLabel(self, image=self.image1, text="")
        self.image1label.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")
        self.image1label.grid_forget()  # Hide the image label initially

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

        self.strength_label = ctk.CTkLabel(self, text="Password strength: ")
        self.strength_label.grid(row=6, column=1, padx=20, pady=10, sticky="ew")

        self.crack_time_label = ctk.CTkLabel(self, text="Estimated crack time: ")
        self.crack_time_label.grid(row=7, column=1, padx=20, pady=10, sticky="ew")

        # Configure grid rows and columns to expand
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def update_progress_bar_color(self):
        # Update the progress bar color dynamically
        self.progress_b.configure(progress_color=self.prog_col)

if __name__ == "__main__":
    app = App()
    app.after(201, lambda: app.iconbitmap("D:\Book\PythonProjects\PassChecker\passcheck\images\lock-svgrepo-com.ico"))
    app.mainloop()

