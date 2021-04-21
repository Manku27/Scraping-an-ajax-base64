import json
import pandas
import requests
import base64

collegedata = []
count = 0
while True:
    datadict = {"url": "management/human-resources-management-colleges", "stream": "13", "sub_stream_id": "607",
                "page": count}
    data = base64.urlsafe_b64encode(json.dumps(datadict).encode()).decode()
    params = {
        "data": data
    }
    response = requests.get('https://collegedunia.com/web-api/listing', params=params).json()
    if response["hasNext"]:
        for i in response["colleges"]:
            d = {}
            d["Name"] = i["college_name"]
            d["Rating"] = i["rating"]
            d["Location"] = i["college_city"] + ", " + i["state"]
            collegedata.append(d)
            # print(d)
    else:
        break
    count += 1

df = pandas.DataFrame(collegedata)
df.to_excel("Complete.xlsx", index=False)