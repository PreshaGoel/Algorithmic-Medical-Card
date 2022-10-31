from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('new.html', showCamera = 1)

cap = cv2.VideoCapture(0)

def genertae():
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imwrite("static/image.jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('static/image.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response (genertae(), mimetype='multipart/x-mixed-replace; boundary=frame' )

@app.route('/imaag')
def showImage():
    return render_template('new.html', showCamera=0)



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)