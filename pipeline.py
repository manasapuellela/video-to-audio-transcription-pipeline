import argparse
from utils.extract_audio import extract_audio_from_video
from utils.transcribe_audio import transcribe_audio
from utils.storage import save_transcript

def main(video_path):
    print("Step 1: Extracting audio...")
    audio_path = extract_audio_from_video(video_path)

    print("Step 2: Transcribing audio using Whisper/OpenAI...")
    text = transcribe_audio(audio_path)

    print("Step 3: Saving transcript...")
    save_transcript(text)

    print("\nPipeline complete!")
    print("Transcript saved to transcript.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", required=True, help="Path to video file (.mp4)")
    args = parser.parse_args()

    main(args.video)

