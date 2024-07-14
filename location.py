import os 
import json 


phil_json = os.path.join("philippines.json")

with open(phil_json, "r") as phil_read:
    phil_data = json.load(phil_read)

regions = []
province = []
municipality = []  
barangay = []

def regions_list():
    for each_regions in phil_data.keys():
        regions.append(each_regions)

regions_list()

def province_select(selected_region):
    province.clear()
    for each_province in phil_data[selected_region]['province_list'].keys():
       province.append(each_province)
    return list(province)

def municipality_select(regionsx, provincex):
    municipality.clear()
    for each_city in phil_data[regionsx]['province_list'][provincex]['municipality_list'].keys():
       municipality.append(each_city)
    return list(municipality)

regionsx = "regions IV-A"
provincex = "QUEZON"
cityx="LUCENA CITY"

def brgy_select(regionsx, provincex, cityx):
    barangay.clear()
    for each_brgy in phil_data[regionsx]['province_list'][provincex]['municipality_list'][cityx]:
        barangay.extend(phil_data[regionsx]['province_list'][provincex]['municipality_list'][cityx][each_brgy])
    return barangay