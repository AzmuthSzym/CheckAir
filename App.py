import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from modules.get_data import getJson


def validate_input(input_val) -> bool:
    try:
        input_val = float(input_val)
    except ValueError:
        return False
    return True


def popup_showinfo() -> None:
    showinfo("AirCheck Info", "Hi! This simple application allows you to check current air pollution data at desired location, which you can now input.")


def process() -> None:
    lat = lat_entry.get()
    lon = lon_entry.get()
    #my_APIkey = "YOUR API KEY"
    my_APIkey = "07f9a8a2e678d62d713b90607cc1cfc3"
    my_Jsondata = getJson(my_APIkey, lat, lon)
    json_data = my_Jsondata.request_data()
    my_data = my_Jsondata.json_deserialize(json_data)
    air_data = my_data
    ctr = 0
    for element in air_data["list"][0]["components"]:
        values_label = Label(info_frame, text="Concetration of {}[ug/m^3]: {}".format(element.upper(), air_data["list"][0]["components"][element]))
        values_label.grid(row=ctr, column=0, sticky=W)
        ctr = ctr + 1


if __name__ == "__main__":
    air_data = dict
    
    root = tk.Tk()
    root.title("AirCheck")
    root.geometry("260x280")
    root.grid_rowconfigure(2, weight = 1)
    root.grid_columnconfigure(2, weight=1)
    reg = root.register(validate_input)
    
    top_frame = Frame(root)
    top_frame.grid(padx=5, pady=5)
    
    lat_label = Label(top_frame, text = "Insert latitude here: ").grid(row = 0)
    lat_entry = Entry(top_frame, width=20, validate="key", validatecommand=(reg, '%P'))
    lat_entry.grid(row = 0, column = 1)
    
    lon_label = Label(top_frame, text = "Insert longitude here: ").grid(row = 1)
    lon_entry = Entry(top_frame, width=20, validate="key", validatecommand=(reg, '%P'))
    lon_entry.grid(row=1, column=1)
    
    showinfo_btn = tk.Button(top_frame, text="App Info", command=popup_showinfo).grid(row = 2, column = 0, pady = 5)
    submit_btn = Button(top_frame, text = "Submit", command = process).grid(row = 2, column = 1, pady = 5)
    
    info_frame = Frame(root)
    info_frame.grid(padx=5, pady=5)    
