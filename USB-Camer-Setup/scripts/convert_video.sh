#!/bin/bash
ffmpeg -i video.mjpg -c:v libx264 -preset fast -crf 23 video.mp4
