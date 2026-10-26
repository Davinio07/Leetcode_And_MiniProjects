import requests
import os
import json
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
class ISSDataPipeline:
    def get_live_location(self):
        url = "http://api.open-notify.org/iss-now.json"
        
        Api_Getter = requests.get(url)
        Api_Getter_Dictionairy: dict = Api_Getter.json()
        
        
        return Api_Getter_Dictionairy
    
    def transform_data(self, raw_data):

        Clean_Data = {}
        Clean_Data_Lon = float(raw_data['iss_position']["longitude"])
        Clean_Data_Lat = float(raw_data['iss_position']['latitude'])
        Clean_Data_timestamp = raw_data['timestamp']
        Clean_Data["Lon"] = Clean_Data_Lon
        Clean_Data["Lat"] = Clean_Data_Lat
        Clean_Data["TimeStamp"] = Clean_Data_timestamp
        return Clean_Data
        

    def load_data(self, clean_data):
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        Blob_Service_Client = BlobServiceClient.from_connection_string(connection_string)
        
        unique_file_name = f"iss_data_{clean_data['TimeStamp']}.json"
        turn_json = json.dumps(clean_data)
        
        Container_Name: str = "storagecontainerdavi"
        Container_Client = Blob_Service_Client.get_container_client(Container_Name)
        
        Container_Client.upload_blob(name=unique_file_name, data=turn_json)
        
        
        blobs = Container_Client.list_blobs()
        for blob in blobs:
            print(blob.name)
        
    def run_pipeline(self):
        raw_data = self.get_live_location()
        clean_data = self.transform_data(raw_data)
        self.load_data(clean_data)
        
pipeline = ISSDataPipeline()
pipeline.run_pipeline()