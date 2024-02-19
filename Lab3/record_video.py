"""
Script for recording a video using the PiCam library,
for later post-processing and extraction of pulse signals
for the optics lab in the TTT4280 course.

Run without arguments to see the usage instructions.

This script was mainly written by Jon Magnus Momrak Haug and Martin Ervik in
preparation for the optics lab in TTT4280 in 2017.

Small modifications made by Asgeir Bjorgan in 2018 (add CLI arguments, change
MP4Box arguments to overwrite the container instead of adding to it, avoiding
the need for removing the previous output file).
"""

import subprocess
import os
from picamera import PiCamera
from time import sleep
import sys

# Print usage instructions
if len(sys.argv) < 2:
        print('Usage: python ' + sys.argv[0] + ' [path to filename]')
        print('')
        example_path = 'some/path/to/a/folder/optics_labs/videos/'
        example_filename = 'finger_kurt-leif_transillumination'
        print('Example: `python ' + sys.argv[0] + ' ' + example_path + example_filename + '`')
        print('(The example will result in two files, ' + example_filename + '.h264 and ' + example_filename + '.mp4)')
        exit()

# Split the root from the extension, ensure correct output file extension
DEFAULT_FILE_EXTENSION = '.h264'
root, extension = os.path.splitext(sys.argv[1])
if extension != DEFAULT_FILE_EXTENSION:
        extension = DEFAULT_FILE_EXTENSION
h264_filename = root + extension

# PiCamera instance. This is an object which has several attributes that can be changed.
camera = PiCamera()

# The resolution can be changed, but the frame rate has to be supported by the
# current resolution.
camera.resolution = (1640, 922)
camera.framerate = 40

# Set a low ISO. Adjusts the sensitivity of the camera. 0 means auto. 10 most probably is the same
# as 100, as picamera doc says it can only be set to 100, 200, 300, ..., 800.
# Might probably want to set this to lowest possible value not equal to 0, but can also be tuned.
camera.iso = 10

# Add a bit of delay here so that the camera has time to adjust its settings.
# Skipping this will set a very low exposure and yield black frames, since the
# camera needs to adjust the exposure to a high level according to current
# light settings before turning off exposure compensation.
print('Waiting for settings to adjust')
sleep(2)

# switch these two off so that we can manually control the awb_gains
camera.exposure_mode = 'off'
camera.awb_mode = 'off'

# Set gain for red and blue channel.  Setting a single number (i.e.
# camera.awb_gains = 1) sets the same gain for all channels, but 1 seems to be
# too low for blue channel (frames constant black).  2 sometimes is not enough,
# and is related to what happens during the sleep(2) above.  Probably has to be
# tuned?
camera.awb_gains = (1, 2)

# Other parameters that could be tuned:
#
# * camera.exposure_compensation (should have been set to a sensible value while camera was sleeping? Might want to fix this for reproducable results)
# * camera.brightness
#
# See https://picamera.readthedocs.io/en/release-1.10/api_camera.html for description of properties,
# and inspiration for other properties to adjust.

# how long we want to record
recordTime = 30

# If we were not running the Pi headless, starting the preview would show us
# what the camera was capturing.  Now, since we run it headless, it allows the
# rest of the settings to be set.
print("Waiting for white balance to adjust")
camera.start_preview()
sleep(5)
print("Start recording to " + h264_filename)
camera.start_recording(h264_filename)

# Record for the amount of time we want
camera.wait_recording(recordTime)

# When finished, stop recording and stop preview.
camera.stop_recording()

print("Recording finished")
camera.stop_preview()

###########################################################################
## The following section is where we wrap the .h264 into a mp4 container ##
###########################################################################

# .h264 doesn't containing any information about the framerate or duration of the movie.
#
# We therefore have to wrap a container around the movie and supply this information manually.
# This can be done using the application MP4Box, e.g. `MP4Box -new -fps [fps] -add [filename.h264] [output_filename.mp4].
# We do this automatically by executing MP4Box externally from the Python script (it is not good practice to execute
# external programs like this, but we'll do it anyway.)
#
# Overview over CLI flags:
# * -fps: Set frames per second as according to the recorded fps
# * -new: Force overwrite of .mp4-file (instead of adding clip to it)
# * -add: Add clip in .h264-file to .mp4-file
print("Pack video in MP4 container")
mp4_filename = root + ".mp4"
subprocess.check_output(["ffmpeg", "-framerate", str(camera.framerate), "-i", h264_filename, "-c", "copy", mp4_filename])
print("Files saved to: " + h264_filename + " and " + mp4_filename)
