import requests
import boxsdk
from boxsdk import DevelopmentClient
import xlrd
client = DevelopmentClient()
user = client.user().get()
from boxsdk import OAuth2, Client
import pickle
import os
import json
import base64
#dYWuBYWplZ1kPZCxDGkR6yWzEoaEt5dT

#items_iter = client.folder(folder_id='31436627801').get_items(limit=100, offset=0, fields='id', 'name' , 'type')
ABSOLUTE_PATH = os.getcwd()
os.mkdir(ABSOLUTE_PATH+'\\Resultados')
items = client.search().query(query='"-ARC97-"', file_extensions=['pdf'], content_types='name', ancestor_folder_ids=31436627801,type='file')
for item in items:
    box_file = client.file(file_id=item.id).get()
    output_file = open(ABSOLUTE_PATH+'\\Resultados\\'+ box_file.name, 'wb')
    box_file.download_to(output_file)
