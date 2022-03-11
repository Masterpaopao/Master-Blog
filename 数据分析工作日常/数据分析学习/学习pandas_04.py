import pandas as pd
pd.set_option("expand_frame_repr", False)
df = pd.read_csv("a_stock_201903.csv", encoding="gbk")

"""
①dataframe数据整理
    df.sort_values()，根据列值排序，by是排序项，ascending是0和1选择逆序还是顺序，传列表参数
    df.append()，合并操作，ignore_index参数为True时忽略各自原来的索引
    df.drop_duplicates()，去重操作，subset参数指定需要比对的列，keep是去除重复行的时候保留first,last,False，还有inplace
    df.reset_index()，在上面的数据中重新排序索引，drop为True时删除掉各自原来的索引，还有inplace
    df.rename(columns={"开盘价":"割韭菜价"})，修改表头，以字典的形式修改表头名字
    df.empty、df.T：前者是判断df数据是否为空，返回布尔值；后者是df数据转置
"""
print(df.sort_values(by=["交易日期", "开盘价"], ascending=[0, 0]))
df1 = df.iloc[0:10][["股票名称", "交易日期", "开盘价"]]
df2 = df.iloc[5:15][["股票名称", "交易日期", "开盘价"]]
df3 = df1.append(df2, ignore_index=True)
print(df3.drop_duplicates(subset=["开盘价"], keep="first", inplace=True))
print(df3)
print(df3.reset_index(drop=True, inplace=True))
print(df3.rename(columns={"开盘价": "割韭菜价"}))
print(pd.DataFrame().empty, df3.empty)
print(df3.T)
"""
②字符串操作
    df[].str[:2]，切片操作
    df[].str.upper()、df[].str.lower()，全大写或全小写操作
    df[].str.len()、df[].str.strip()，长度操作，删两端空白操作
    df[].str.contains("sh")，是否包含子串
    df[].str.replace("sh", "qq")，替换子串
    
"""
print(df["股票名称"].str[:2])
print(df["股票代码"].str.upper())
print(df["股票代码"].str.len())
print(df["股票代码"].str.contains("sh"))
print(df["股票代码"].str.replace("sh", "qq"))
