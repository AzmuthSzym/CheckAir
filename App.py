from get_data import getJson


def validate_input(input_type: str) -> input:
    while True:
        input_val = input(f"Input desired {input_type} to be checked ")
        try:
            input_val = float(input_val)
        except ValueError:
            print("Please make sure that your input is a valid number")
            continue
        else:
            break
    return input_val


def print_data(air_data: dict) -> None:
    print("Concentration of Carbon monoxide ug/m^3: {}".format(air_data["list"][0]["components"]["co"]))
    print("Concentration of PM2_5 particles ug/m^3: {}".format(air_data["list"][0]["components"]["pm2_5"]))


if __name__ == "__main__":
    print("Hi! This simple application allows you to check current air pollution data at desired location, which you can now input.")
    lat = validate_input("latitude")
    lon = validate_input("longitude")
    my_APIkey = "YOUR API KEY"
    my_Jsondata = getJson(my_APIkey, lat, lon)
    json_data = my_Jsondata.request_data()
    my_data = my_Jsondata.json_deserialize(json_data)
    print_data(my_data)
