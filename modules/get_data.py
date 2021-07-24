import requests
import json


class getJson():

    def __init__(self, API_key: str, lat: float, lon: float) -> None:
        self.API_key = API_key
        self.lat = lat
        self.lon = lon

    def request_data(self) -> str:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={self.lat}&lon={self.lon}&appid={self.API_key}")
        assert response.status_code == 200, "Couldn't fetch data!"
        return str(response.json())

    def json_deserialize(self, json_data: str) -> dict:
        json_data = json_data.replace("'",'"')
        data_dict = json.loads(json_data)
        return data_dict
