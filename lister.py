import os

file_extentions =('.db', '.sql', '.key','.pem')

for root, dirs, files in os.walk ('.'):
    for file in files: 
        if file.endswith(file_extentions):
            print(os.path.join(root, file))