import os
import random
import sys

def remove_random_images(folder_path, num_to_remove):
    """
    Randomly selects and removes a specified number of files from a folder.

    Args:
        folder_path (str): The path to the folder containing the images.
        num_to_remove (int): The number of random images to remove.
    """
    print(f"Attempting to remove {num_to_remove} random images from '{folder_path}'...")

    # --- 1. Validate the folder path ---
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # --- 2. Get a list of all files in the directory ---
    try:
        # We use os.path.join to create the full path for os.path.isfile
        all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    except OSError as e:
        print(f"Error: Could not access the folder '{folder_path}'. Reason: {e}")
        return

    # --- 3. Check if there are enough files to remove ---
    if len(all_files) < num_to_remove:
        print(f"Warning: The folder contains only {len(all_files)} files, which is less than the {num_to_remove} requested for removal.")
        print("No files will be deleted.")
        return

    # --- 4. Randomly select the files to be deleted ---
    files_to_delete = random.sample(all_files, num_to_remove)
    
    print(f"\nThe following {len(files_to_delete)} files will be permanently deleted:")
    for filename in files_to_delete:
        print(f"  - {filename}")
    
    # --- 5. Get final confirmation from the user ---
    # Use a raw string for the prompt to handle backslashes if any
    confirm = input(r"Are you sure you want to proceed? (yes/no): ")
    if confirm.lower() != 'yes':
        print("\nOperation cancelled by user.")
        return

    # --- 6. Delete the selected files ---
    deleted_count = 0
    errors_count = 0
    print("\nDeleting files...")
    for filename in files_to_delete:
        try:
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            deleted_count += 1
        except OSError as e:
            print(f"Error deleting file {filename}: {e}")
            errors_count += 1
            
    print("\n--- Deletion Complete ---")
    print(f"Successfully deleted: {deleted_count} files.")
    if errors_count > 0:
        print(f"Failed to delete:   {errors_count} files.")

if __name__ == "__main__":
    # --- Configuration ---
    TARGET_FOLDER = 'new_dataset/replay'
    NUMBER_OF_FILES_TO_DELETE = 384
    
    remove_random_images(TARGET_FOLDER, NUMBER_OF_FILES_TO_DELETE)
