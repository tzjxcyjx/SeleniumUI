import pytesseract
from PIL import Image
from ShowApiRequest import ShowapiRequest
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# image = Image.open("E:/imooc2.png")
# text= pytesseract.image_to_string(image,config=tessdata_dir_config)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:/imooc3.png") #文件上传时设置
res = r.post()
#print(res.text)
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息