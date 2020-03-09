
# 【1】===导包-加载第三方工具
# requests 代替原来所有学urllib.request
import requests
from bs4 import BeautifulSoup;
import os;
# 小说网址为：
xiaoshuo_url = "https://www.biqukan.com/%s/";

# 【4】===获取小说每一个章节的内容
def Get_xiaoshuo_mulu_context():

    pass

# 【3】===获取小说的目录
def Get_xiaoshuo_mulu(url,xiaoshuo_name,header):
    # 1.开始请求网络数据：
    # 第一个参数：请求的地址 第二个参数：请求头文件信息；
    requests_01 = requests.get(url=url,data = header);
    # 2.检查是否访问成功
    print("网络请求的返回码：",requests_01.status_code);
    if requests_01.status_code == 200:
        # 3.将网站下载到本地中
        print("当前网页的编码格式:",requests_01.encoding);
        # 4.修改请求到的数据编码格式
        requests_01.encoding = "gbk";
        # 5.请求源码 - data = html.read();
        data = requests_01.text;
        # print(str(data));
        # 6.将网站信息保存到本地：
        file_path = "C:\/Users\/Administrator\/Desktop\/WHGC2_2019年2月26日\/08_Request_网络小说爬虫\/01_笔趣看小说爬虫下载工具\/%s\/"%xiaoshuo_name;
        print(file_path)
        # 7.判断路径是否存在
        if not os.path.exists(file_path):
            os.makedirs(file_path);
            pass
        # 8.存储文件
        file_xiaoshuo = open("%s%s.html"%(file_path,xiaoshuo_name),"w",1);
        file_xiaoshuo.write(data);
        file_xiaoshuo.close();
        print("已经保存到本地文件中。")

        pass
    else:
        print("网络访问失败：请求码：%d - 请检查网址"%requests_01.status_code);
        pass


    pass


# 【2】===创建一个爬虫的入口
if __name__ == "__main__":
    print("==========进入程序=============");
    print("欢迎使用Python小说爬虫V.10版本");
    print("目前本软件只支持：https://www.biqukan.com网站小说");
    # 1.请用户输入小说下载编号：
    print("请用户输入小说编号格式为：(37_37651)");
    xiaoshuo_code = input("==================请输入小说编号===================\n");
    url = xiaoshuo_url%xiaoshuo_code;
    print("小说地址为：",url)
    #2.请用户输入小说名称
    xiaoshuo_name = input("==================请输入小说名称===================\n")
    print("小说名称为：",xiaoshuo_name);
    # 3.创建网络请求
    # 01.创建一个用户代理-用于请求header文件
    """
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
    """
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"};
    # 调用下载目录函数
    # replace(" ",""):用于去除字符串中所有的空格
    # 第一个参数：小说的地址，第二个参数：小说的名称 第三个参数：请求头文件信息
    Get_xiaoshuo_mulu(url,xiaoshuo_name.replace(" ",""),header);



    pass
