'''
Parses the log file and returns the {app : time in seconds} pair.
Ex: {"firefox":280}
'''

class AppTimeTracking:
    def file_as_list(self, file) -> list:
        flist = []
        with open(file, "r+") as f:
            flist = f.readlines()
        return flist

    def get_app_with_time(self, app_names, window_info) -> dict:
        '''
        Returns the app names with the time spent on each of them in seconds.
        '''
        app_dict = dict.fromkeys(app_names)
        for key in app_dict:
            app_dict[key] = {}
        window_names = window_info[0]
        window_times = window_info[1]

        for app_name in app_dict:
            total_time = 0
            for i in range(len(window_names)):
                if app_name in window_names[i]:
                    total_time = total_time + window_times[i]
            app_dict[app_name] = total_time
        return app_dict


    def get_window_info(self, log_file) -> list:
        '''
        Parses the log file.
        Returns an the windows visited and the time spent on each.
        '''
        window_file = self.file_as_list(log_file)
        window_names = []
        window_times = []
        window_info = []
        window_file.pop(0)
        for window in window_file:
            temp = window.split("\t")
            time = temp[1].split()
            time = int(time[0])
            window_times.append(time)
            window_names.append(temp[0].lower())
        window_info.append(window_names)
        window_info.append(window_times)
        return window_info
