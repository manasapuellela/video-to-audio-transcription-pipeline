import moviepy.editor as mp

def extract_audio_from_video(video_path, output_path="output_audio.wav"):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    return output_path

