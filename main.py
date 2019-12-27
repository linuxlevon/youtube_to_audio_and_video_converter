import pytube.compat
from tkinter import messagebox
from tkinter.filedialog import askdirectory

video_input = input("Enter a video url: ")
yt = pytube.YouTube(video_input)

question = messagebox.askquestion('Format', 'Do yu want to choose the video format?')
if question == 'yes':
    videos = yt.streams.filter(progressive=True).all()
    for i in range(len(videos)):
        print(i, " ", videos[i])

else:
    videos = yt.streams.filter(subtype='webm').all()
    print("*Note This Option Wont Have Sound If You Want To Download the Video*")
    for x in range(len(videos)):
        print(x, " ", videos[x])

num = int(input("Enter you're choice: "))

messagebox.showinfo('Save Video', 'Choose a directory')
placeholder = askdirectory()
videos[num].download(placeholder)
messagebox.showinfo("Done", f'Video was sucessfully downloaded to {placeholder}')

