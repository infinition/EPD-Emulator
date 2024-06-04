from epd_emulator import epdemulator 
from PIL import Image, ImageFont
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__)) #Current directory path
refreshdelay = 5 #Refresh delay in seconds wanted for the screen (Tkinter & Flask)

#Initializating the emulator
    #Change the values of the parameters as you want in the ligne epd = epdemulator.EPD() ......
        #config_file: the name of your EPD model
        #use_tkinter: True if you want to use Tkinter, False if you want to use Flask
        #use_color: True if you want to use color, False if you want to use monochrome
        #update_interval: the refresh delay in seconds wanted for the screen (Tkinter & Flask)
        #reverse_orientation: True if you want to reverse the orientation of the screen, False if you want to keep it as it is

epd = epdemulator.EPD(config_file="epd2in13", use_tkinter=False, use_color=True, update_interval=refreshdelay, reverse_orientation=False)
epd.init()
epd.Clear(255)  # Ensure that the screen is blank at the beginning
width, height = epd.width, epd.height #Define the width and height of the screen (in pixels)to use it later


#Folder paths
picdir = os.path.join(current_dir, 'images')
fontdir = os.path.join(current_dir, 'fonts')

#Load the fonts
font = ImageFont.truetype(os.path.join(fontdir, 'Arial.ttf'), 11)

#Load the image
image1 = Image.open(os.path.join(picdir, 'bjorn.bmp'))
image2 = Image.open(os.path.join(picdir, 'bjorn1.bmp'))

#Resize the image
new_width1, new_height1 = int(image1.width * 0.75), int(image1.height * 0.75)
image1 = image1.resize((new_width1, new_height1))
new_width2, new_height2 = int(image2.width * 0.75), int(image2.height * 0.75)
image2 = image2.resize((new_width2, new_height2))

#Center the image
x_center1 = (width - new_width1) // 2
y_bottom1 = height - new_height1

x_center2 = (width - new_width2) // 2
y_bottom2 = height - new_height2

    
show_first_image = True #Boolean to switch between the two images

while True:
        draw = epd.draw #Create a draw object
        draw.text((40, 5), "Emulator", font=font, fill=0) #Draw a text
        draw.rectangle((1, 1, width -1 , height -1 ), outline=0) #Draw a rectangle
        draw.line((1, 20, width - 1, 20), fill=0) #Draw a line
        if show_first_image:
            epd.paste_image(image1, (x_center1, y_bottom1 - 1))
        else:
            epd.paste_image(image2, (x_center1, y_bottom1 - 1))
        show_first_image = not show_first_image #Switch between the two images

        image_buffer = epd.get_frame_buffer(draw) #Get the frame buffer
        epd.display(image_buffer) #Display the frame buffer

        time.sleep(refreshdelay) #Wait for the refresh delay



