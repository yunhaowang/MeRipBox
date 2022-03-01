import sys

if len(sys.argv) != 3:
	print "Usage: python py_assign_strand2peak.py example/test_PE/Motif/test_PE.bed example/test_PE/Motif/test_PE.strand.bed"
	sys.exit()

in_fl = open(sys.argv[1])
out_fl = open(sys.argv[2],"w")

dic = {}
peak_lst = []
for line in in_fl:	
	if line.strip().endswith("."): continue
	chrom,s,e,peak,qv,strand = line.strip().split(" ")[-1].split("\t")
	chr_s_e = "\t".join([chrom,s,e,peak,qv])
	dic[chr_s_e] = []
	peak_lst.append(chr_s_e)
in_fl.close()

in_fl = open(sys.argv[1])
for line in in_fl:
	if line.strip().endswith("."): continue
        chrom,s,e,peak,qv,strand = line.strip().split(" ")[-1].split("\t")
        chr_s_e = "\t".join([chrom,s,e,peak,qv])
        dic[chr_s_e].append(strand)
in_fl.close()

for peak in peak_lst:
	if len(dic[peak]) == 1:
		print >>out_fl, peak + "\t" + dic[peak][0]
out_fl.close()
