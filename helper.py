import requests, base64, json, os, time,config
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from aip import AipOcr


client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)
driver = webdriver.Chrome(config.driver_location)
# 访问百度
driver.get('http://www.baidu.com')
def get_text_from_image(image):
	words=""
	for word in client.basicGeneral(image)['words_result']:
		words+=word['words']
	tissue = words[2:3]
	if tissue=='.':            #去掉题目编号
		words = words[3:]
	else:
		words= words[2:]
	return words


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
count = 0
screenpath = config.image_directory
while True:
  text = input('按下回车发起搜索')

  start = time.time()
  count = count+1
  imagepath = config.image_directory+"screen" + str(count) +".png"
  region_path = config.image_directory+"region" + str(count) +".png"

  if not os.path.exists(config.image_directory):
    os.mkdir(config.image_directory)
  os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
  os.system("adb pull /sdcard/screenshot.png " + imagepath)

  im = Image.open(imagepath)
  img_size = im.size
  w = im.size[0]
  h = im.size[1]

  region = im.crop((config.left, config.top, w - config.right, config.bottom))  # 裁剪的区域
  region.save(region_path)
  image_data = open(region_path, 'rb').read();
  keyword =get_text_from_image(image_data)

  print("OCR识别内容: " + keyword)

  driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
  driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
  driver.find_element_by_id('kw').send_keys(keyword)
  driver.find_element_by_id('su').send_keys(Keys.ENTER)

  end = time.time()
  print('程序用时：' + str(end - start) + '秒')
