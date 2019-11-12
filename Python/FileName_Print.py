import os

for root, dirs, files in os.walk(r"S:\ArcGIS\Python"):
    for filename in files:
        print(filename)
