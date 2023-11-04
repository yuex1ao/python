import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from pytube import YouTube;

window = tk.Tk()
window.title("youtube影片下載器")
window.minsize(width = 960, height = 540)
window.resizable(width = False, height = False)
photo = PhotoImage(file = "background.png")

label = Label(window, image = photo, justify=LEFT, compound = CENTER)
label.pack()

textLabel1 = Label(window, text = "複製影片網址", font=("標楷體",16), fg = 'black')
textLabel1.place(relx = 0.01, rely = 0.01)

textLabel2 = Label(window, text = "輸入儲存檔名", font=("標楷體",16), fg = 'black')
textLabel2.place(relx = 0.01, rely = 0.08)

textLabel3 = Label(window, text = "選擇儲存位置", font=("標楷體",16), fg = 'black')
textLabel3.place(relx = 0.01, rely = 0.15)

textLabel3 = Label(window, text = "選擇檔案格式", font=("標楷體",16), fg = 'black')
textLabel3.place(relx = 0.01, rely = 0.22)


youtubeURL = StringVar()
entry1 = Entry(width=40, font=("標楷體", 16, "bold"), bg="#4EFEB3", fg="#930093", state=NORMAL, textvariable = youtubeURL)
entry1.place(relx = 0.16, rely = 0.01)

youtubeName = StringVar()
entry2 = Entry(width=30, font=("標楷體", 16, "bold"), bg="#4EFEB3", fg="#930093", state=NORMAL, textvariable = youtubeName)
entry2.place(relx = 0.16, rely = 0.08)

setpath = StringVar()
def selectPath():
    setpath_ = askdirectory()
    setpath.set(setpath_)

entry3 = Entry(width=20, font=("標楷體", 16, "bold"), bg="#4EFEB3", fg="#930093", state=NORMAL, textvariable = setpath)
entry3.place(relx = 0.16, rely = 0.15)

button = Button(text = "選擇路徑", font=("標楷體", 12, "bold"), command = selectPath)
button.place(relx = 0.42, rely = 0.15)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="MP3", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="MP4", value=2, variable=radio_state)
radiobutton1.place(relx = 0.2, rely = 0.22)
radiobutton2.place(relx = 0.3, rely = 0.22)


def start_click():
    downLoader()

start = Button(text = "開始下載", font=("標楷體", 16, "bold"), command = start_click, bg = '#FF8EFF')
start.place(relx = 0.15, rely = 0.3)

def downLoader():
    try: # get above data and download
        url = str(youtubeURL.get())
        name = str(youtubeName.get())
        format = radio_state.get() # 1 -> MP3, 2 -> MP4
        path = str(setpath.get())
        yt = YouTube(url) 

        if(format == 1):
            yt.streams.filter().get_audio_only().download(output_path=path, filename = name + '.mp3')
        else:
            yt.streams.filter().get_highest_resolution().download(output_path=path, filename = name + '.mp4')
        outputLabel = Label(text = "下載完成", fg = "red", font=("標楷體", 18, "bold"))
        outputLabel.place(relx = 0.15, rely = 0.4)
    except Exception as e:
        print(e)
        outputLabel = Label(window, text = e, fg = "red")
        outputLabel.place(relx = 0.01, rely = 0.4)

window.mainloop()