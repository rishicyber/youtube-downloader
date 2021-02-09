import pafy
import tkinter as tk
from tkinter import ttk
from threading import Thread
from tkinter import font


win = tk.Tk()
win.title("Youtube Downloader")
# win.minsize(400, 225)
win.maxsize(1920, 1080)
win.resizable(False, False)
win.iconbitmap("youtube.ico")


style = ttk.Style(win)
font = font.Font(family="Comic Sans MS", size=10, weight="bold")
style.configure("TButton", font=font)


def startDownloadingThread(file_handler):
    run_thread = Thread(target=startDownloading, args=(file_handler,))
    run_thread.start()


def startDownloading(file_handler):
    radSel = radVar.get()
    if radSel == 0:
        abc = file_handler.getbest()
    elif radSel == 1:
        abc = file_handler.getbestvideo(preftype="mp4", ftypestrict=False)
    elif radSel == 2:
        abc = file_handler.getbestaudio(preftype="m4a", ftypestrict=False)
    abc.download()
    result_label.configure(
        text=f"{file_handler.title}\nDuration :  {file_handler.duration}\nblah blah\n\n\nDownloaded"
    )


def SearchFor():
    url = entered_url.get()
    if url == "":
        result_label.configure(text="Seems like you haven't entered an link yet")
    else:
        # result_label.configure(text=url)
        try:
            file_handler = pafy.new(url)
            video_title = file_handler.title
            video_duration = file_handler.duration
            # abc = file_handler.getbest()
            # abc.download()
            startDownloadingThread(file_handler)  # Download in a separate thread

            # list_of_streams = file_handler.allstreams
            result_label.configure(
                text=f"{video_title}\nDuration :  {video_duration}\nblah\nblah\nblah...\n\n\nDownload in progress"
            )
        except:
            result_label.configure(text="Please enter a valid youtube link")


main_frame = ttk.LabelFrame(win, text="Welcome to my youtube downloader")
main_frame.grid(row=0, column=0, padx=10, pady=10)
main_frame["padding"] = [20, 0]
# main_frame["font"] = font


url_label = ttk.Label(
    main_frame,
    text="Enter youtube link here:",
    font=("Comic Sans MS", 10, "bold italic"),
)
# font=("Comic Sans MS", 10),
url_label.grid(row=0, column=0, padx=5, pady=10, sticky="W")


entered_url = tk.StringVar()
entry_box = ttk.Entry(main_frame, width=100, textvariable=entered_url)
entry_box.grid(row=1, column=0, sticky="WE", columnspan=3)


radVar = tk.IntVar()
rad0 = tk.Radiobutton(
    main_frame,
    text="VIDEO",
    variable=radVar,
    value=0,
    font=("Comic Sans MS", 10, "bold italic"),
)
rad1 = tk.Radiobutton(
    main_frame,
    text="VIDEO ONLY",
    variable=radVar,
    value=1,
    font=("Comic Sans MS", 10, "bold italic"),
)
rad2 = tk.Radiobutton(
    main_frame,
    text="AUDIO ONLY",
    variable=radVar,
    value=2,
    font=("Comic Sans MS", 10, "bold italic"),
)
rad0.grid(row=2, column=0, sticky="W")
rad1.grid(row=2, column=1, sticky="W")
rad2.grid(row=2, column=2, sticky="E")


download_button = ttk.Button(
    main_frame,
    text="Download",
    command=SearchFor,
)
download_button.grid(row=3, column=0, pady=10, columnspan=3)

result_label = ttk.Label(
    main_frame,
    text="Let's get started",
    font=("Comic Sans MS", 12, "bold italic"),
)
result_label.grid(row=4, column=0, rowspan=10, columnspan=3)
entry_box.focus()
win.configure(background="#f05b5b")
win.attributes("-alpha", 0.9)
win.mainloop()

# url = pyperclip.paste()
# if (url == ""):
#    print("empty string")