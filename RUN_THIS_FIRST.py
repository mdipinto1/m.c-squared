import os
import zipfile

#Extracts oversized files for execution
#Adds london_airbnb.html to gitignore automatically
files_extracted = ['./denver_airbnb.html', './london_airbnb.html']


#Extracts London AirBnb data, if not already extracted
destination_file = './Clean_Data/London_AirBNB_Data.csv'
if not os.path.exists(destination_file):
    file_to_unzip = './Clean_Data/London_AirBNB_Data.zip'
    extract_to_dir = './Clean_Data/'
    with zipfile.ZipFile(file_to_unzip, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    files_extracted.append(destination_file)
    print(f"{file_to_unzip} extracted successfully")
else: print(f"{destination_file} already present.")


#Extracts London Starbucks data, if not already extracted
destination_file = './Clean_Data/London_Starbucks_Data.csv'
if not os.path.exists(destination_file):
    file_to_unzip = './Clean_Data/London_Starbucks_Data.zip'
    extract_to_dir = './Clean_Data/'
    with zipfile.ZipFile(file_to_unzip, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    files_extracted.append(destination_file)
    print(f"{file_to_unzip} extracted successfully")
else: print(f"{destination_file} already present.")


#Extracts london_listings, if not already extracted
destination_file = './Raw_Data/london_listings.csv'
if not os.path.exists(destination_file):
    file_to_unzip = './Raw_Data/london_listings.zip'
    extract_to_dir = './Raw_Data/'
    with zipfile.ZipFile(file_to_unzip, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    files_extracted.append(destination_file)
    print(f"{file_to_unzip} extracted successfully")
else: print(f"{destination_file} already present.")


#Opens .gitignore as read, checks .gitignore for presence of files
#Appends files that were extracted above and are not already present to .gitignore
with open('.gitignore', "r") as file:
    lines_for_gitignore = []
    lines = file.readlines()
    for file_name in files_extracted:
        file_in_gitignore = False
        for line in lines:
            if file_name.lstrip('./') in line:
                file_in_gitignore = True
                break
        if not file_in_gitignore:
            lines_for_gitignore.append(file_name)
        else: print(f"{file_name} already in .gitignore")
file.close()

#Opens .gitignore as append and writes each file from lines_for_gitignore
with open('.gitignore', 'a') as file:
    for file_name in lines_for_gitignore:
        file.write('\n'+file_name.lstrip('./'))
        print(f"Added {file_name} to .gitignore")