import os
import shutil
from copystatic import copy_files_recursive

def main():
	if os.path.exists("public"):
		shutil.rmtree("public")
	os.mkdir("public")
	copy_files_recursive("./static", "./public")




main()
