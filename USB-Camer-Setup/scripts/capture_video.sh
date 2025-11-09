
#!/bin/bash
DEVICE=/dev/video0
OUTFILE=/root/video.mjpg
v4l2-ctl -d $DEVICE --set-fmt-video=width=1920,height=1080,pixelformat=MJPG
v4l2-ctl -d $DEVICE --stream-mmap --stream-count=300 --stream-to=$OUTFILE
echo "Video recorded at $OUTFILE"
