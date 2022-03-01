import sys

if len(sys.argv) != 3:
	print "Usage: python py_extract_unique_alignment_hisat2.single-end.py example/test_SE/Alignment/test_SE.sam example/test_SE/Alignment/test_SE.uniq.sam"
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
		info = line.strip()
		i = 1
		read0 = read
		head -= 1
		continue
	if read != read0:
		if i == 1:
			print >>out_sam, info
		info = line.strip()
		i = 1
		read0 = read
	else:
		i += 1
if i == 1:
	print >>out_sam, info
in_sam.close()
out_sam.close()
