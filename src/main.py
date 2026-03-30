import os
import shutil
import sys
from gencontent import generate_pages_recursive
from copystatic import copy_files_recursive

def main():
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
	else:
		basepath = "/"
	if os.path.exists("docs"):
		shutil.rmtree("docs")
	os.mkdir("docs")
	copy_files_recursive("./static", "./docs")
	generate_pages_recursive("content", "template.html", "docs",basepath)

main()
