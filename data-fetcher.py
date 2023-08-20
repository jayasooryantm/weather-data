import requests as rq
import datetime as dt
import shutil
import json

def fetch_api_data(today:str):

    data_url = f"http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3772?res=hourly&date={today}Z&key=12a3f254-6c4a-4f6d-a464-a7a2290a7226"
    response = rq.get(data_url)
    return response.json()

def zip_json_files():
    filepath:str = 'data'
    output_filepath:str = 'data_bundle'
    shutil.make_archive(output_filepath, 'zip', filepath)


if __name__ == "__main__":
    today = dt.datetime.now().strftime("%Y-%m-%d")
    json_data = fetch_api_data(today)
    with open(f"data/api_data_{today}.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    zip_json_files()
