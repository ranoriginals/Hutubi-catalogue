import pandas as pd
import datetime
import os

csv_name = os.popen("ls ./*.csv").read().strip()

data = pd.read_csv(csv_name)
list_data = data.values.tolist()
jday_list = []

for i in range(len(list_data)):
    s = list_data[i][1].split()[0]
    jday = datetime.datetime.strptime(s,"%Y-%m-%d").timetuple().tm_yday
    jday_list.append(float(jday))


ten_day_num = []
target_filename = "fre_10_day_2010.txt"
target = open(target_filename,'w')

for i in range(0,37):
    time_start = i*10+1
    time_end = (i+1)*10+1
    count = 0
    for j in range(len(jday_list)):
        if time_start <= jday_list[j] < time_end:
            count = count+1
    str1 = str(i+1)+' '+str(count)+'\n'
    target.writelines(str1)

target.close()

