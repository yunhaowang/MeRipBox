import sys

if len(sys.argv) != 3:
	print "Usage: python py_remove_unpaired_read_mate.py example/test_PE/Alignment/test_PE.uniq.fm.sort.rd.rr.sam example/test_PE/Alignment/test_PE.uniq.fm.sort.rd.rr.ru.sam"
	sys.exit()

in_fl = open(sys.argv[1])
out_fl = open(sys.argv[2],"w")

dic = {}
for line in in_fl:
	if line.startswith("@"):
		continue
	else:
		rid = line.strip().split("\t")[0]
		dic[rid] = 0
in_fl.close()

in_fl = open(sys.argv[1])
for line in in_fl:
        if line.startswith("@"):
		continue
        else:
                rid = line.strip().split("\t")[0]
                dic[rid] += 1
in_fl.close()

in_fl = open(sys.argv[1])
for line in in_fl:
        if line.startswith("@"):
		print >>out_fl, line,
        else:
                rid = line.strip().split("\t")[0]
                if dic[rid] == 2:
			print >>out_fl, line,	
in_fl.close()
out_fl.close()
