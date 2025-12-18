import customtkinter as ctk
from app.controllers.app_controller import AppController

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = AppController()
        self.title("Weather App")
        self.geometry("400x350")
        self.resizable(False, False)

        self.title_label = ctk.CTkLabel(
            self,
            text="Weather App",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=20)

        self.city_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter city name",
            width=250
        )
        self.city_entry.pack(pady=10)

        self.get_weather_btn = ctk.CTkButton(
            self,
            text="Get Weather",
            command=self.get_weather
        )
        self.get_weather_btn.pack(pady=10)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=14)
        )
        self.result_label.pack(pady=20)
        self.credit_label = ctk.CTkLabel(
            self,
            text="Developed by Mahbub Alam",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="gray"
        )
        self.credit_label.pack(side="bottom", pady=8)


    def get_weather(self):
        city = self.city_entry.get().strip()

        try:
            data = self.controller.fetch_weather(city)
            self.result_label.configure(
                text=(
                    f"City: {data['city']}\n"
                    f"Temperature: {data['temperature']} °C\n"
                    f"Condition: {data['condition']}"
                )
            )
        except Exception as e:
            self.result_label.configure(text=f"⚠️ {e}")
