import os

for root, dirs, files in os.walk(r"C:\Users\jaw\Desktop\Div01_Photos_Before_and_After"):
    for filename in files:
        print(filename)
