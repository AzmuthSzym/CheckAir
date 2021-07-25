from modules.get_data import getJson
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo


def validate_input(input_val) -> bool:
    try:
        input_val = float(input_val)
        print(input_val)
    except ValueError:
        print(input_val)
        return False
    print(input_val)
    return True
        

def print_data(air_data: dict) -> None:
    print("Concentration of Carbon monoxide ug/m^3: {}".format(air_data["list"][0]["components"]["co"]))
    print("Concentration of PM2_5 particles ug/m^3: {}".format(air_data["list"][0]["components"]["pm2_5"]))


def popup_showinfo():
    showinfo("AirCheck Info", "Hi! This simple application allows you to check current air pollution data at desired location, which you can now input.")


def retrieve():
    lat = lat_entry.get()


if __name__ == "__main__":
    lat = 0
    lon = 0    
    root = tk.Tk()
    root.title("AirCheck")
    root.geometry("500x500")
    root.grid_rowconfigure(2, weight = 1)
    root.grid_columnconfigure(2, weight=1)
    reg = root.register(validate_input)
    top_frame = Frame(root)
    top_frame.grid(padx=5, pady=5)
    lat_label = Label(top_frame, text = "Insert latitude here: ").grid(row = 0)
    lat_entry = Entry(top_frame, width = 20, validate = "key", validatecommand = (reg, '%P'))
    lat_entry.grid(row = 0, column = 1)
    lon_label = Label(top_frame, text = "Insert longitude here: ").grid(row = 1)
    lon_entry = Entry(top_frame, width = 20, validate = "key", validatecommand = (reg, '%P'))
    lon_entry.grid(row = 1, column = 1)
    submit_btn = Button(top_frame, text = "Submit", command = retrieve).grid(row = 2, column = 1, pady = 5)
    #popup_showinfo()
    #my_APIkey = "YOUR API KEY"
    #my_Jsondata = getJson(my_APIkey, lat, lon)
    #json_data = my_Jsondata.request_data()
    #my_data = my_Jsondata.json_deserialize(json_data)
    #print_data(my_data)
