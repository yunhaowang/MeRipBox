import sys

if len(sys.argv) != 3:
	print "Usage: python py_extract_unique_alignment_hisat2.pair-end.py example/test_PE/Alignment/test_PE.sam example/test_PE/Alignment/test_PE.uniq.sam"
	sys.exit()

in_sam = open(sys.argv[1])
out_sam = open(sys.argv[2],"w")

head = 1
for line in in_sam:
	if line.startswith("@"):
		print >>out_sam, line,
		continue
	read,flag,chrom = line.strip().split("\t")[:3]
	if chrom == "*":
		continue
	if head:
		info1 = line.strip()
		i = 1
		read0 = read
		head -= 1
		continue
	if read != read0:
		if i == 2:
			print >>out_sam, info1 + "\n" + info2
		info1 = line.strip()
		i = 1
		read0 = read
	else:
		i += 1
		info2 = line.strip()
if i == 2:
	print >>out_sam, info1 + "\n" + info2
in_sam.close()
out_sam.close()
