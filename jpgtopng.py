import sys
import os
import re
from PIL import Image, ImageFilter


source_path = sys.argv[1]
destination_path = sys.argv[2]

if not os.path.exists(destination_path):
	os.makedirs(destination_path)

for filename in os.listdir(source_path):
	file_path = os.path.join(source_path, filename)
	if os.path.isfile(file_path):
		img = Image.open(file_path)
		new_filename = re.sub(r'\.([^\s]*)', '', filename)
		img.resize((200,200)).convert('RGB').convert('L').save(destination_path + new_filename + '.png', 'PNG')
