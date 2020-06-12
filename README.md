# Hutubi-catalogue

Hutubi Earthquake catalogue in 2010-2012

以43.5-44.5˚N, 86.5-87.5˚E为范围，获取2010、2011、2012全年的地震事件目录。

可在此网页查询相关地震目录的页数和条目数：http://data.earthquake.cn/datashare/report.shtml?PAGEID=earthquake_zhengshi

`2010`,`2011`,`2012`三个文件夹分别存放有各自的地震目录，基于2020/06/12-22:00的查询结果。

结果如下：

2010: 19页，374条结果

2011: 10页，184条结果

2012: 10页，195条结果

1. 201*-catalogue.py 用于爬取地震目录，会生成文件201*.csv

2. get_10_day_num.py 用于统计以10天为单位的地震频度，会生成文件fre_10_day_201*.txt

3. get_M3_event.py 用于筛选每年中震级大于3级的事件，并打印出对应的Julia Day

4. plot_2010-2012.sh 用于绘制地震频度随时间的关系，会生成2010-2012.ps && 2010-2012.pdf
