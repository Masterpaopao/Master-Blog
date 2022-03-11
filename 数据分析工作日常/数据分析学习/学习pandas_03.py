import pandas as pd
pd.set_option("expand_frame_repr", False)
df = pd.read_csv("a_stock_201903.csv", encoding="gbk")
"""
①数据筛选9
    用判等==去逐行判断是否符合要求，返回True或False
    想要过滤出符合条件的行数据，将条件放进df索引列表里面即可
    如果要过滤出符合多个条件的数据需要使用isin方法，参数传列表
    也可以用> >= < <= 过滤数据，也可以用&和|进行与或操作，需要双方括起来
"""
print(df["股票代码"] == "sh600000")
print(df[df["股票代码"] == "sh600000"])
print(df[df["股票代码"].isin(["sh600000", "sz000001"])])
print(df[(df["开盘价"] >= 11.56) & (df["收盘价"] >= 11.55)])
"""
②空缺值处理
    df.dropna(how="any")，将带有空值的行删掉
    df.dropna(subset=["月头","开盘价"], how="all")，all表示只有月头和开盘价都为空值的时候才删掉
    df.fillna(value=0)，将空值赋值为固定的值
    df.fillna(method="ffill")，向上寻找最近的一个非空值，以该值来填充
    df.fillna(method="bfill")，向下寻找最近的一个非空值，以该值来填充
    df.notnull()、df.isnull()，对所有数据判断是否为空值，返回True或False，放df列表索引里过滤
"""
# 创建一个列叫月头，指定数据为2019-03-01时写入进去2019-03-01
index = df[df["交易日期"] == "2019-03-01"].index
df.loc[index, "月头"] = df["交易日期"]
# 我们可以看到df数据，被过滤掉的数据行里月头的值为NaN出现了空值，所以需要处理
print(df.dropna(how="any"))
print(df.dropna(subset=["月头", "开盘价"], how="all"))
print(df.fillna(value=0))
print(df["月头"].fillna(value="N"))
print(df.fillna(method="ffill"))
print(df.fillna(method="bfill"))
print(df[df["月头"].notnull()])
print(df[df["月头"].isnull()])
