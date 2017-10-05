import sys
from PIL import Image
import os




class photo_merge():
	def __init__(self,file_path=os.path.join(os.environ["HOME"], "Desktop/"),photoNames=[],output='out.png'):
		self.photoNames=photoNames
		self.file_path=file_path
		self.output=output
		self.create_path_names()
		self.merge_photo()

	def create_path_names(self):
		print self.photoNames
		self.path_names=[self.file_path+photo for photo in self.photoNames]

	def merge_photo(self):
		images = map(Image.open, self.path_names)
		widths, heights = zip(*(i.size for i in images))
		total_width = sum(widths)
		max_height = max(heights)
		new_im = Image.new('RGB', (total_width, max_height))
		x_offset = 0
		for im in images:
			new_im.paste(im, (x_offset,0))
			x_offset += im.size[0]
		new_im.save(self.file_path+self.output)



if __name__ == "__main__":
	photo1=photo_merge(photoNames=[])
