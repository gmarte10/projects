# App Time Tracker

This is a small person project I made used to track the amount of time spent on an app on
a linux machine.

## Installation

Download and extract the project from github

## Usage

Switch to [Xorg] (https://helpdesk.psionline.com/hc/en-gb/articles/13470827149332-How-to-perform-the-switch-from-the-Wayland-display-server-to-Xorg-X11-on-Linux-Ubuntu-22-04-LTS).

Make the windows_visited.sh executable

```bash
chmod u+x windows_visited.sh
```

Run the bash file to start tracking app time

```bash
./windows_visited.sh
```

Current apps being tracked are 3 browsers (Firefox, Chrome and Opera).
To add more apps, add the last word of their name in lowercase to
the APP_NAMES array in constants.py. Use the output from the bash file
to get the correct name.

Ex: README.md - deploy - Visual Studio Code 6

Insert "code" into the APP_NAMES array to track and display the total
time spent on visual studio code.

Run main.py to display the total time for each app

```bash
./python3 main.py
```
