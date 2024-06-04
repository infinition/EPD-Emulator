import json
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
from flask import Flask, render_template_string, send_file
import io
import threading
import webbrowser
import time
import os
import traceback

currentdir = os.path.dirname(os.path.realpath(__file__)) 

class EPD:
    def __init__(self, config_file="epd2in13", use_tkinter=False, use_color=False, update_interval=2, reverse_orientation=False): 
        config_path = os.path.join(currentdir, 'config', f'{config_file}.json')
        self.load_config(config_path)
        
        self.use_color = use_color  
        self.image_mode = 'RGB' if self.use_color else '1'  

        if reverse_orientation:
            self.width, self.height = self.height, self.width

        self.image = Image.new(self.image_mode, (self.width, self.height), 'white' if self.use_color else 255) 
        self.use_tkinter = use_tkinter
        self.update_interval = update_interval * 1000 if not use_tkinter else update_interval
        print(f"update_interval: {self.update_interval}")

        if self.use_tkinter:
            self.init_tkinter()
        else:
            self.init_flask()
            self.start_image_update_loop()

        self.draw = ImageDraw.Draw(self.image)


    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            self.width = config.get('width', 122)
            self.height = config.get('height', 250)
            self.color = config.get('color', 'white')
            self.text_color = config.get('text_color', 'black')


    def init_tkinter(self):
        self.root = tk.Tk()
        self.root.title(f"Waveshare {self.width}x{self.height} EPD Emulator")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
        self.update_tkinter()

    def update_tkinter(self):
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image)
        self.root.update()

        self.root.after(self.update_interval, self.update_tkinter)



    def init_flask(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return render_template_string(f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                        #screenImage {{
                            width: 50%;
                            height: auto;
                        }}
                    </style>
                    <script>
                        function updateImage() {{
                            var image = document.getElementById("screenImage");
                            image.src = "screen.png?t=" + new Date().getTime(); // Prevent caching
                        }}

                        setInterval(updateImage, {self.update_interval}); 
                    </script>
                </head>
                <body onload="updateImage()">
                    <img id="screenImage" src="screen.png" alt="EPD Emulator">
                </body>
                </html>
            ''')

        @self.app.route('/screen.png')
        def display_image():
            try:
                return send_file(os.path.join(os.path.dirname(__file__), 'screen.png'), mimetype='image/png')
            except Exception as e:
                traceback.print_exc()
                return "Internal Server Error", 500

        threading.Thread(target=self.run_flask).start()



    def run_flask(self):
        webbrowser.open("http://127.0.0.1:5000/")
        self.app.run(port=5000, debug=False, use_reloader=False)



    def update_image_bytes(self):
        self.image_bytes = io.BytesIO()
        self.image.save(self.image_bytes, format='PNG')
        self.image.save(os.path.join(os.path.dirname(__file__), 'screen.png'))  


    def start_image_update_loop(self):
        def update_loop():
            while True:
                self.update_image_bytes()
                time.sleep(self.update_interval)

        threading.Thread(target=update_loop, daemon=True).start()


    def init(self):
        print("EPD initialized")

    def Clear(self, color):
        self.image = Image.new(self.image_mode, (self.width, self.height), "white")
        self.draw = ImageDraw.Draw(self.image)  
        self.display(self.getbuffer(self.image))
        print("Screen cleared")

    def display(self, image_buffer):
        if self.use_tkinter:
            self.tk_image = ImageTk.PhotoImage(self.image)  
            self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image)  
            self.root.update()  
        else:
            self.update_image_bytes()


    def displayPartial(self, image_buffer):
        self.display(image_buffer)


    def get_frame_buffer(self, draw):
        return self.getbuffer(self.image)

    def getbuffer(self, image):
        return image.tobytes()

    def sleep(self):
        print("EPD sleep")

    def Dev_exit(self):
        print("EPD exit")
        if self.use_tkinter:
            self.root.destroy()

    def get_draw_object(self):
        return ImageDraw.Draw(self.image)

    def draw_text(self, position, text, font, fill):
        self.draw.text(position, text, font=font, fill=fill)
        self.display(self.getbuffer(self.image))

    def draw_rectangle(self, xy, outline=None, fill=None):
        self.draw.rectangle(xy, outline=outline, fill=fill)
        self.display(self.getbuffer(self.image))

    def draw_line(self, xy, fill=None, width=0):
        self.draw.line(xy, fill=fill, width=width)
        self.display(self.getbuffer(self.image))

    def draw_ellipse(self, xy, outline=None, fill=None):
        self.draw.ellipse(xy, outline=outline, fill=fill)
        self.display(self.getbuffer(self.image))

    def paste_image(self, image, box=None, mask=None):
        self.image.paste(image, box, mask)
        self.display(self.getbuffer(self.image))

