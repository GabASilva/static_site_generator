import os
import shutil
from gencontent import generate_page, generate_pages_recursive
from copystatic import copy_files_recursive

def main():
	if os.path.exists("public"):
		shutil.rmtree("public")
	os.mkdir("public")
	copy_files_recursive("./static", "./public")
	generate_pages_recursive("content", "template.html", "public")

main()
