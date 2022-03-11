"""
Python版本：3.9.7
已安装的包：numpy、pandas、scipy、sympy、pyecharts
pyecharts中文文档：https://pyecharts.org/#/
"""
import numpy
import pandas
import scipy
import sympy
from pyecharts.charts import Line
import pyecharts.options as opts
import datetime


# 任务主函数
def draw_tread(
        calc_start=20161230,
        calc_end=20211230,
        tread_win=20,  # 20个周期内找一根最长或者点数最多的
        wave_win=5,  # 5个周期有一个最低值则是波谷
        wave_step=3,  # 5个周期相关联的地方可能会漏掉波谷，所以滑动观察，步长为3
        bias=0.5,  # 趋势线被击穿，但是点在线的附近，y对应线上y’差值小于0.5
        tread_point_cnt=3,  # 表示趋势线上至少有3个点
        tread_length=12  # 趋势线的相对长度取大于等于12的，并且长度最长的一条，才算趋势线
):
    # 第一步，打开csv文件，确定处理数据的区间
    df = pandas.read_csv('寻找趋势线.csv')
    endIndex = df[df.trade_date == calc_end].index.tolist()[0]
    startIndex = df[df.trade_date == calc_start].index.tolist()[0]
    df = df.tail(endIndex - startIndex + 1)
    # 第二步，将这些数据渲染到pyecharts的折线图上
    (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=df["trade_date"])
            .add_yaxis(
            series_name="",
            y_axis=df["price"],
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .render("render.html")
    )


if __name__ == "__main__":
    draw_tread()
