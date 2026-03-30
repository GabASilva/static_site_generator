import os
import shutil
import sys
from gencontent import generate_page, generate_pages_recursive
from copystatic import copy_files_recursive

def main():
	basepath = sys.argv
	if basepath == [""]:
		basepath = ["/"]
	if os.path.exists("public"):
		shutil.rmtree("public")
	os.mkdir("public")
	copy_files_recursive("./static", "./docs")
	generate_pages_recursive("content", "template.html", "docs",basepath)

main()
