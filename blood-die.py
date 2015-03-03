# #!/usr/bin/env python
# blood-die.py
# Olivier Louwaars s2814714
# 3-3-2015

import sys
import json
from collections import namedtuple

def main(argv):
	# Check for valid program call
	if len(argv)<2:
		print("Usage = blood-die.py blood-die.json")
		exit(-1)

	langList=json.load(open(argv[1]))
	langWithWord=namedtuple('langWithWord','language, langClass,bloodWords,dieWords')
	simiLangList=[langWithWord(attr[0],attr[1],attr[2].strip().split(', '),attr[3].strip().split(', ')) for attr in langList]
	
	resDict={}
	for item in simiLangList:
		for text in item.bloodWords:
			if text in item.dieWords:
				resDict[item.language]=item.langClass
	print(resDict)

if __name__=="__main__":
	main(sys.argv)