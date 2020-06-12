import pandas as pd
import datetime


def print_event(csv_name):
    data = pd.read_csv(csv_name)
    list_data = data.values.tolist()
    threshold = 3
    for i in range(len(list_data)):
        event_info = list_data[i]
        time = event_info[1].split()[0]
        mag = event_info[5]
        if mag >= threshold:
            jday = datetime.datetime.strptime(time,"%Y-%m-%d").timetuple().tm_yday
            print(csv_name,jday)

csv_name = "./2010/2010.csv"
print_event(csv_name)
csv_name = "./2011/2011.csv"
print_event(csv_name)
csv_name = "./2012/2012.csv"
print_event(csv_name)
