import moviepy.editor as mpe

clip1 = mpe.VideoFileClip("brownv.mp4")
clip2=mpe.AudioFileClip('brown.mp3')
tempclip=clip2.set_fps(clip1.fps)
print(tempclip.fps)
finalclip=clip1.set_audio(tempclip)
finalclip.write_videofile("final3.mp4")


