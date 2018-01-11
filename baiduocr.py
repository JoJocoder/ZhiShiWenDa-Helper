from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '10673926'
API_KEY = 'XVfNGUOZj25Qr4GsMuS6A1ZL'
SECRET_KEY = 'cTNPEvjmch78gAeLoU9RVirdqLGgblCB '
path=r'C:\Users\Janton\Desktop\ZhiShiWenDa-Helper-master\image\region3.png'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_text_from_image(image):
	words=""
	for word in client.basicGeneral(image)['words_result']:
		words+=word['words']
	return words


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
