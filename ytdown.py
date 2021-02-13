import pafy
import tkinter as tk
from tkinter import ttk
from threading import Thread
from tkinter import font
from ttkthemes import ThemedStyle


win = tk.Tk()
win.title("Youtube Downloader")
win.resizable(False, False)
win.iconbitmap("youtube.ico")

style = ThemedStyle(win)
style.set_theme("equilux")


myFont = font.Font(family="Comic Sans MS")

style_main = ttk.Style(win)
font = font.Font(family="Comic Sans MS", size=10, weight="bold")
style_main.configure("TButton", font=font)


main_frame = ttk.LabelFrame(win)
main_frame.grid(row=0, column=0, padx=10, pady=10)
main_frame["padding"] = [20]
# main_frame["font"] = font


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
        abc = file_handler.getbestaudio()
    abc.download()
    result_label.configure(
        text=f"{file_handler.title}\nDuration :  {file_handler.duration}\n\n\nDownloaded"
    )


def SearchFor():
    url = entered_url.get()
    if url == "":
        result_label.configure(text="Seems like you haven't entered an link yet")
    else:
        try:
            file_handler = pafy.new(url)
            video_title = file_handler.title
            video_duration = file_handler.duration
            startDownloadingThread(file_handler)  # Download in a separate thread

            result_label.configure(
                text=f"{video_title}\nDuration :  {video_duration}\n\n\nDownload in progress"
            )
        except:
            result_label.configure(text="Please enter a valid youtube link")


def change_theme(a):
    theme = selected_theme.get()
    result_label.configure(text="Changed theme to " + theme)
    style.set_theme(theme)
    if theme == "scidpink":
        win.configure(background="#F72D60")
    elif theme == "scidmint":
        win.configure(background="#7EAF51")
    elif theme == "scidblue":
        win.configure(background="#41A5E1")
    elif theme == "black":
        win.configure(background="#323232")
    elif theme == "kroc":
        win.configure(background="#FFA66A")
    else:
        win.configure(background="#f05b5b")


url_label = ttk.Label(
    main_frame,
    text="Enter youtube link here:",
    font=("Comic Sans MS", 10, "bold italic"),
)
url_label.grid(row=0, column=0, padx=5, pady=10, sticky="W")


selected_theme = tk.StringVar()
number_field = ttk.Combobox(
    main_frame,
    width=20,
    textvariable=selected_theme,
    state="readonly",
)
number_field["values"] = (
    "xpnative",
    "kroc",
    "itft1",
    "blue",
    "equilux",
    "scidpink",
    "scidblue",
    "scidmint",
    "black",
)
number_field.current(4)
number_field.grid(row=0, column=2, pady=10, sticky="E")
number_field.bind("<<ComboboxSelected>>", change_theme)


entered_url = tk.StringVar()
entry_box = ttk.Entry(main_frame, width=100, textvariable=entered_url)
entry_box.grid(row=1, column=0, padx=5, pady=10, sticky="WE", columnspan=3)


radVar = tk.IntVar()
rad0 = ttk.Radiobutton(
    main_frame,
    text="VIDEO",
    variable=radVar,
    value=0,
)
rad1 = ttk.Radiobutton(
    main_frame,
    text="VIDEO ONLY",
    variable=radVar,
    value=1,
)
rad2 = ttk.Radiobutton(
    main_frame,
    text="AUDIO ONLY",
    variable=radVar,
    value=2,
)
rad0.grid(row=2, column=0, sticky="W")
rad1.grid(row=2, column=1, sticky="W")
rad2.grid(row=2, column=2, sticky="E")


download_button = ttk.Button(main_frame, text="Download", command=SearchFor)
download_button.grid(row=3, column=0, pady=10, columnspan=3)

result_label = ttk.Label(
    main_frame,
    text="Let's get started",
    font=("Comic Sans MS", 12, "bold italic"),
)
result_label.grid(row=4, column=0, rowspan=10, columnspan=3)
entry_box.focus()
win.configure(background="#f05b5b")
# win.attributes("-alpha", 0.9)  # transparency


win.mainloop()