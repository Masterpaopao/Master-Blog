# 给定csv文件，找出每隔三年的最高价，以及最低价或者低于最高价的1/4的数据
import pandas as pd
from dateutil.relativedelta import relativedelta
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
                continue
            else:
                break
        # 返回两条数据间隔的数据量，用于rolling
        return now_index - df[df["trade_date"] == past_date].index[0] + 1


if __name__ == '__main__':

    # 首先在给定的csv文件里面，将每一条数据rolling滚动近三年的数据比较计算
    df = pd.read_csv("寻找趋势线.csv",
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
    # 在每一次滚动里，找到近三年的最高价和最低价，设置为另外两个列
    df["year_3_min"], df["year_3_max"] = df["price"].rolling(calculate_date(df["trade_date"], start_index + 1)).min(), \
                df["price"].rolling(calculate_date(df["trade_date"], start_index + 1)).max()
    # 如果本条数据就是近三年的最高价或最低价，则标记为1，设置为另外两个列
    df["is_year_3_min"], df["is_year_3_max"] = (df["price"] == df["year_3_min"]).astype(int), (
                df["price"] == df["year_3_max"]).astype(int)
    # 如果本条数据低于近三年最高价的四分之一的价格，则标记为1，设置为另外一个列
    df["is_year_3_min_1_4_hold"] = (df["price"] < 0.25 * df["year_3_max"]).astype(int)
    # 将df数据输出成文件
    df.to_csv("result.csv")
