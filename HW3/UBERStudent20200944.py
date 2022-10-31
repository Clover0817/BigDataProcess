import sys, calendar

uberList = []
dayOfWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
with open(sys.argv[1], "rt") as fp:
	while True:
		line = fp.readline()
		if not line: break

		info = line.split(',', 2)
		date = info[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		num = info[2].strip()
		uberList.append("%s,%s %s\n" %(info[0], dayOfWeek[day], num))

	f = open(sys.argv[2], "wt")
	for item in uberList:
		f.write(item)
	f.close()
