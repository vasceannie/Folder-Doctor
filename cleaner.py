import os
import shutil
from tkinter import Tk, filedialog

def organize_folder(folder):
    """
    Organizes the files in the given folder by moving them into subfolders based on their file extensions.

    Parameters:
    folder (str): The path to the folder to organize.

    Returns:
    None
    """
    # Get a list of all files in the selected folder
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    for file in files:
        # Get the file extension and make it lowercase
        file_extension = os.path.splitext(file)[1].lower()
        
        # If the file has no extension, skip it
        if not file_extension:
            continue
        
        # Create a folder for the file extension if it doesn't exist
        # [1:] to remove the dot from the file extension
        extension_folder = os.path.join(folder, file_extension[1:])
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
        
        # Move the file into the appropriate folder
        shutil.move(os.path.join(folder, file), os.path.join(extension_folder, file))
    
    # Print a success message after organizing the folder
    print("Folder organized successfully!")

if __name__ == "__main__":
    # Hide the main Tkinter window
    Tk().withdraw()

    # Open a dialog to select a folder
    folder = filedialog.askdirectory(title="Select the folder to organize")

    # If a folder is selected, organize it
    if folder:
        organize_folder(folder)
    else:
        # Print a message if no folder is selected
        print("No folder selected. Operation cancelled.")
