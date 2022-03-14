# 需求：给定csv文件，找出每隔三年的最高价，以及最低价或者低于最高价的1/4的数据
import os
import pandas as pd
from dateutil.relativedelta import relativedelta

# pandas配置项
pd.set_option("expand_frame_repr", False)
pd.options.display.precision = 4


def calculate_date(date, amount):
    """
    功能：
        rolling专用函数，根据时间字符串，找到三年前的时间，并在df数据中统计间隔的数据数量
    参数：
        date - 时间字符串
        amount - 最低的数据滚动量
    返回：
        days - 间隔的天数
    """
    if df[df["trade_date"] == date].index[0] + 1 < amount:
        return amount
    else:
        # 求出当前数据的index
        now_index = df[df["trade_date"] == date].index[0]
        # 求出此数据的三年前时间
        past_date = (df.iat[now_index, 0] - relativedelta(years=3)).strftime("%Y%m%d")
        # 但是不能确定这个日期会在表格中存在，所以预设向后顺延的可能
        while True:
            if df[df["trade_date"] == past_date].empty:
                past_date = (pd.to_datetime(start_date) + relativedelta(days=1)).strftime("%Y%m%d")
            else:
                break
        # 返回两条数据间隔的数据量，用于rolling
        return now_index - df[df["trade_date"] == past_date].index[0] + 1


if __name__ == '__main__':

    # 首先在给定的csv文件里面，将每一条数据rolling滚动近三年的数据比较计算
    df = pd.read_csv("csv/data.csv",
                     names=["index", "trade_date", "price"],
                     header=0, index_col=["index"],
                     parse_dates=["trade_date"])
    # 进行年计算需要安装专用模块，pip install python-dateutil
    # 先找到滚动数据的起点，即第一条数据的三年后
    start_date = (df.iat[0, 0] + relativedelta(years=3)).strftime("%Y%m%d")
    # 但是不能确定这个日期会在表格中存在，所以预设向后顺延的可能
    while True:
        if df[df["trade_date"] == start_date].empty:
            start_date = (pd.to_datetime(start_date) + relativedelta(days=1)).strftime("%Y%m%d")
            continue
        else:
            break
    # 获取此条滚动数据的index，找到df里滚动的起点，别忘了可以滚动的数据是结果+1，因为index从0开始
    start_index = df[df["trade_date"] == start_date].index[0]
    # 在每一次滚动里，找到近三年的最高价和最低价，设置为另外两个列，利用rolling配合自写过滤函数
    df["year_3_min"] = df["price"].rolling(calculate_date(df["trade_date"], start_index + 1)).min()
    df["year_3_max"] = df["price"].rolling(calculate_date(df["trade_date"], start_index + 1)).max()
    # 对于每条数据，计算近三年最高价的四分之一线，设置为另外一个列
    df["year_3_max_1_4"] = 0.25 * df["year_3_max"]
    # 把trade_date类型的数据转化为字符串形式，以便于设为折线图的横坐标
    df["trade_date"] = df["trade_date"].astype(str)
    # 花费了半天终于掌握如何在已有的列中根据条件去生成新的一列，公式为df.loc[条件，要生成的新列名] = 需要的赋值
    df.loc[df["year_3_min"] == df["price"], "is_year_3_min"] = df["price"]
    df.loc[df["year_3_max"] == df["price"], "is_year_3_max"] = df["price"]
    df.loc[df["year_3_max_1_4"] > df["price"], "is_year_3_max_1_4_hold"] = df["price"]
    # 将所有的空值处理成'-'，以配合折线图自动忽略'-'，而不需要花里胡哨地去过滤空值
    df.fillna(value='-', inplace=True)
    # 将df数据输出成csv文件
    df.to_csv("csv/result.csv", index=False)
    # 再生成json文件传送给前端，记录一下这儿卡时间很久的原因
    df.to_json("html/json/result.json")
    # 开启Python服务器端口，内置模块
    os.system("cd html  && python -m http.server")

