import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select the directory
def select_directory():
    global directory
    directory = filedialog.askdirectory()
    if directory:
        organize_button.config(state=tk.NORMAL)
        status_label.config(text=f"Selected Directory: {directory}")

#Main function to organize the files
def organize_files():
    if not directory:
        messagebox.showwarning("Warning", "No directory selected")
        return

#We define file types
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.rb']
    }

    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if any(file.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, file))

    status_label.config(text="Files organized successfully")
    messagebox.showinfo("Success", "Files organized successfully")

if __name__ == "__main__":
    #GUI
    window = tk.Tk()
    window.title("File Organizer")
    window.geometry("600x400")
    window.iconbitmap("file.ico")
    
    label = tk.Label(window, text="Select a directory to organize:")
    label.pack(pady=10)
    
    select_button = tk.Button(window, text="Select Directory", command=select_directory)
    select_button.pack(pady=10)
    
    organize_button = tk.Button(window, text="Organize Files", command=organize_files, state=tk.DISABLED)
    organize_button.pack(pady=10)
    
    status_label = tk.Label(window, text="")
    status_label.pack(pady=10)
    
    directory = None
    
    window.mainloop()