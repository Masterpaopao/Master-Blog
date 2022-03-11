# 微信推送图片的主程序文件  By YuHang
"""
Python版本：
    3.6.13
需要安装的第三方库：
    pywin32, pypiwin32, pandas, pillow, dataframe_image, redis, excel2img, openpyxl
需要安装的软件：
    按键精灵，谷歌浏览器（必须设置为默认浏览器），Excel（是微软的Excel不是WPS）
"""
import json

import win32api
import win32gui
import win32con
import win32clipboard
import dataframe_image
import re
import os
import time
import pandas
import redis
import excel2img
from PIL import Image
from io import BytesIO
from constant_data import *
from constant_keyboard import *
from public_methods import *
from redis_methods import *

# 获取窗口句柄
hwnd = win32gui.FindWindow(WINDOWCLASS, WINDOWTITLE)
# 定义redis连接池和会话窗口
redis_pool = redis.ConnectionPool(host=REDISHOST, db=REDISDB, port=REDISPORT, decode_responses=True)
redis_client = redis.Redis(connection_pool=redis_pool)
# 规定数据的浮点数精度为2
pandas.options.display.precision = 2


def remove_files(file_paths, lis_type=True):
    """
    功能：
        根据path地址列表删除指定的文件
    参数：
        file_paths - 文件的地址
        lis_type - 为True时则代表传参的值为列表
    """
    if lis_type is False:
        file_paths = list(file_paths)
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(file_path + "文件已删除。")
            except Exception as e:
                print(f"文件操作发生异常，原因为：{e}")


def create_img_path(img_date, count=1):
    """
    功能：
        创建文件夹并将提前生成图片地址
    参数：
        img_date - 图片时间
        count - 代表分割图片的总数量，如果是1则无视
    返回：
        img_path_lis - 图片地址列表
    """
    img_path_lis = []
    # 先创建日期文件夹进行图片归类
    date_dir = "-".join(img_date.split("_")[:3])
    path = "image/" + date_dir
    if not os.path.exists(path):
        os.makedirs(path)
    # 定义图片名字
    if count == 1:
        return [r"{}/【{}】.png".format(path, img_date)]
    else:
        for i in range(count):
            img_path_lis.append(r"{}/【{}】_{}.png".format(path, img_date, i + 1))
        return img_path_lis


def create_image(img_date, df, limit=100):
    """
    功能：
        在已经创建好的文件夹内根据图片地址生成图片
    参数：
        img_date - 图片时间
        df - dataframe数据
        limit - 数据的数量限制，最高只能100行，行数计算不包含表头
    返回：
        img_path_lis - 图片地址列表
    """
    df_len = len(df)
    if df_len > limit:
        # 将数据同等份分割成子列表
        df_lis = [df[i:i + limit] for i in range(0, df_len, limit)]
        # 生成相应的地址列表
        img_path_lis = create_img_path(img_date, len(df_lis))
        for index, dfl in enumerate(df_lis):
            # 注意，这句代码必须要使用谷歌浏览器且设置为默认浏览器
            dataframe_image.export(dfl, img_path_lis[index])
    else:
        # 如果图片不需要分割
        img_path_lis = create_img_path(img_date)
        dataframe_image.export(df, img_path_lis[0])
    return img_path_lis


def go_dataframe_image(img_date, df, receiver_lis):
    """
    功能：
        图片输出程序
    参数：
        img_date - 图片时间
        df - dataframe数据
        receiver_lis - 接收消息的群组编号列表
    """
    # 窗口初始化
    start_window()
    # 生成图片
    img_path_lis = create_image(img_date, df)
    # 发送消息
    for i in receiver_lis:
        image_send(img_path_lis, img_date, i - 1)


def mouse_click(x, y):
    """
    功能：
        在某一个窗口坐标触发鼠标点击行为
    参数：
        x - 窗口的x坐标
        y - 窗口的y坐标
    """
    # 获取句柄对应窗体顶点坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    x = left + x
    y = top + y
    # 设置鼠标位置
    win32api.SetCursorPos((x, y))
    # 鼠标左键发生点击事件
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # 鼠标左键发生抬起事件
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.5)


