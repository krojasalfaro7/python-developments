import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

camera = cv2.VideoCapture(2)

app = FastAPI()

async def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.get("/")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace;boundary=frame")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9000, access_log=False)