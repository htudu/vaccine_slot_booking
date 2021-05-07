import json
import requests

class InfomationCenter(object):
    def __init__(self, url):
        self.booking_url = url

    def fetch_available_slots(self):
        '''
        1) checking all centers for availability of slots 
        2) checking for free or paid centers
        3) checking age limit
        4) Relevant Information Fields:
            a) total_slots - number of centers in the district
            b) free_slots - number of centers with free slots in the district
            c) paid_slots - number of center with paid slots in the district
            d) avialable_capacity - number of vaccine slots
            e) date - Date on which the vaccine is available
            f) vaccine_name - name of the vaccine provided in the center
            g) center_type - paid/free center
            h) center_name - Name of the center

        returning >>> dictionary with relevant informations  
        '''
        # try:
        center_information = {}
        message = "success"
        code = 200        
        headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
        vaccine_app = requests.get(self.booking_url, headers=headers)

        availability_slots = 0
        
        if vaccine_app.status_code == 200:
            results = vaccine_app.json()
            free_center = []
            paid_center = []
            list_of_centers = []
            for center in results["centers"][:5]:
                if center['fee_type'] == "Free":
                    free_center.append(center)
                else:
                    paid_center.append(center)
                for n,session in enumerate(center['sessions']):
                    available_center_info = {}
                    if int(session['available_capacity']) >= 0:
                        
                        #--- center information dictionary ---
                        available_center_info["center_name"] = center["name"]
                        available_center_info["center_type"] = center["fee_type"]
                        available_center_info[f"slot{n+1}-date"] = session["date"]
                        available_center_info[f"slot{n+1}-availablity"] = session["available_capacity"]
                        available_center_info[f"slot{n+1}-age_limit"] = session["min_age_limit"]
                        available_center_info[f"slot{n+1}-vaccine_name"] = session["vaccine"]
                        #--- 
                        list_of_centers.append(available_center_info)

                        #--- increment the slot value ---
                        availability_slots += 1


            center_information["total_slots"] = len(results['centers'])
            center_information["free_slots"] = len(free_center)
            center_information["paid_slots"] = len(paid_center)
            center_information["available"] = availability_slots
            center_information["center_info"] = list_of_centers
        else:
            print("Response failed")
    
        # except Exception as data_error:
        #     message = f"Exception due to - {data_error}"
        #     code = 500
        #     import traceback
        #     print(traceback.print_exc())
            # print(str(repr(data_error)))
        
        return {"message": message,
                "code": code,
                "data":center_information}

