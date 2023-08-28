import os
import shutil

def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)
        if os.path.isfile(item_path):
            file_extension = item.split(".")[-1]
            target_folder = os.path.join(destination_folder, file_extension)
            
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            new_item_path = os.path.join(target_folder, item)
            shutil.move(item_path, new_item_path)
            print(f"Moved {item} to {target_folder}")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")
    organize_files(source_folder, destination_folder)
