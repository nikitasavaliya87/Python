import requests
import datetime

pixela_endpoint="https://pixe.la/v1/users"

USERNAME="tiku"
GRAPH_ID="yoga-graph"
TOKEN="bcdgwioagdujw"
pixel_param={
    "token":"bcdgwioagduj",
    "username":"tiku",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint, json=pixel_param)
# print(response.text)

#pixel_graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param={
    "id": GRAPH_ID,
    "name":"Yoga Graph",
    "unit":"Min",
    "type":"float", 
    "color":"sora",
}

header={
    "X-USER-TOKEN":TOKEN,
}
# response=requests.post(url=pixel_graph_endpoint,json=graph_param,headers=header)
# print(response.text)

pixel_graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
x=datetime.datetime.today()
param={
    "date":x.strftime("%Y%m%d"),
    "quantity":"70.30",
}
response=requests.post(url=pixel_graph_endpoint,json=param,headers=header)
print(response.text)
