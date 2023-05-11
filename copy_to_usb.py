import os
import shutil

# Define the name of the USB device you're looking for
target_device_name = "CIRCUITPY"
target_device_drive = None

# Find the drive letter of the target USB device
drive_letters = [f'{chr(ord("A")+i)}:' for i in range(25)]

for drive in drive_letters:
    if os.path.isdir(drive):
        try:
            volume_name = os.popen("vol " + drive).read().strip()
            if volume_name.__contains__(target_device_name):
                target_device_drive = drive
                break
        except Exception as e:
            print(e)
            pass


if target_device_drive is None:
    exit(1)
else:
    print(f"Device found at: {target_device_drive}")

# Define the paths to the folders and file you want to delete, copy, and overwrite
project_folder_to_delete = os.path.join(target_device_drive, 'magic_macro')
project_folder_to_copy = os.path.join(os.getcwd(), 'magic_macro')
entrypoint_to_copy = os.path.join(os.getcwd(), 'main_code.py')

# Delete the folder
if os.path.isdir(project_folder_to_delete):
    shutil.rmtree(project_folder_to_delete)

# Copy the folder and the file
shutil.copytree(project_folder_to_copy, os.path.join(target_device_drive, 'magic_macro'))
shutil.copyfile(entrypoint_to_copy, os.path.join(target_device_drive, 'code.py'))

