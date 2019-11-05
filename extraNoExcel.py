import requests
import boxsdk
from boxsdk import DevelopmentClient
import xlrd
from boxsdk import OAuth2, Client
import pickle
import os
import json
client = DevelopmentClient()
user = client.user().get()
#mapwYH46MYdvRR47j3YmtxhN1V7tdbTA

#entrada = sys.argv[1:]
#workbook = xldr.open_workbook(entrada[0])
#Folha1 = workbook.sheet_by_index(0)
ABSOLUTE_PATH = os.getcwd()
os.mkdir(ABSOLUTE_PATH+'\\Resultados')
#nomeArq= Folha1.cell_value(i,0)
items = client.search().query(query='"-ARC97-"', file_extensions=['pdf'], content_types='name', ancestor_folder_ids=31436627801,type='file')
data_temp =''
idanterior=''
for item in items:
    if item.created_at < data_temp:
        print("Arquivo recente existente")
    else:
        idRecente=item.id
        data_temp = item.created_at
        idanterior= item.id
box_file = client.file(file_id=idRecente).get()
output_file = open(ABSOLUTE_PATH+'\\Resultados\\'+ box_file.name, 'wb')
box_file.download_to(output_file)