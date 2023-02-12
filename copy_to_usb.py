import os
import shutil

# Define the name of the USB device you're looking for
target_device_name = "CIRCUITPY"
target_device_drive = None

# Find the drive letter of the target USB device
for drive in ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']:
    if os.path.isdir(drive):
        try:
            volume_name = os.popen("vol " + drive).read().strip()
            if volume_name.__contains__(target_device_name):
                target_device_drive = drive
                break
        except Exception as e:
            print(e)
            pass

print(f"Device found at: {target_device_drive}")

if target_device_drive is None:
    exit(1)

# Define the paths to the folders and file you want to delete, copy, and overwrite
folder_to_delete = os.path.join(target_device_drive, 'magic_macro')
folder_to_copy = os.path.join(os.getcwd(), 'magic_macro')
file_to_copy = os.path.join(os.getcwd(), 'main_code.py')

# Delete the folder
if os.path.isdir(folder_to_delete):
    shutil.rmtree(folder_to_delete)

# Copy the folder
shutil.copytree(folder_to_copy, os.path.join(target_device_drive, 'magic_macro'))
shutil.copyfile(file_to_copy, os.path.join(target_device_drive, 'code.py'))

