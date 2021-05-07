import requests
import datetime

from service.center_info import InfomationCenter

# API details
host = "https://cdn-api.co-vin.in"
endpoint = "api/v2/appointment/sessions/public/calendarByDistrict"

# fetch location details
district = 265
# fetch today's date
today_date = datetime.date.today()
today = today_date.strftime("%d-%m-%Y")
today = "09-05-2021"

booking_url = f"{host}/{endpoint}?district_id={district}&date={today}"
print(booking_url)
import pprint

app = InfomationCenter(booking_url)
pprint.pprint(app.fetch_available_slots())

# headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
# res = requests.get(booking_url, headers=headers)
# pprint.pprint(res.request.headers)
# print(res.status_code)
# if res.status_code == 200:
#     result = res.json()
#     free_center = []
#     paid_center = []
#     for center in result["centers"]:
#         if center['fee_type'] == "Free":
#             free_center.append(center)
#         else:
#             paid_center.append(center)
#         for session in center['sessions']:
#             if int(session['available_capacity']) > 0:
#                 print("****************")
#                 print(f"{center['name']} - {center['fee_type']}")
#                 print(f"Date - {session['date']} | available capacity - {session['available_capacity']}")
#                 print(f"Vaccine - {session['vaccine']} | Age limi - +{session['min_age_limit']}")
    
#     print(f"total = {len(result['centers'])}")
#     print(f"free = {len(free_center)}")
#     print(f"Paid = {len(paid_center)}")
# else:
#     print("Response failed")