import sys, calendar

uberList = []
dayOfWeek = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
with open(sys.argv[1], "rt") as fp:
	while True:
		line = fp.readline()
		if not line: break

		info = line.split(',', 2)
		region = info[0]

		date = info[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))

		num = info[2].split(",")
		vehicles = int(num[0])
		trips = int(num[1])

		uberList.append([region, day, vehicles, trips])
	
	uberList = sorted(uberList, key = lambda uber: uber[0])
	f = open(sys.argv[2], "wt")
	for item in uberList:
		f.write("%s,%s %d,%d\n" %(item[0], dayOfWeek[item[1]], item[2], item[3]))
	f.close()
