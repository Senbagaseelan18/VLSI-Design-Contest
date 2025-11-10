from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <title>Live Camera Stream</title>
  <style>
    body { text-align: center; background: #111; color: white; font-family: Arial; }
    h1 { margin-top: 30px; }
    iframe { width: 80%; height: 600px; border: 3px solid #444; border-radius: 10px; }
  </style>
</head>
<body>
  <h1>🔴 Live USB Camera Stream</h1>
  <p>Camera is currently streaming...</p>
  <iframe src="/start" title="Camera Stream"></iframe>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/start')
def start_stream():
    cmd = ["v4l2-ctl", "--device=/dev/video0", "--stream-mmap", "--stream-count=0"]
    subprocess.Popen(cmd)
    return "Camera stream started. Press Ctrl+C to stop."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

