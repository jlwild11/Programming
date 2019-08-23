import os

for root, dirs, files in os.walk(r"N:\PROJECTS\PLACER_COUNTY\500_GIS_Data\Bid_Packages\Active\BP_08\PHOTOS\TREE_PHOTOS_BEFORE"):
    for filename in files:
        print(filename)
