import moviepy.editor

video = moviepy.editor.VideoFileClip("A ARTE DA FRIEZA - CONTROLE e USE suas Emoções com SABEDORIA.mp4")

# if your video is in same folder where your python file than you can give nam direct
# else you need to give path 

audio =  video.audio
audio.write_audiofile("extractedsong.mp3 ")