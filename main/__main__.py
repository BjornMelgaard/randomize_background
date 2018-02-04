import os
import glob
import subprocess
import time
import random
import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='+', help='Path of a file or a folder of files.')
args = parser.parse_args()

# Parse paths
full_paths = [os.path.join(os.getcwd(), path) for path in args.path]

images = full_paths

first = images[0]

delay = 2

while True:
    #randomize the order.
    #Ensure that we don't have the same first element as the last element.
    while first== images[0]:
        random.shuffle(images)

    for image in images:
        feh = subprocess.Popen(['feh', '--bg-fill', image])
        time.sleep(delay * 60)

        #record the last image.
        first = image

        #be a nice guy.
        feh.terminate()
    random.shuffle(images)
