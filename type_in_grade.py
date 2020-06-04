import os
import pandas as pd


class MakeGrade:
	def __init__(self, path):
		self.path = path

	def get_files_name(self):
		files = os.listdir(self.path)
		files.sort(key=lambda x: int(x[2:4]))
		return files

	def get_number(self):
		number_list = []
		files = self.get_files_name()
		for i in files:
			number_list.append(i[2:4])
		return number_list

	def get_id(self):
		id_list = []
		files = self.get_files_name()
		for j in files:
			id_list.append(j[5:15])
		return id_list

	def get_name(self):
		name_list = []
		files = self.get_files_name()
		for i in files:
			name_list.append(i[15:-9])
		return name_list


if __name__ == "__main__":
	files_path = "D:/OneDrive - ctgu.edu.cn/Export/批改的卷子/"
	files_ = MakeGrade(files_path)
	numbers = files_.get_number()
	ids = files_.get_id()
	names = files_.get_name()
	dic1 = {'序号': numbers, '学号': ids,'姓名': names,'成绩':None}
	df = pd.DataFrame(dic1)
	df.to_excel('2.xlsx', index=False)