def keyboard_press(keys, count):
    """
    功能：
        键盘映射触发键盘敲击行为
    参数:
        keys - 键盘映射列表
        count - 触发次数
    """
    for n in range(0, count):
        # 遍历keys中所有按键，依次按下
        for key in keys:
            win32api.keybd_event(VKCODE[key], 0, 0, 0)
            time.sleep(0.1)
        # 遍历keys中所有按键，依次抬起
        for key in keys:
            win32api.keybd_event(VKCODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1)


def clipboard_write(data, data_type):
    """
    功能：
        将数据写入剪切板
    参数：
        data - 需要粘贴的数据
        data_type - 数据的类型，0为文字，1为图片
    """
    # 打开剪切板
    win32clipboard.OpenClipboard()
    # 清空剪切板
    win32clipboard.EmptyClipboard()
    # 如果传进来的是图片
    if data_type:
        # 打开图片
        image = Image.open(data)
        # 开辟一个内存空间读写byte型的数据
        output = BytesIO()
        # 将图片以byte形式写入output
        image.save(output, 'BMP')
        # data写入output的14位以后数据，为无格式形式的纯图片数据
        data = output.getvalue()[14:]
        # 关闭内存空间
        output.close()
        # 将图片以DIB格式写入剪切板
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    else:
        # 将文本以unicode编码写入剪切板
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, data)
    # 关闭剪切板
    win32clipboard.CloseClipboard()
    time.sleep(0.5)


def group_choose(index):
    """
    功能：
        在窗口中选择群聊
    参数：
        index - 群组的编号索引
    """
    # 点击左侧通讯录图标
    mouse_click(CONTACTSICONX, CONTACTSICONY)
    time.sleep(0.5)
    # 点击特定群组
    mouse_click(FIRSTGROUPX, FIRSTGROUPY + GROUPDISTANCE * index)
    time.sleep(0.5)
    # 点击发消息进入聊天页面
    mouse_click(SETMESSAGEX, SETMESSAGEY)
    time.sleep(0.5)


def message_send():
    """
    功能：
        发送消息
    """
    # 同时按下‘ctrl’和‘v’，进行粘贴
    keyboard_press(['ctrl', 'v'], 1)
    # 按下enter键，进行发送
    keyboard_press(['enter'], 1)
    time.sleep(0.5)


def image_send(img_path_lis, img_date, index):
    """
    功能：
        将图片发送到群组里
    参数：
        img_path_lis - 图片地址列表
        img_date - 图片日期
        index - 群组的编号索引
    """
    group_choose(index)
    # 发送文字提醒
    img_date = img_date[:4] + '年' + img_date[5:7] + '月' + img_date[8:10] + '日' + img_date[11:13] + '时' + img_date[14:16] + '分'
    tips = f"程序于{img_date}向编号为{index + 1}的群组发送{len(img_path_lis)}张图片"
    clipboard_write(tips, 0)
    message_send()
    # 发送图片
    for img_path in img_path_lis:
        clipboard_write(img_path, 1)
        message_send()


def start_window():
    """
    功能：
        目标窗口的初始化
    """
    global hwnd
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(WINDOWCLASS, WINDOWTITLE)
    # 窗口激活
    win32gui.SetForegroundWindow(hwnd)
    # 参数3为窗口最大化操作
    win32gui.ShowWindow(hwnd, 3)
    # 将鼠标移动至通讯录竖栏
    win32api.SetCursorPos((CONTACTSCOLUMNX, CONTACTSCOLUMNY))
    # 通过虚拟滑动鼠标滚轮，让滑动条滚到顶部
    for i in range(1, 9999):
        # 滚动鼠标滚轮
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1)
    time.sleep(0.5)


