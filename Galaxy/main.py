import ffmpeg
from moviepy.editor import VideoFileClip,AudioFileClip
if __name__ == '__main__':
    input_vid =VideoFileClip('C:/Users/ASUS/Desktop/youtube/vid.mp4')
    input_aud=AudioFileClip('C:/Users/ASUS/Desktop/youtube/aud.webm')
    output_clip=input_vid.set_audio(input_aud)
    output_clip.write_videofile('C:/Users/ASUS/Desktop/youtube/final.mp4')