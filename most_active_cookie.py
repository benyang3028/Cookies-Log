import sys
import os
import collections

def getActiveCookies(file_name, criteria):
    '''
    returns the most frequent cookies based on criteria (-d)
    '''
    with open(file_name, 'r') as csv_file:
        cookie_dict = collections.defaultdict(int)
        curr_max = -1
        most_active = []
        next(csv_file) #skips header line
        for row in csv_file:
            cookie, timestamp = row.split(',')
            date, time = timestamp.split('T')
            if date == criteria:
                cookie_dict[cookie] += 1
                if cookie_dict[cookie] > curr_max:
                    most_active = [cookie]
                    curr_max = cookie_dict[cookie]
                elif most_active and cookie_dict[cookie] == curr_max:
                    most_active.append(cookie)
        for cookie in most_active:
            print(cookie)
        
def main():
    args = sys.argv
    args.pop(0) #remove name of python file
    if len(args) == 3:
        csv, param, criteria = args[0], args[1], args[2]
        if os.path.isfile('./' + csv): #checks if cookies log is in path
            getActiveCookies(csv, criteria)
    else:
        print("usage: most_active_cookie.py cookie_log.csv -d <date>")

if __name__=="__main__":
    main()
