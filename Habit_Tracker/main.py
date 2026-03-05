print(786)
import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
PIXELA_PARAMETERS = {
    "token":f"{os.environ.get('TOKEN')}",
    "username":f"{os.environ.get('PIXELA_USERNAME')}",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
PIEXLA_API = "https://pixe.la/v1/users"

response = requests.post(url= PIEXLA_API,json=PIXELA_PARAMETERS)
#print(response.text)
graph_api = f"{PIEXLA_API}/{os.environ.get('PIXELA_USERNAME')}/graphs"
graph_params = {
    "id":f"{os.environ.get('GRAPH_ID')}",
    "name":"Weight tracker",
    "unit":"kg",
    "type":"float",
    "color":"momiji"
}
HEADERS = {
    "X-USER-TOKEN":f"{os.environ.get('TOKEN')}"
}
response = requests.post(url=graph_api,json=graph_params,headers=HEADERS)
#print(response.text)
today = dt.datetime.now()

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kg or grams have you burn today?:")
}
pixel_api = f"{graph_api}/{os.environ.get('GRAPH_ID')}"
response = requests.post(url = pixel_api,json=pixel_params,headers=HEADERS)
print(response.text)

post_params = {
    "quantity":"59"
}
put_api = f"{pixel_api}/{today.strftime('%Y%m%d')}"
# response = requests.put(url = put_api,json=post_params,headers=HEADERS)
# print(response.text)
delete_params = {
    "quantity":"59"
}
#for deleting
delete_pixel_api = f"{put_api}"
# response = requests.delete(url=delete_pixel_api,json=delete_params,headers=HEADERS)
# print(response.text)
