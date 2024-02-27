import constants
import app_time_tracking as att
import output

'''
Uses the log file to output the time spent on each app.
Outputs the data on the terminal in a table format and to a JSON file.

App names must be manually inserted into the constants.py file.

A window is a description of the window a user was on.
The format is: [Tab description] [Seperator] [App]
ex: YouTube — Mozilla Firefox
'''

def main():
    # Get the windows visited and their times
    tracking = att.AppTimeTracking()
    window_info = tracking.get_window_info(constants.INPUT_LOG)

    # Pair the apps with the time spent on them
    app_time_dict = tracking.get_app_with_time(constants.APP_NAMES, window_info)

    out = output.Output()
    out.write_to_json(app_time_dict, constants.OUTPUT_JSON)
    out.print_as_table(app_time_dict)

if __name__ == "__main__":
    main()
