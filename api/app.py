from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    with Image.open(r"C:\Users\payal\Downloads\Cheesecake.jpg") as img:
        resize = img.resize((1080,1080), Image.LANCZOS)
    return resize.show()

if __name__== "__main__":
    app.run(debug=True)
