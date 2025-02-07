#os for access to info about computer os 
#shutil to easily manipulate files

import os 
import shutil

#define categories of files for the desktop cleaner to recognise
categories = {
    "Pictures": [".png", ".jpeg", ".jpg", ".gif"],
    "Documents": [".docx", ".pdf", ".xlsx", ".odt", ".txt"],
    "Videos": [".mov", ".mp4"],
}

#change user for personal use
user = "matthewchen"
user_dir = f"/Users/{user}"

def organise(source_dir = user_dir + '/Desktop'):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        #skip directories and handle system files 
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()


        moved = False
        for category, extension in categories.items():
            if ext in extension:
                dest_dir = os.path.join(user_dir, category)
                os.makedirs(dest_dir, exist_ok = True) 
                shutil.move(file_path, dest_dir)
                moved = True
                print(f"{filename} successfully moved to {category} folder! ")
                break
    
        if not moved:
            dest_dir = os.path.join(source_dir, "Other")
            os.makedirs(dest_dir, exist_ok = True)
            shutil.move(file_path, dest_dir)
            print(f"{filename} successfully moved to 'Other' folder!")
    

if __name__ == "__main__":
    organise()
        











