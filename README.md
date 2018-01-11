
#使用说明

## 系统要求
1. **安卓手机一部看直播**
2. **电脑一台查看搜索结果**

### 使用步骤
1. 安装python3.6 [python下载地址](https://www.python.org/downloads/)
2. 在本项目根路径下执行 pip install -r requirements.txt
3. 修改默认的配置文件config.py 中Chrome Driver的路径
 Chrome Driver 在lib有一份,需要设置存放的路径 [driver下载地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)
4. 修改配置文件config.py 中图片存放路径
5. 使用百度OCR识别，https://cloud.baidu.com/product/ocr.html
6. 把手机设为开发者模式,在电脑环境变量中添加adb路径,lib中有下载好的adb,调试好adb
7. 每个手机像素不一样,在config文件中调整
8. 启动项目 python helper.py 每当题目出来时按下回车键即可   

##效果
![使用效果](https://github.com/JoJocoder/ZhiShiWenDa-Helper/blob/master/image/xiaoguo3.png)




