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
        

def popup_showinfo():
    showinfo("AirCheck Info", "Hi! This simple application allows you to check current air pollution data at desired location, which you can now input.")


def process():
    lat = lat_entry.get()
    lon = lon_entry.get()
    #my_APIkey = "YOUR API KEY"
    my_Jsondata = getJson(my_APIkey, lat, lon)
    json_data = my_Jsondata.request_data()
    my_data = my_Jsondata.json_deserialize(json_data)
    air_data = my_data
    values_label1 = Label(info_frame, text ="Concetration of CO[ug/m^3]: {}".format(air_data["list"][0]["components"]["co"])).grid(row = 0, column = 0)
    values_label2 = Label(info_frame, text ="Concetration of NO[ug/m^3]: {}".format(air_data["list"][0]["components"]["no"])).grid(row = 1, column = 0)
    values_label3 = Label(info_frame, text ="Concetration of NO2[ug/m^3]: {}".format(air_data["list"][0]["components"]["no2"])).grid(row = 2, column = 0)
    values_label4 = Label(info_frame, text ="Concetration of O3[ug/m^3]: {}".format(air_data["list"][0]["components"]["o3"])).grid(row = 3, column = 0)
    values_label5 = Label(info_frame, text ="Concetration of PM2_5[ug/m^3]: {}".format(air_data["list"][0]["components"]["pm2_5"])).grid(row = 4, column = 0)
    values_label6 = Label(info_frame, text ="Concetration of PM10[ug/m^3]: {}".format(air_data["list"][0]["components"]["pm10"])).grid(row = 5, column = 0)


if __name__ == "__main__":
    air_data = dict
    root = tk.Tk()
    root.title("AirCheck")
    root.geometry("260x250")
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
    
    showinfo_btn = tk.Button(top_frame, text="App Info", command=popup_showinfo).grid(row = 2, column = 0, pady = 5)
    submit_btn = Button(top_frame, text = "Submit", command = process).grid(row = 2, column = 1, pady = 5)
    
    info_frame = Frame(root)
    info_frame.grid(padx=5, pady=5)    
