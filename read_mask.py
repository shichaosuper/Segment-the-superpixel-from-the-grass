import csv
import numpy as np

class read_mask:
	csv_reader = []
	def bfs_find_individual(self, csv_reader):
		grass_list = []
		csv_reader = np.array(csv_reader)
		print(type(csv_reader[0][0]))
		row, col = csv_reader.shape
		vis = np.zeros(csv_reader.shape)
		
		dx = [0, 0, 1, 1, 1]
		dy = [-1, 1, -1, 0, 1]
		
		for i in range(row):
			for j in range(col):
				if csv_reader[i, j] == '0' and vis[i, j] == 0:
					 
					q = [[i, j]]
					rear, head = 0, 1
					
					while(rear < head):
						curx, cury = q[rear]
						rear += 1
						vis[curx, cury] = 1
						for dir in range(5):
							_x, _y = curx + dx[dir], cury + dy[dir]
							if(_x < 0 or _x >= row or _y < 0 or _y >= col):
								continue
							if(csv_reader[_x, _y] == '0' and vis[_x, _y] == 0):
								vis[_x, _y] = 1
								head += 1
								q += [[_x, _y]]
					grass_list += [q]
		return grass_list
		
		
	def find_corner(self, csv_reader):
		grass_list = self.bfs_find_individual(csv_reader)
		corners_list = []
		for grass in grass_list:
			row_min, row_max, col_min, col_max = 1000000, -1, 1000000, -1
			for pt in grass:
				x, y = pt
				row_min = min(row_min, x)
				row_max = max(row_max, x)
				col_min = min(col_min, y)
				col_max = max(col_max, y)
			corners_list += [[row_min, row_max, col_min, col_max]]
		
		return corners_list

	def __init__(self, name):
		self.csv_reader = csv.reader(open(name+".csv"))
		mx = []
		for rows in self.csv_reader:
			mx += [rows]

		self.csv_reader = mx
		
	def _find_corner(self):
		corners_list = self.find_corner(self.csv_reader)
		for pr in corners_list:
			print(pr[0], pr[1], pr[2], pr[3])
		return corners_list, len(self.csv_reader), len(self.csv_reader[0])
