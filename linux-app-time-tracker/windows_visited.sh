#! /bin/bash

# Outputs window name (tab and app name) and the total time spent on that window

# A window is a description of the window a user was on.
# The format is: [Tab description] [Seperator] [App]
# ex: YouTube — Mozilla Firefox

# Does not work on Wayland, only Xorg
# Outputs on terminal and in file
# ex: Google News - Chromium	1509

readonly SLEEP_TIME=3
readonly OUTPUT_FILE="windows_visited_log.txt"

# Returns the tab description and the app name
function get_window_description() {
	echo $(xdotool getwindowfocus getwindowname)
}

function time_in_seconds() {
	echo $(date "+%s")
}

# Table header
function output_header() {
	header=$(echo -e "program_name\ttotal_time")
	echo "$header" > $OUTPUT_FILE
	output=$(echo -e "$1\t$2")
	echo "$output" >> $OUTPUT_FILE
	echo -e "program_name\ttotal_time"
	echo -e "$1\t$2"
}

function time_spent_on_window() {
	echo $(($1-$2))
}

function output_window_info() {
	output=$(echo -e "$1\t$2")
	echo "$output" >> $OUTPUT_FILE
	echo -e "$1\t$2"
}

function main() {
	# Setup the header and the first entry
	window_name=$(get_window_description)
	time=$(time_in_seconds)
	total_time=0
	output_header "$window_name" "$total_time"
	sleep $SLEEP_TIME;

	while true;
	do 
		curr_window_name=$(get_window_description)
		curr_time=$(time_in_seconds)

		if [ "$window_name" != "$curr_window_name" ];
		then
			total_time=$(time_spent_on_window "$curr_time" "$time")
			output_window_info "$window_name" "$total_time"
			window_name=$curr_window_name
			time=$curr_time
		fi
		sleep $SLEEP_TIME;
	done
}

main