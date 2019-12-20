import os

FolderPath = r"C:\Users\jaw\Desktop\Brunswick_1106_Attachments"
fileList = []
for root, dirs, files in os.walk(FolderPath):
    for filename in files:
        fileList.append(filename)

print(fileList)