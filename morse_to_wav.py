import numpy as np
import wave

def morse_to_audio(morse_code, filename, wpm=20, freq=600):
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

    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)  # 16 bits
        f.setframerate(sample_rate)
        f.writeframes(audio.tobytes())

# Example usage
if __name__ == "__main__":
    morse_code = "......-...-..---/.-----.-..-..-.."  # "HELLO WORLD"
    morse_to_audio(morse_code, "hello_world.wav")
