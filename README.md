# EPD-Emulator
EPD Emulator for simulating EPD (E-Paper Display) screens, useful for development and testing purposes. It supports both Tkinter and Flask for display rendering, and it can emulate color as well as monochrome displays.

![image](https://github.com/infinition/EPD-Emulator/assets/37984399/6006d07a-e760-46c8-9ded-731a590179f0)


## Features

- **Tkinter and Flask Support**: Choose between using a GUI window or a web server to render the simulated EPD screen.
- **Color and Monochrome**: Simulate both color and monochrome e-paper displays.
- **Configurable**: Easy to configure with JSON files for different EPD models.
- **Orientation**: Supports both normal and reverse orientation display modes.

## Installation

To use the EPD Emulator, you need to have Python installed on your system. Clone this repository to your local machine, and install the required dependencies:

```bash
git clone https://github.com/infinition/EPD-Emulator.git
cd Epd-Emulator
pip install -r requirements.txt


## Usage
To start using the emulator, you have to call it from another python file.
I have created a demo file to illustrate how to use it. (waveshare_emulator demo.py)

Run the waveshare_emulator demo.py script. You can specify the EPD type, color mode , rotation mode, TKINTER or flask and other options directly in the script.

python waveshare_emulator demo.py

For a demonstration of the emulator’s capabilities, run the waveshare_emulator_demo.py script.

python waveshare_emulator_demo.py

## Configuration

In waveshare_emulator demo.py, on the following line :
      line epd = epdemulator.EPD(config_file="epd2in13"........)

You can specify your type of EPD (I have created json files corresponding the differents EPD type.)

List of EPD : :

epd1in54
epd2in7
epd2ing
epd2in13
epd2in13v2
epd2in66
epd3in7
epd3in52
epd4in2
epd4in3
epd5in65
epd5in83
epd6in0
epd6in2
epd7in5
epd9in7
epd10in3
epd11in6
epd12in48

Change the values of the parameters as you want in the line epd = epdemulator.EPD() ......
        #config_file: the name of your EPD model
        #use_tkinter: True if you want to use Tkinter, False if you want to use Flask
        #use_color: True if you want to use color, False if you want to use monochrome
        #update_interval: the refresh delay in seconds wanted for the screen (Tkinter & Flask)
        #reverse_orientation: True if you want to reverse the orientation of the screen, False if you want to keep it as it is


## License
This project is licensed under the MIT License - see the LICENSE file for details.
