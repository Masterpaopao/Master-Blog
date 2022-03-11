import pandas as pd
pd.set_option("expand_frame_repr", False)
df = pd.read_csv("sh600000.csv", encoding="gbk", nrows=200)
"""
①dataframe数据的列操作
    根据数据的类型，可以进行加减乘除操作
    用赋值的方式可以新增一个列
    mean()：求一整列的平均值，返回一个值，会自动排除空值；如果是多列，传递列表参数
    mean()中axis参数：对两列数据中的每一行求平均值
    max()、min()、std()、median()、quantile(0.5)：最大值、最小值、标准差、中位数、25%分位数
    count()：非空的数据量
    del：删除某一列
    drop(["详细交易日期"], axis=1)：删除某一列的另一种方式，但是不影响df本身，建议带上inplace=True参数，自动代替原df
    cumsum()、cumprod(): 累加值、累乘值
    value_counts()：元素相同值的个数，只能print()直接打印
"""
print(df["交易日期"] + "15:00:00")
print(df["收盘价"] * df["成交量"])
df["详细交易日期"] = df["交易日期"] + " 15:00:00"
df["交易所"] = "上交所"
print(df[["开盘价", "收盘价"]].mean())
print(df[["开盘价", "收盘价"]].mean(axis=1))
print(df["开盘价"].max(), df["开盘价"].min(), df["开盘价"].std(), df["开盘价"].median(), df["开盘价"].quantile(0.25))
print(df["开盘价"].count())
del df["交易所"]
df.drop(["详细交易日期"], axis=1, inplace=True)
print(df)
df["累计成交量"] = df["成交量"].cumsum()
print(df[["成交量", "累计成交量"]])
"""
②比较函数
    shift(-1)：删除首行数值，剩余数据向上挪动，会导致最后一个数值为NaN空值
    shift(1)：删除尾行数值，剩余数据向下挪动，会导致第一个数值为NaN空值
    diff(-1)：将本行数据对比下行数据得到差值，会导致最后一个数值为NaN空值
    diff(1)：将本行数据对比上行数据得到差值，会导致第一个数值为NaN空值
    pct_change(1): 将本行数据对比上行数据得到百分比差值，会导致第一个数值为NaN空值
    rank()：排名函数，参数ascending代表排序方式，参数pct为True时按百分比排名
"""
df["下周期开盘价"] = df["开盘价"].shift(-1)
print(df[["开盘价", "下周期开盘价"]])
df["涨跌"] = df["收盘价"].diff(1)
print(df[["收盘价", "涨跌"]])
df["涨跌幅"] = df["收盘价"].pct_change(1)
print(df[["收盘价", "涨跌幅"]])
df["涨跌排名"] = df["涨跌"].rank(ascending=False, pct=False)
print(df[["收盘价", "涨跌", "涨跌排名"]])
print(df["开盘价"].value_counts())