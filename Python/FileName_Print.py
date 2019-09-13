import os

for root, dirs, files in os.walk(r"C:\Users\jaw\Desktop\BP10_BLM_Before_And_After_Photos"):
    for filename in files:
        print(filename)
