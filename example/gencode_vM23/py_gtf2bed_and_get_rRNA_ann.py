import sys

if len(sys.argv) != 4:
	print "Usage: python py_gtf2bed_and_get_rRNA_ann.py gencode.vM23.annotation.chr19.gtf gencode.vM23.annotation.chr19.bed gencode.vM23.annotation.chr19.rRNA.bed"
	sys.exit()

in_fl = open(sys.argv[1])
out_1 = open(sys.argv[2],"w")
out_2 = open(sys.argv[3],"w")
for line in in_fl:
	if line.startswith("#"):
		continue
	chrom,source,feature,s,e,score,strand = line.strip().split("\t")[:7]
	if feature == "transcript":
		info = line.strip().split("\t")[-1]
		gene_id = info.split("gene_id \"")[1].split("\"")[0]
		iso_id = info.split("transcript_id \"")[1].split("\"")[0]
		gene_type = info.split("gene_type \"")[1].split("\"")[0]
		print >>out_1, "\t".join([chrom,s,e,iso_id,gene_id,strand])
		if gene_type == "rRNA" or gene_type == "Mt_rRNA":
			print >>out_2, "\t".join([chrom,s,e,iso_id,gene_id,strand])
in_fl.close()
out_1.close()
out_2.close()
