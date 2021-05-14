# https://cdn-api.co-vin.in/api/v2/admin/location/states
import requests


class StatesInfo:
    def __init__(self):
        self.url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

    def fetch_all_states(self):
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        app = requests.get(self.url, headers=headers)
        if app.status_code == 200:
            results = app.json()
            return {
                state["state_name"]: state["state_id"] for state in results["states"]
            }

    def fetch_state_id(self, state):
        state_list = self.fetch_all_states()
        return state_list.get(state)


class CityInfo:
    def __init__(self, state_id):
        self.url = (
            f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}"
        )
        print(self.url)

    def fetch_all_cities(self):
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        app = requests.get(self.url, headers=headers)
        if app.status_code == 200:
            results = app.json()
            return {
                state["district_name"]: state["district_id"]
                for state in results["districts"]
            }

    def fetch_city_id(self, city):
        city_list = self.fetch_all_cities()
        print(city_list)
        return city_list.get(city)
