import datetime
import pprint
import json
from service.center_info import InfomationCenter
from service.location import StatesInfo, CityInfo

# API details
host = "https://cdn-api.co-vin.in"
endpoint = "api/v2/appointment/sessions/public/calendarByDistrict"

# fetch location details
with open("data.json", "r") as json_file:
    json_data = json.load(json_file)
state_input = json_data.get("state")
city_input = json_data.get("district")
state = StatesInfo()
state_id = state.fetch_state_id(state_input)
# state_list = state.fetch_all_states()
city = CityInfo(state_id)
# city_id = city.fetch_city_id(city_input)
city_list = city.fetch_all_cities()

for city_name, city_id in city_list.items():
    print("##################################################")
    print(f"#           {city_name}                #")
    print("##################################################")
    district = city_id

    # fetch today's date
    week = 1
    for ndays in range(week):
        today_date = datetime.date.today() + datetime.timedelta(days=ndays)
        today = today_date.strftime("%d-%m-%Y")
        booking_url = f"{host}/{endpoint}?district_id={district}&date={today}"
        app = InfomationCenter(booking_url)
        print(f"========================= Day {ndays+1} ===================")
        pprint.pprint(app.fetch_available_slots())
