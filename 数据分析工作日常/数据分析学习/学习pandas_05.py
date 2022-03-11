import pandas as pd
pd.set_option("expand_frame_repr", False)
df = pd.read_csv("a_stock_201903.csv", encoding="gbk", parse_dates=["交易日期"])

"""
①时间处理
    pd.to_datetime()，给定一个时间字符串，智能识别出日期，但不能识别中文
    df[].dt.year/month/week/day/hour/minute/second，返回年月周日时分秒，注意原日期数据需要先parse_dates序列化
    df[].dt.dayofyear/dayofweek/weekday/day_name()，前者是返回一年的第几天，后两个都是返回一周的第几天，最后是星期几
    df[].dt.days_in_month，查询这一天所在的月份有多少天
    df[].dt.is_month_start/is_month_end，查询这一天是否是本月的第一天/最后一天
    df[] + pd.Timedelta(days=1)，增加一天，也可以增加周，时，分，秒，参数都是复数形式，加不了年和月
"""
print(pd.to_datetime("200510261223"))
print(df)
print(df["交易日期"].dt.second)
print(df["交易日期"].dt.day_name())
print(df["交易日期"].dt.days_in_month)
print(df["交易日期"].dt.is_month_start)
print(df["交易日期"] + pd.Timedelta(days=1))
print(df["交易日期"] + pd.Timedelta(seconds=10))
"""
②滚动操作
    df[].rolling(3).mean()，意思就是将每行数据与上面两行数据计算三行数据的平均值，向上寻找
    df[].rolling(3).max()/min()/std()，与上行同理，可以接各种函数计算
    df[].expanding().mean()，每一行数据与以上所有数据进行一个平均值计算，滚动累计的操作
    df.to_csv/to_excel/to_dict，将dataframe数据输出csv文件/excel文件/字典
"""
df["收盘价_三天均值"] = df["收盘价"].rolling(3).mean()
print(df[["收盘价", "收盘价_三天均值"]])
df["收盘价_三天最大值"] = df["收盘价"].rolling(3).max()
print(df[["收盘价", "收盘价_三天最大值"]])
df["收盘价_至今均值"] = df["收盘价"].expanding().mean()
print(df[["收盘价", "收盘价_至今均值"]])
