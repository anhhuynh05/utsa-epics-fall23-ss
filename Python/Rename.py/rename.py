import os

folder_path = "C:\\Users\\duyan\\OneDrive\\Pictures\\Python"
os.chdir(folder_path)

file_list = os.listdir()

for index, filename in enumerate(file_list):
    if filename.endswith(".jpg"):  # Adjust the file extension accordingly
        new_filename = f"UTSA_{index + 1}.jpg"
        os.rename(filename, new_filename)
        print(f"Renamed {filename} to {new_filename}")
