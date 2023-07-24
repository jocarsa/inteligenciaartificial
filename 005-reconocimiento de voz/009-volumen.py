import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Load the WAV file
wav_file_path = 'prueba.wav'
sound = pygame.mixer.Sound(wav_file_path)

# Set up the display
screen_width, screen_height = 1024, 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Volume Example')

# Load your sprite images
low_volume_sprite_path = 'reposo.jpg'
high_volume_sprite_path = 'abierto.jpg'

low_volume_sprite = pygame.image.load(low_volume_sprite_path)
high_volume_sprite = pygame.image.load(high_volume_sprite_path)

sprite_width, sprite_height = low_volume_sprite.get_size()

# Set the sprite's initial position
sprite_x, sprite_y = screen_width // 2, screen_height // 2

# Play the sound
sound.play()

# Function to calculate the volume (RMS) of audio samples
def calculate_volume(waveform):
    rms = np.sqrt(np.mean(np.square(waveform)))
    return rms

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the waveform data from the WAV file
    waveform = np.frombuffer(sound.get_raw(), dtype=np.int16)

    # Calculate the volume (RMS) of the waveform
    volume = calculate_volume(waveform)

    # Choose the sprite based on the volume threshold (you can adjust this threshold as needed)
    if volume > 50:
        current_sprite = high_volume_sprite
    else:
        current_sprite = low_volume_sprite
    print(volume)

    # Change sprite position based on volume (adjust as needed based on your WAV file and desired effect)
    sprite_x = int(screen_width / 2 + volume)
    sprite_y = int(screen_height / 2 + volume)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the current sprite at the updated position
    screen.blit(current_sprite, (sprite_x - sprite_width // 2, sprite_y - sprite_height // 2))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
