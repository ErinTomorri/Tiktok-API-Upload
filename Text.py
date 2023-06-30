# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from moviepy.editor import *
import numpy as np
import random
import numpy as np
import os
import requests

def shake(txt_clip, jitter=10):
    return txt_clip.fl_image(lambda image: image * (1 - jitter) + jitter * (np.random.randn(*image.shape) % 255)).set_duration(txt_clip.duration)

def add_fade_and_shake_text(input_video, output_video, text, start_time, duration):
    video = VideoFileClip(input_video)

    # Define the text clip
    txt_clip = (TextClip(text, fontsize=75, color='white', font='Font.otf')
                .set_duration(duration)
                .crossfadein(1)  # Fading in the text clip
                .crossfadeout(1))  # Fading out the text clip
    txt_clip = txt_clip.set_position(('center', 'center'))  # Set the position of the text clip

    # Add shake effect to the text clip
    shaken_text = shake(txt_clip)

    # Add the text clip to the video
    video = CompositeVideoClip([video, shaken_text.set_start(start_time)])

    # Write the final video with the text overlay
    video.write_videofile(output_video, codec='libx264', audio_codec="aac")

def add_fade_and_slide_text(input_video, output_video, text, start_time, duration, slide_position):
    video = VideoFileClip(input_video)

    # Define the text clip
    txt_clip = (TextClip(text, fontsize=50, color='white')
                .set_duration(duration)
                .fadein(1)
                .fadeout(1)
                .set_position(('center', 'top'))
                .set_start(start_time))

    # Calculate the slide animation
    slide_duration = 1  # Duration of the slide animation (in seconds)
    slide_start_position = slide_position  # Start position of the slide animation
    rand_x =  random.randint(1, 1080)
    rand_y =  random.randint(1, 1920)
    slide_end_position = (rand_x, rand_y)  # End position of the slide animation

    # Convert slide position values from strings to integers
    slide_start_x, slide_start_y = slide_start_position
    slide_end_x, slide_end_y = slide_end_position
    slide_start_x = int(slide_start_x)
    slide_start_y = int(slide_start_y)
    slide_end_x = int(slide_end_x)
    slide_end_y = int(slide_end_y)

    # Calculate the position of the text clip for each frame during the slide animation
    def slide_position_func(t):
        if t < 0:
            return slide_start_position
        elif t > slide_duration:
            return slide_end_position
        else:
            progress = t / slide_duration
            x = int(slide_start_x + (slide_end_x - slide_start_x) * progress)
            y = int(slide_start_y + (slide_end_y - slide_start_y) * progress)
            return (x, y)

    # Apply slide animation to the text clip
    txt_clip = txt_clip.set_position(slide_position_func)

    # Add the text clip to the video
    video = CompositeVideoClip([video, txt_clip])

    # Write the final video with the text overlay
    video.write_videofile(output_video, codec='libx264', audio_codec="aac")

# Example usage

def create(b, voice):
    input_video = "production_id_4678261 (1080p).mp4"
    output_video = "output.mp4"
    text = "Fading and Sliding Text"
    start_time = 1  # seconds
    duration = 1  # seconds
    slide_position = ('200', '100')  # Starting position of the slide animation

    add_fade_and_slide_text(input_video, output_video, text, start_time, duration, slide_position)

def read():
    # Open the text file
    words = []
    phrase = ""
    count = 0
    voice = 0
    file_path = 'Audio/DANKTON - KYS.txt'  # Replace with the actual file path

    # Alternatively, you can read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == "Voice: Krabs":
                voice = 0
            elif line.strip() == "Voice: Patrick":
                voice = 1
            elif line.strip() == "Voice: Spongebob":
                voice = 2
            elif line.strip() == "Voice: Plankton":
                voice = 3
            elif line.strip() == "Voice: Squidward":
                voice = 4
            if line.strip() == "":
                count1 = 0
                phrase = phrase.replace(", ","\n")
                words.append(phrase)
                phrase = ""
                count+=1
            else:
                phrase += line
    return words, voice

def main():
    c,voice = read()
    create(c, voice)

'''def images(b):
    for num in range(len(b)):
        if "patrick" in b[num].lower():
        elif "krabs" in b[num].lower():
        elif "shot" in b[num].lower():
        elif "puff" in b[num].lower():
        elif "chum" in b[num].lower():
        elif "sponge" in b[num].lower():
        elif "cobain" in b[num].lower():
        elif "lean" in b[num].lower():
        elif "sponge" in b[num].lower():
        elif "biggie" in b[num].lower():
        elif "tupac" in b[num].lower():
        elif "police" in b[num].lower():
        elif "choppa" in b[num].lower():
        elif "pearl" in b[num].lower():
        elif "bucket" in b[num].lower():
        elif "lamborghini" in b[num].lower():
        elif "bikini" in b[num].lower():
        elif "cudi" in b[num].lower():
        elif "walk" in b[num].lower():
        elif "sandy" in b[num].lower():
        elif "squirrel" in b[num].lower():
        elif "karen" in b[num].lower():
        elif "mag" in b[num].lower():
        elif "weapon" in b[num].lower():
        elif "krusty" in b[num].lower():
        elif "andy" in b[num].lower():
        elif "spongeboy" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "mil" in b[num].lower():
        elif "empty" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "spongebob" in b[num].lower():
        elif "spongebob" in b[num].lower():
'''

main()