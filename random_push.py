import os

def create_directory(directory_name):
    """
    Creates a new directory with the given name.
    
    Args:
        directory_name (str): The name of the directory to be created.
    """
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

def create_subfolders(directory_name, subfolders):
    """
    Creates subfolders within the given directory.
    
    Args:
        directory_name (str): The name of the directory where subfolders will be created.
        subfolders (list): A list of subfolder names.
    """
    for subfolder in subfolders:
        subfolder_path = os.path.join(directory_name, subfolder)
        try:
            os.mkdir(subfolder_path)
            print(f"Subfolder '{subfolder}' created successfully.")
        except FileExistsError:
            print(f"Subfolder '{subfolder}' already exists.")

def main():
    directory_name = "MyFiles"
    subfolders = ["Audio", "Images", "Text"]
    
    create_directory(directory_name)
    create_subfolders(directory_name, subfolders)

if __name__ == "__main__":
    main()