import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Load the WAV file
wav_file_path = 'prueba.wav'
sound = pygame.mixer.Sound(wav_file_path)

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Waveform Amplitude Example')

# Load your sprite images
low_amplitude_sprite_path = 'reposo.jpg'
high_amplitude_sprite_path = 'bocaabierta.jpg'

low_amplitude_sprite = pygame.image.load(low_amplitude_sprite_path)
high_amplitude_sprite = pygame.image.load(high_amplitude_sprite_path)

sprite_width, sprite_height = low_amplitude_sprite.get_size()

# Set the sprite's initial position
sprite_x, sprite_y = screen_width // 2, screen_height // 2

# Play the sound
sound.play()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the waveform data from the WAV file
    waveform = np.frombuffer(sound.get_raw(), dtype=np.int16)

    # Calculate the current amplitude (average absolute value of waveform samples)
    amplitude = np.mean(np.abs(waveform))

    # Choose the sprite based on the amplitude threshold (you can adjust this threshold as needed)
    if amplitude > 1000:
        current_sprite = high_amplitude_sprite
    else:
        current_sprite = low_amplitude_sprite

    # Change sprite position based on amplitude (adjust as needed based on your WAV file and desired effect)
    sprite_x = int(screen_width / 2 + amplitude)
    sprite_y = int(screen_height / 2 + amplitude)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the current sprite at the updated position
    screen.blit(current_sprite, (sprite_x - sprite_width // 2, sprite_y - sprite_height // 2))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
