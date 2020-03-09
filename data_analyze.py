
from matplotlib import pyplot as plt
import matplotlib
# 设定显示的信息
font = {'family': 'microsoft YAHEI',
        'weight': 'bold'}
matplotlib.rc('font', **font)
# 温度信息：2~24小时之间的温度  y轴温度
y=[15,13,14.5,17,20,25,26,26,27,22,18,15]
# 做x轴的刻度 时间
x=list(range(2,25,2))

# 设定图的信息
plt.figure(figsize=(15,6),dpi=80)

# 画一个折线图
plt.plot(x,y,linewidth=2,linestyle=":",color="r")
# 设定x轴的刻度
# plt.xticks(x)
plt.xticks(x[:2])
# 设置x轴与y轴的显示信息
plt.xlabel("时间")
plt.ylabel("温度")
# 设置整张图片的显示信息
plt.title("一天中的温度情况")

# 将生成的图保存到本地
# plt.savefig("output/one.png")
# 显示图
plt.show()

import random

a=[random.randint(20,35) for i in range(120)]
# 时间  x轴
x=list(range(1,121))
plt.figure(figsize=(16,6),dpi=80)
plt.plot(x,a)
x_msg=["10点{}分".format(i) for i in range(60)]
x_msg+=["11点{}分".format(i) for i in range(60)]
# ratation显示文字的翻转度数
plt.xticks(x[::5],x_msg[::5],rotation=45)# 刻度不能用简单地数字表示10点1分-10点60分 11点1分-11点60分
plt.xlabel("时间")
plt.ylabel("温度")
plt.show()