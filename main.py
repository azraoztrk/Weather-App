from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image

window = Tk()
window.title("Is It Raining?")
window.minsize(600, 600)
window.config(padx=20, pady=20, bg="white")


my_pic = Image.open("sun.jpg")
resized = my_pic.resize((200,200))
new_pic=ImageTk.PhotoImage(resized)
my_label=Label(window, image=new_pic)
my_label.pack(pady=20)

label = Label(text="City: ",bg="white", fg="dark blue",font=("Arial", 30, "bold"))
label.place(x=150, y=100)
label.pack()

entry = Entry(width=30)
entry.pack(pady=15)

weather_label = Label(text="",font=("Arial", 15, "bold"))
weather_label.pack()


def fetch_weather():
    city = entry.get()
    city = city.replace("İ", "I").replace("ı", "i")
    city = city + ",TR"
    api_key = "ddce34d4828df7666d23ab2eca27c23d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Temperature: {temperature:.1f} °C\nWeather: {weather}")
        else:
            messagebox.showerror("Error", "City not found or API Error")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


button = Button(text="Fetch Weather", bg="white",fg="dark blue",font=("Arial", 20, "bold"),command=fetch_weather)
button.pack(pady=20)

window.mainloop()