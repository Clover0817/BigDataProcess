import sys, calendar

uberList = []
dayOfWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
with open(sys.argv[1], "rt") as fp:
	while True:
		line = fp.readline()
		if not line: break

		info = line.split(',', 2)
		region = info[0]

		date = info[1].split("/")
		d = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		day = dayOfWeek[d]

		num = info[2].split(",")
		vehicles = int(num[0])
		trips = int(num[1])

		uberList.append("%s,%s %d,%d\n" %(region, day, vehicles, trips))

	f = open(sys.argv[2], "wt")
	for item in uberList:
		f.write(item)
	f.close()
