"""
①set_option()学习
    "expand_frame_repr"：设定dataframe数据显示的规则，为False时不忽略中间的列，完整展示
    pd.options.display.precision = 1：规定数据的浮点数精度为1
"""
import pandas as pd
pd.set_option("expand_frame_repr", False)
pd.options.display.precision = 1
"""
②read_csv()学习
    names与header的结合用法：如果不满意原来的表头，我们可以通过names重新定义表头，然后header=0进行覆盖
    encoding参数：如果是含有中文字符的csv文件，需要将指定gbk编码
    sep参数：代表数据的分隔符，默认值是英文逗号，其他常见的有'\t'
    skiprows参数：跳过前n行的数据，n+1行作为表头，也就是说表头在计数范围
    nrows参数：除去表头，只读取前n行的数据，默认是全部读取，注意，表头不在计数范围内
    usecols参数：读取指定的这几列数据，其他列数据不读
    parse_dates参数，将指定列的数据从字符串识别为日期格式
    error_bad_lines参数：设定为False时，遇到有问题的行数据直接跳过
    na_values参数：碰到NULL数据设定为空值
    index_col参数：默认是从0开始做索引，可以指定交易日期为索引
"""
df = pd.read_csv("sh600000.csv", encoding="gbk", sep=",", nrows=2,
                 parse_dates=["交易日期"], usecols=["股票名称", "交易日期", "开盘价", "收盘价"],
                 index_col=["交易日期"])
print(df)
"""
③查看dataframe数据
    df.shape：输出多少行多少列，注意是不包含表头和指定的索引列
    df.shape[0]、df.shape[1]：输出行的数量或列的数量
    df.columns：输出每一列的名字，表头的名字，可for循环
    df.index：输出每一行的名字，索引的名字，可for循环
    df.head()、df.tail()：看前n行数据和后n行数据，默认是5，忽略表头
    df.sample(n=3)：随机抽取n行数据
    df.describe()：直观感受数据
    
"""
print(df.shape, df.shape[0], df.shape[1])
print(df.columns, df.index)
print(df.head(1), df.tail(1))
print(df.sample(1))
print(df.describe())
"""
④读取dataframe指定的数据
    列表访问：如果要访问两个列的数据，需要传递列表参数
    df.loc[]操作：通过index和columns来访问数据，也可以用切片的方式指定范围
    df.iloc[]操作：通过行号列号来来访问数据
    df.at[]、df.iat[]：如果只找一个指定的数据，这个更加高效些,前者填index和columns参数，后者行号列号
"""
df1 = pd.read_csv("sh600000.csv", encoding="gbk", index_col=["交易日期"])
print(df1[["开盘价", "收盘价"]])
print(df1.loc["1999-11-10", "开盘价"])
print(df1.loc["1999-11-12":"1999-11-16", "开盘价":"收盘价"])
print(df1.iloc[2:5, 2:6])
print(df1.at["1999-11-10", "开盘价"], df1.iat[1,6])
