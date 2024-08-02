from pytube import YouTube
from tkinter import *
from tkinter import filedialog

def download_vid():
    video_url = url_entry.get()
    save_path = open_file_dialog()

    if save_path:
        try:
            yt = YouTube(video_url)
            broadcasts = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res = broadcasts.get_highest_resolution()
            
            # Make the button disable while download
            download_button.config(text="Downloading", state=DISABLED)
            
            highest_res.download(output_path=save_path)

            result_label.config(text="Video download completed.")
        
        except Exception as e:
            result_label.config(text="Error: " + str(e))
        
        finally:
            # Make the button enable after download is completed
            download_button.config(text="Download", state=NORMAL)

    else:
        result_label.config(text="Incorrect save location.")

    if video_url == 'close' or 'quit':
        window.quit()

def open_file_dialog():
    folder = filedialog.askdirectory()

    if folder:
        print("Selected folder: " + str(folder))

    return folder

# GUI
window = Tk()
window.title("YouTube Video Downloader")
window.geometry('600x200')
window.iconbitmap('yt_icon.ico')

# Youtube URL entry
url_label = Label(window, text="Enter YouTube video link:")
url_label.pack(pady=10)

url_entry = Entry(window, width=40)
url_entry.pack(pady=10)

# Download button
download_button = Button(window, text="Download", command=download_vid)
download_button.pack(pady=10)

# Download result label
result_label = Label(window, text="")
result_label.pack(pady=10)

window.mainloop()