from PIL import Image
import argparse         #argparse模块用于命令行参数控制

parser = argparse.ArgumentParser()   
parser.add_argument('file')  #增加参数file
parser.add_argument('-O','--output')    #增加参数--output
parser.add_argument('--width',type=int,default=100)  #增加参数--width
parser.add_argument('--height',type=int,default=100) #增加参数--height
args = parser.parse_args()     #获取命令行参数

#将获取到的参数赋值给各变量
ImgName = args.file
OutPutFile = args.output
Width = args.width
Height =args.height

#字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZo0QLCJUYXZcvunxrjft/\|()1{}[]?-_=~<>i!lI;:\"^`'.")

#将像素点转换成字符
def get_char(r,g,b,alpha=255):
	if alpha == 0:
		return " "
	length = len(ascii_char)
	gray = int(0.299*r + 0.587*g + 0.114*b)  #将RGB转成灰度
	
	return ascii_char[int(gray/255*(length-1))]


if __name__ == "__main__":
	im = Image.open(ImgName)  #打开图片
	im = im.resize((Width,Height), Image.NEAREST) #重置图片尺寸
	
	txt = ""
	for i in range(Height):
		for j in range(Width):
			txt += get_char(*im.getpixel((j,i))) 
		txt += "\n"
	print(txt)	
	if OutPutFile:
		with open(OutPutFile,'w') as f:
			f.write(txt)
	else:
		with open('output.txt','w') as f:
			f.write(txt)