def output_excel(df, excel_date, headers):
    """
    功能：
        数据在输出成Excel文件时大额数据不会被转化为科学计数法形式
    参数：
        df - dataframe数据
        excel_date - excel文件命名的时间
        headers - 需要操作的表头名字列表
    返回：
        excel_path - excel文件地址
    """
    # 先检查excel目录是否存在
    date_dir = "-".join(excel_date.split("_")[:3])
    path = "excel\\" + date_dir
    if not os.path.exists(path):
        os.makedirs(path)
    # 将指定列的数据类型修改为字符串保证excel文件的可读性
    df[headers] = df[headers].astype(str)
    try:
        # 定义一个excel对象，需要openpyxl第三方库支持
        excel = pandas.ExcelWriter(f"{path}\\【{excel_date}】.xlsx")
        df.to_excel(excel, sheet_name=f"【{excel_date}】", index=False)
        # 将数据写入进去之后继续优化指定列宽，为了进一步保证excel文件的可读性
        sheet = excel.sheets[f"【{excel_date}】"]
        # 我在这个地方卡了很久，设置列宽的对象不是表头名字，而是excel文件上面的ABCD……序号！
        order_lis = [chr(ord('A') + list(df.T.index).index(header)) for header in headers]
        for order in order_lis:
            sheet.column_dimensions[order].width = 12
        # 表格对象完成所有操作之后记得保存到本地
        excel.save()
        print(f"{path}\\【{excel_date}】.xlsx文件已生成。")
        return f"{path}\\【{excel_date}】.xlsx"
    except Exception as e:
        print(f"文件操作发生异常，原因为：{e}")


def create_image_excel2img(img_date, excel_path):
    """
    功能：
        使用excel2img模块，在已经创建好的文件夹内根据图片地址生成图片
    参数：
        img_date - 图片时间
        excel_path - excel文件地址
    返回：
        img_path_list - 图片地址列表
    """
    excel_name = re.findall(r"【.*】", excel_path)[0]
    img_path_lis = create_img_path(img_date)
    excel2img.export_img(excel_path, img_path_lis[0], excel_name)
    print(f"{img_path_lis[0]}文件已生成。")
    return img_path_lis


def go_excel2img(img_date, excel_path, receiver_lis):
    """
    功能：
        使用excel2img模块，图片输出程序
    参数：
        img_date - 图片时间
        excel_path - excel文件地址
        receiver_lis - 接收消息的群组编号列表
    返回:
        used_path_lis - 返回本轮操作产生的文件path地址
    """
    # 窗口初始化
    start_window()
    # 生成图片，因为本函数返回的是所有文件地址列表故变量名有所改变
    used_path_lis = create_image_excel2img(img_date, excel_path)
    # 发送消息
    for i in receiver_lis:
        image_send(used_path_lis, img_date, i - 1)
    # 完成之后清点本轮操作产生的所有文件地址列表
    used_path_lis.append(excel_path)
    return used_path_lis


@printf
def run_procedure(received_df, receiver_lis):
    """
    功能：
        核心运行过程，配合打印装饰器函数
    参数：
        received_df - 接收到的df数据
        receiver_lis - 接收到的群组编号列表
    """
    # 展示一下被弹出来的dataframe数据
    print(f"已在redis队列弹出一条消息{received_df.to_json()}")
    # 根据数据量的大小，决定一种图片输出方式
    img_date = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # 数据行数超过100选择excel2img方式输出图片，生成一个excel文件
    excel_path = output_excel(received_df, img_date, HEADERS)
    # excel文件里面的数据经过展示优化之后进行制图
    used_path_lis = go_excel2img(img_date, excel_path, receiver_lis)
    # 操作完成之后删除本轮生成的excel文件和图片文件
    # remove_files(used_path_lis)

    # # 数据行数少于100选择dataframe_image方式输出图片
    # excel_path = output_excel(received_df, img_date, HEADERS)
    # go_dataframe_image(img_date, received_df, receiver_lis)

    # 每一轮操作完成后，终端应当给出提示
    print(f"数据时间{img_date}，发送的微信群组编号为{receiver_lis}，本轮操作已完成。")


def start_program():
    """
    功能：
        项目程序入口
    """
    # 在死循环监听队列中，提取推送过来的消息
    while True:
        received_df, receiver_lis = redis_pop(redis_client)
        if received_df is not None and receiver_lis is not None:
            # 数据有效，进行一轮操作
            run_procedure(received_df, receiver_lis)


if __name__ == '__main__':
    # 手动生产
    output_df = pandas.read_csv("csv\sh600000.csv", encoding="gbk", nrows=20)
    receiver_list = [1]
    redis_push(redis_client, output_df, receiver_list)
    # 项目启动
    start_program()
