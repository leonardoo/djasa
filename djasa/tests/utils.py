import os
from shutil import rmtree

def remove_app(dirpath):
	path = os.path.join(os.getcwd(), dirpath)
	rmtree(path,ignore_errors=True)

def get_list_dir_files(top_path):
	
	top_dir = os.path.join(os.getcwd(),top_path)
	dirs = []

	for (dirpath, dirnames, filenames) in os.walk(top_dir):
		dirs.append((dirpath,filenames))
	return dirs
