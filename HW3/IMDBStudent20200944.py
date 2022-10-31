import sys

genreDic = {}
with open(sys.argv[1], "rt") as fp:
	while True:
		line = fp.readline()
		if not line: break

		info = line.split('::')
		genre = info[2].split('|')
		for item in genre:	
			g = item.strip()
			if g not in genreDic.keys():
				genreDic[g] = 1
			else:
				genreDic[g] += 1

	f = open(sys.argv[2], "wt")
	genreList = genreDic.keys()
	for key in genreList:
		f.write("%s %d\n" %(key, genreDic[key]))
	f.close()
