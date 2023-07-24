import numpy as np
import scipy.io.wavfile as wavfile

def load_wav(file_path):
    """Load a WAV file and return the sample rate and audio data."""
    sample_rate, audio_data = wavfile.read(file_path)
    return sample_rate, audio_data

def analyze_waveform(audio_data):
    """Analyze the waveform to calculate sample loudness bit by bit."""
    max_amplitude = np.max(np.abs(audio_data))
    bit_depth = 16  # Assuming a 16-bit WAV file, modify this if using a different bit depth.
    max_loudness = 2 ** (bit_depth - 1) - 1
    sample_loudness = np.round(np.abs(audio_data) / max_amplitude * max_loudness)
    return sample_loudness

def print_sample_loudness_bit_by_bit(sample_loudness):
    """Print the sample loudness bit by bit."""
    bit_depth = 16  # Modify this if using a different bit depth.
    for loudness in sample_loudness:
        print(' '.join(format(int(x), f'0{bit_depth}b') for x in loudness))

if __name__ == "__main__":
    file_path = "prueba.wav"  # Replace with the path to your WAV file
    sample_rate, audio_data = load_wav(file_path)
    sample_loudness = analyze_waveform(audio_data)
    print_sample_loudness_bit_by_bit(sample_loudness)
