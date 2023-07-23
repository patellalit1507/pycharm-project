import ffmpeg

input_video=ffmpeg.input("vedo.webm")
input_audio=ffmpeg.input("audo.webm")
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('output.webm').run()