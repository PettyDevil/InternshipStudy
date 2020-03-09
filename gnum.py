from matplotlib import pyplot as plt
import matplotlib
# 设定显示的信息
font = {'family': 'microsoft YAHEI',
        'weight': 'bold'}
matplotlib.rc('font', **font)

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x=list(range(11,31,1))
plt.plot(x,y)
plt.xticks(x)
plt.xlabel("年龄")
plt.ylabel("女(男)朋友个数")
plt.title("11岁到30岁每年交的女(男)朋友的数量")
plt.show()