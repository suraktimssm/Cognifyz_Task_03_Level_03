import os
import shutil

folder_path = r"E:\Users\suraktim choudhury\Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

for folder in file_types:
    path = os.path.join(folder_path, folder)
    if not os.path.exists(path):
        os.makedirs(path)
        
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                moved = True
                break
        
        if not moved:
            other_path = os.path.join(folder_path, "Others")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, filename))
            
print("✔ Files organized successfully!")    