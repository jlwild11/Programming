import os
import pandas as pd


FolderPath = r"N:\GIS\Projects\USFS\Stand_Exams\PHOTO EXPORT\20200512_"
fileList = []
for root, dirs, files in os.walk(FolderPath):
    for filename in files:
        fileList.append(filename)

print(fileList)

#ExportFilename = r"C:\Users\jaw\OneDrive - Mountain G. Enterprises, Inc\Desktop\CSV\20200512_.csv"
#df = pd.DataFrame(fileList, columns=["Filenames"])
#df.head()
#csv.to_csv(ExportFilename,index=False)