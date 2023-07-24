import numpy as np
import scipy.io.wavfile as wavfile
import pygame

def load_wav(file_path):
    """Load a WAV file and return the sample rate and audio data."""
    sample_rate, audio_data = wavfile.read(file_path)
    return sample_rate, audio_data

def analyze_waveform(audio_data):
    """Analyze the waveform to calculate sample loudness bit by bit."""
    max_amplitude = np.max(np.abs(audio_data))
    bit_depth = 16  # Assuming a 16-bit WAV file, modify this if using a different bit depth.
    max_loudness = 2 ** (bit_depth - 1) - 1
    sample_loudness = np.round(np.abs(audio_data) / max_amplitude * max_loudness).astype(int)
    return sample_loudness

def get_sprite_based_on_loudness(sample_loudness):
    """Change the sprite based on the sample loudness."""
    # Define the range for loudness values that correspond to the sprite change
    threshold = 100  # Adjust this threshold based on your specific WAV file and requirements
    if np.any(sample_loudness > threshold):
        return sprite2
    else:
        return sprite1

if __name__ == "__main__":
    file_path = "prueba.wav"  # Replace with the path to your WAV file
    sample_rate, audio_data = load_wav(file_path)
    sample_loudness = analyze_waveform(audio_data)

    pygame.init()
    screen = pygame.display.set_mode((1024, 1024))
    clock = pygame.time.Clock()

    # Load your sprites here (sprite1 and sprite2)
    sprite1 = pygame.image.load("reposo.jpg")
    sprite2 = pygame.image.load("abierto.jpg")
    
    current_sprite = sprite1

    # Play the WAV file using pygame.mixer
    pygame.mixer.init(frequency=sample_rate)  # Set the mixer frequency to match the sample rate
    audio_obj = pygame.mixer.Sound(file=file_path)

    running = True
    contador = 0
    while running:
        contador += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get the sprite based on the loudness data
        current_sprite = get_sprite_based_on_loudness(sample_loudness[contador][0])

        # Play the audio
        audio_obj.play()

        # Update the display
        screen.fill((255, 255, 255))
        screen.blit(current_sprite, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    # Stop the audio before quitting
    audio_obj.stop()
    pygame.quit()
