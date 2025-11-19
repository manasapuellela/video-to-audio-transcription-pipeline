def save_transcript(text, output_file="transcript.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
