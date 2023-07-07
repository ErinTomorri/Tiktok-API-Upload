# Importing the PIL library
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import numpy as np
import random
import os
import requests

def create(b, voice):
    text = ""
    count1 = 0
    for num in range(len(b)):
        if voice == 0:
            folder_path = "Images/Krabs"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Krabs/"+str(number)+".png"
            name = "Krabs"

        elif voice == 1:
            folder_path = "Images/Patrick"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Patrick/"+str(number)+".png"
            name = "Patrick"

        elif voice == 2:
            folder_path = "Images/Sponge"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Sponge/"+str(number)+".png"
            name = "Sponge"

        elif voice == 3:
            folder_path = "Images/Plankton"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Plankton/"+str(number)+".png"
            name = "Plankton"

        elif voice == 4:
            folder_path = "Images/Squidward"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Squidward/"+str(number)+".png"
            name = "Squidward"
        elif voice == 5:
            folder_path = "Images/Musk"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Musk/"+str(number)+".png"
            name = "Musk"
        elif voice == 6:
            folder_path = "Images/Zuck"
            number = random.randint(1, len(os.listdir(folder_path)))
            file = "Images/Zuck/"+str(number)+".png"
            name = "Zuck"
        # Open an Image
        img = Image.open(file)
        
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('Font.otf', 45)
        if b[num] == "Voice: "+name+"\n":
            continue
        elif b[num] != "- Dankton\n":
            text = text + b[num]
        else:
            text = ""
            count1 +=1
        # Add Text to an image
        I1.text((220,480), text, font=myFont, fill =(255, 255, 255))
        
        # Save the edited image
        img.save("FinalImage/"+name+"/"+name+str(count1)+".png")
    

def read():
    # Open the text file
    words = []
    phrase = ""
    count = 0
    voice = 0
    name = os.listdir("Text")
    rand = random.randint(0,len(name))
    file_path = 'Text/'+name[rand]  # Replace with the actual file path

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
            elif line.strip() == "Voice: Musk":
                voice = 5
            elif line.strip() == "Voice: Zuck":
                voice = 6
            if line.strip() == "":
                count1 = 0
                words.append(phrase)
                phrase = ""
                count+=1
            else:
                phrase += line
    return words, voice

def main():
    for num in range(10):
        c,voice = read()
        create(c, voice)
        print ("Done")

main()