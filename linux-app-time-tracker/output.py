import json

'''
Helper module used to output data as a JSON file and to print
in a table format in the terminal.
'''

class Output:
    def __init__(self):
        pass

    def write_to_json(self, dictx, out_file):
        # Convert and write JSON object to file
        with open(out_file, "w") as outfile: 
            json.dump(dictx, outfile)

    def print_as_table(self, dictx):
        # Print the names of the columns.
        print("{:<10} {:<10}".format('APP', 'TOTAL_TIME'))
 
        # print each data item.
        for key, value in dictx.items():
            print("{:<10} {:<10}".format(key, value))
