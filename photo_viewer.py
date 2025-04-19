import os
import random
from flask import Flask, send_from_directory, jsonify, render_template_string

# Path to your image folder
PHOTO_DIR = r"C:\stephanieandreeseshower"

app = Flask(__name__)

def get_image_files():
    return [f for f in os.listdir(PHOTO_DIR)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Slideshow</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            background-color: black;
            overflow: hidden;
            height: 100%;
            width: 100%;
        }
        #slideshow {
            width: 100vw;
            height: 100vh;
            object-fit: contain;
            display: block;
        }
        #fullscreenBtn {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 999;
            padding: 10px 15px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 1px solid white;
            font-size: 16px;
            cursor: pointer;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <button id="fullscreenBtn" onclick="goFullscreen()">🔳 Fullscreen</button>
    <img id="slideshow" src="" alt="Slideshow">
    
    <script>
        let images = [];
        let index = 0;
        let wakeLock = null;

        async function fetchImages() {
            const response = await fetch('/list');
            images = await response.json();
            shuffle(images);
            showNextImage();
        }

        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        function showNextImage() {
            if (images.length === 0) return;

            const nextImageSrc = "/image/" + images[index];
            index = (index + 1) % images.length;

            const preloadImg = new Image();
            let timedOut = false;

            const failSafeTimeout = setTimeout(() => {
                timedOut = true;
                console.warn("Image load timed out, skipping:", nextImageSrc);
                showNextImage();
            }, 6000);

            preloadImg.onload = () => {
                if (timedOut) return;
                clearTimeout(failSafeTimeout);
                document.getElementById("slideshow").src = preloadImg.src;
                setTimeout(showNextImage, 5000);
            };

            preloadImg.onerror = () => {
                clearTimeout(failSafeTimeout);
                console.error("Failed to load:", nextImageSrc);
                showNextImage();
            };

            preloadImg.src = nextImageSrc;
        }

        function goFullscreen() {
            const elem = document.documentElement;
            if (elem.requestFullscreen) {
                elem.requestFullscreen();
            } else if (elem.webkitRequestFullscreen) {
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) {
                elem.msRequestFullscreen();
            }
        }

        // Wake Lock API to prevent screen from sleeping
        async function requestWakeLock() {
            try {
                if ('wakeLock' in navigator) {
                    wakeLock = await navigator.wakeLock.request('screen');
                    console.log('Wake Lock is active');

                    wakeLock.addEventListener('release', () => {
                        console.log('Wake Lock was released');
                        requestWakeLock();
                    });
                }
            } catch (err) {
                console.error(`${err.name}, ${err.message}`);
            }
        }

        document.addEventListener('visibilitychange', () => {
            if (wakeLock !== null && document.visibilityState === 'visible') {
                requestWakeLock();
            }
        });

        fetchImages();
        requestWakeLock();
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

@app.route('/list')
def list_images():
    images = get_image_files()
    return jsonify(images)

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory(PHOTO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
