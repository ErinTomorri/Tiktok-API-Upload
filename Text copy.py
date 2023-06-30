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

def create(b, voice):


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

def images(b):



main()