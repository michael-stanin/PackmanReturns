

BLOCKS_LAYOUT_FILE = "blocks_layout.txt"
PELLETS_LAYOUT_FILE = "pellets_layout.txt"

class Layout:

	def __init__(self, dirpath=None):
		self.dirpath = dirpath

	def read_layout(self, filename):
		f = open(self.dirpath + filename, 'r')
		layout = [line.split() for line in f]
		f.close()

		return layout
	


#layout = Layout("../resources/levels/1/blocks_layout.txt")

