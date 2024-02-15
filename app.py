import customtkinter

from api.tweet import tweet

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.ingess = ""

        # configure window
        self.title("Twitter analysis GUI")
        self.geometry(f"{1100}x580")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Twitter analysis", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.csv_button = customtkinter.CTkButton(self.sidebar_frame, text="CSV", command=self.csv_button_event)
        self.csv_button.grid(row=1, column=0, padx=20, pady=10)
        self.api_button = customtkinter.CTkButton(self.sidebar_frame, text="API", command=self.api_button_event)
        self.api_button.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

         # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), columnspan=2, sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1) 

        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("CTkTabview"), width=50)
        self.textbox.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.process_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Process Input", state="disabled",
                                                      command=self.process_input)
        self.process_button.grid(row=1, column=0, padx=10, pady=(20, 10), sticky="ew")

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        self.input_value = None
        self.selection_value = None

        self.textbox.bind("<KeyRelease>", self.validate_textbox)

    def validate_textbox(self, event):
        text = self.textbox.get("1.0", "end").strip()
        if text:
            self.process_button.configure(state="normal")
        else:
            self.process_button.configure(state="disabled")

    def api_button_event(self):
        print('api')
        self.process_button.configure(text="API")
        self.ingess = "API"

    def csv_button_event(self):
        print('csv')
        self.process_button.configure(text="csv")
        self.ingess = "csv"

    def process_input(self):
        input_text = self.textbox.get("1.0", "end-1c") 
        print("Input Text:", input_text)

    def process_input(self):
        # Handle process button click event
        input_text = self.textbox.get("1.0", "end-1c")  
        if input_text: 
            self.user_input = input_text 
            self.process_button.configure(state="normal") 
            print(self.user_input)
            print(self.ingess)
            if self.ingess == "API":
                tweet(self.user_input)
            else:
                print("kaggle")

        else:
            print("Please enter some text") 


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
