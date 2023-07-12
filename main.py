from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import numpy as np
import random
import os

def resize_image_to_1080_width(image_path):
    # Load the image
    image = Image.open(image_path)

    # Get the current width and height
    width, height = image.size

    if image.mode == 'RGBA':
        image = image.convert('RGB')

    if width != 1080:
        # Calculate the scaling factor
        scaling_factor = 1080 / width

        # Calculate the new width and height
        new_width = 1080
        new_height = int(height * scaling_factor)

        # Resize the image
        resized_image = image.resize((new_width, new_height))

        # Save the resized image or overwrite the original image
        resized_image.save(image_path)
        print(f"Image resized to {new_width}x{new_height} pixels.")
    else:
        print("Image width is already 1080 pixels. No resizing needed.")
def paste_image_on_black_background(image_path):
    # Load the image to be pasted
    image_to_paste = Image.open(image_path)

    # Create a new black background image with dimensions 1080x1920
    background = Image.new('RGB', (1080, 1920), color='black')

    # Calculate the coordinates to paste the image in the center
    x = (background.width - image_to_paste.width) // 2
    y = (background.height - image_to_paste.height) // 2

    # Paste the image onto the black background
    background.paste(image_to_paste, (x, y))

    # Save the final image
    background.save(image_path)
def create(w1,w2,w3,p1,p2,e1,e2):
   
    a = os.listdir("Image/"+p1+"/"+e1+"/")
    file = "Image/"+p1+"/"+e1+"/"+random.choice(a)
    a = os.listdir("Image/"+p2+"/"+e2+"/")
    file2 = "Image/"+p2+"/"+e2+"/"+random.choice(a)
    a = os.listdir("Image/NO")
    file3 = "Image/NO/"+random.choice(a)
    print(file)
    print(file2)
    print(file3)

    resize_image_to_1080_width(file)
    resize_image_to_1080_width(file2)
    paste_image_on_black_background(file)
    paste_image_on_black_background(file2)

    text1 = random.choice(w1)
    text2 = random.choice(w2)
    text3 = random.choice(w3)


    count1 = 0

    img = Image.open(file)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('Font.otf', 55)
    x, y = 40, 480
    shadowColor = (0, 0, 0)
    thickness = 4
    I1.text((x - thickness, y - thickness), text1, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x + thickness, y - thickness), text1, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x - thickness, y + thickness), text1, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x + thickness, y + thickness), text1, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((40,480), text1, font=myFont, fill =(255, 255, 255))
    img.save("2Images/images/"+str(0)+".png")

    img = Image.open(file2)
    I1 = ImageDraw.Draw(img)
    x, y = 40, 480
    shadowColor = (0, 0, 0)
    thickness = 4
    I1.text((x - thickness, y - thickness), text2, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x + thickness, y - thickness), text2, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x - thickness, y + thickness), text2, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((x + thickness, y + thickness), text2, font=myFont, fill=shadowColor, thick=thickness)
    I1.text((40,480), text2, font=myFont, fill =(255, 255, 255))
    img.save("2Images/images/"+str(1)+".png")
def video(num,p3):

    image_paths = ["2Images/images/0.png", "2Images/images/1.png"]
    video_path = "Videos/"+p3+"/"+random.choice(os.listdir("Videos/"+p3))
    output_path = "FinalVideos/output"+str(num)+".mp4"

    # Load video clip
    video = VideoFileClip(video_path)

    # Extract audio from the original video
    audio = video.audio

    # Define image duration (in seconds)
    image_duration = 3

    # Create a list to store the clips
    clips = []

    # Iterate over image paths and add them on top of the video for the specified duration
    for image_path in image_paths:
        image = ImageClip(image_path)
        image = image.set_duration(image_duration).resize(height=video.h)
        clips.append(image.set_audio(audio))
        video = video.subclip(image_duration)

    # Add the remaining portion of the original video to the composite
    clips.append(video.set_audio(audio))

    # Concatenate the clips into the composite video
    composite_video = concatenate_videoclips(clips)

    # Set the final duration of the composite video
    composite_video = composite_video.set_duration(composite_video.duration)

    # Set the audio of the composite video
    composite_video = composite_video.set_audio(audio)

    # Save the composite video to the output path
    composite_video.write_videofile(output_path, codec="libx264")
def read(e1, e2):
    words1 = []
    words2 = []
    words3 = []
    phrase = ""
    count = 0
    voice = 0
    file_path1 = '2images/'+e1+'.txt'  
    file_path2 = '2images/'+e2+'.txt'  
    file_path3 = '2images/Sad.txt'
    # image1
    with open(file_path1, 'r') as file:
        for line in file:
            if line.strip() == "":
                count1 = 0
                words1.append(phrase)
                phrase = ""
                count+=1
            else:
                phrase += line
    # image2
    with open(file_path2, 'r') as file:
        for line in file:
            if line.strip() == "":
                count1 = 0
                words2.append(phrase)
                phrase = ""
                count+=1
            else:
                phrase += line
    # image3
    with open(file_path3, 'r') as file:
        for line in file:
            if line.strip() == "":
                count1 = 0
                words3.append(phrase)
                phrase = ""
                count+=1
            else:
                phrase += line
    return words1,words2,words3
def main():
    p1 = "Krabs"
    p2 = "Spongebob"
    p3 = "Plankton"
    e1 = "Happy"
    e2 = "Scared"
    w1,w2,w3 = read(e1,e2)
    for num in range(20):
        create(w1,w2,w3,p1,p2,e1,e2)
        video(num,p3)
main()