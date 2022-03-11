# redis相关函数的定义文件  By YuHang

import json
import pandas as pd
from public_methods import *


def redis_push(client, df, receiver_lis):
    """
    功能：
        将dataframe数据推送到redis队列队首
    参数：
        client - redis会话窗口
        df - dataframe数据
        receiver_lis - 接收消息的微信群编号列表
    """
    df_dic = df.to_dict(orient="index")
    df_message = {"data": df_dic, "receivers": receiver_lis}
    df_json = json.dumps(df_message, ensure_ascii=False)
    try:
        client.lpush("wxmsg", df_json)
    except Exception as e:
        print(f"redis操作发生异常，原因为：{e}")


def redis_pop(client):
    """
    功能：
        从redis队列中弹出队尾元素
    参数：
        client - redis会话窗口
    返回：
        df/None - dataframe数据/空值
    """
    wx_msg = client.brpop("wxmsg", timeout=1)
    wx_msg = wx_msg[1] if wx_msg is not None else None
    if wx_msg:
        df_message = json.loads(wx_msg)
        df = pd.DataFrame.from_dict(df_message["data"], orient="index")
        receiver_lis = df_message["receivers"]
        return df, receiver_lis
    else:
        return None, None


def redis_write(client, df, date):
    """
    功能：
        将dataframe数据写入redis数据库
    参数：
        client - redis会话窗口
        df - dataframe数据
        date - 写数据时的详细时间
    """
    df_dic = df.to_dict(orient="index")
    df_json = json.dumps(df_dic, ensure_ascii=False)
    try:
        client.set(date, df_json, nx=True)
    except Exception as e:
        print(f"redis操作发生异常，原因为：{e}")


def redis_read(client, date):
    """
    功能：
        从redis数据库读取出dataframe数据
    参数：
        client - redis会话窗口
        date - 写数据时的详细时间
    返回：
        df - dataframe数据
    """
    if client.exists(date):
        df_json = client.get(date)
        df_dic = json.loads(df_json)
        df = pd.DataFrame.from_dict(df_dic, orient="index")
        return df
    return None
