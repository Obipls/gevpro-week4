# #!/usr/bin/env python
# spontal_filter.py
# Olivier Louwaars s2814714
# 3-3-2015

import sys
import xml.etree.ElementTree as ET

def main(argv):
	# Check for valid program call
	if len(argv)<3:
		print("Usage = spontal_filter.py spontal.xml spontal_filtered.xml")
		exit(-1)
	
	# Open XML-file and variablelize it's children
	tree=ET.parse(argv[1])
	root=tree.getroot()
	x=0
	for child in root:
		# Check if the start and end pitch are within the range from bottom to top
		if not float(root[x][5].text)<=float(root[x][12].text)<=float(root[x][7].text) or not float(root[x][5].text)<=float(root[x][13].text)<=float(root[x][7].text):
			# Remove them if they are out of range
			root.remove(child)
		x+=1
	# Write all the correct values to a new document
	tree.write(argv[2])

if __name__=="__main__":
	main(sys.argv)