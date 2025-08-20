import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def morse_to_audio(morse_code, wpm=20, freq=600):
    dot_duration = 1.2 / wpm  # seconds
    dash_duration = dot_duration * 3
    symbol_space = dot_duration
    letter_space = dot_duration * 3
    word_space = dot_duration * 7
    sample_rate = 44100

    def tone(duration):
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        audio = np.sin(2 * np.pi * freq * t)
        return (audio * 32767).astype(np.int16)

    def silence(duration):
        return np.zeros(int(sample_rate * duration), dtype=np.int16)

    audio = np.array([], dtype=np.int16)
    for word in morse_code.split(' / '):
        for letter in word.split(' '):
            for symbol in letter:
                if symbol == '.':
                    audio = np.concatenate([audio, tone(dot_duration), silence(symbol_space)])
                elif symbol == '-':
                    audio = np.concatenate([audio, tone(dash_duration), silence(symbol_space)])
            audio = np.concatenate([audio, silence(letter_space - symbol_space)])
        audio = np.concatenate([audio, silence(word_space - letter_space)])

    return audio

def save_morse_mp3(morse_code, filename="morse.mp3", wpm=20, freq=600):
    audio = morse_to_audio(morse_code, wpm, freq)
    sample_rate = 44100
    # Convert numpy array to AudioSegment
    segment = AudioSegment(
        audio.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio.dtype.itemsize,
        channels=1
    )
    segment.export(filename, format="mp3")
    print(f"Morse code saved as {filename}")

# Example usage
if __name__ == "__main__":
    morse_code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."  # "HELLO WORLD"
    save_morse_mp3(morse_code, "hello_world.mp3")
