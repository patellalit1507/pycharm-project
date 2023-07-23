from tkinter import *
from pytube import YouTube
import os

root=Tk()
root.title("Youtube Video downloader")
root.geometry('600x600')
link=StringVar()

#def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
     #percent = (100*(file_size-remaining))/file_size
    # print("{:00.0f}% downloaded".format(percent))

def remove():
    global videoname
    if os.path.exists("videoname.mp4"):
        os.rename("videoname.mp4",videoname[:9])

        os.remove("tempv.mp4")
        os.remove("tempa.webm")

    else:
        print("file not found")

def combine():
    global videoname
    import moviepy.editor as mpe
    my_clip=mpe.VideoFileClip("tempv.mp4")
    my_audio=mpe.AudioFileClip("tempa.webm")
    final_clip=my_clip.set_audio(my_audio)
    final_clip.write_videofile('videoname.mp4')
    my_audio.close()
    my_clip.close()

    remove()




def get_url():

     Url=YouTube(str(link.get()))
     mystreams=Url.streams
     print(mystreams.filter(res="720p",progressive=False).all)

     video=Url.streams.filter(res='720p',progressive=False,mime_type='video/mp4').first()
     Audio=Url.streams.filter(mime_type="audio/webm").last()

     #file_size=mystreams.filesize
     #print("{} mb".format(file_size/1000000))
     try:
         video.download('C:/Users/ASUS/PycharmProjects/pythonProject/assignment',filename="tempv")
         Audio.download("C:/Users/ASUS/PycharmProjects/pythonProject/assignment",filename="tempa")

         Label(root, text='DOWNLOADED', font='arial 15').place(x=250, y=300)
         global videoname
         videoname=video.title

         combine()
     except:
         print("some error occured ")

     combine()
def main():
      get_link=Entry(root,text=link,bg="pink",width=40,font=("arial",14))
      btn_submit=Button(root,text="Download",font=("Arial"),command=get_url)
      get_link.place(x=100,y=200)
      btn_submit.place(x=250,y=250)

main()


root.mainloop()