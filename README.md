# MeRipBox (version 0.1)
Time-stamp: <2022-2-28 Yunhao Wang, Email: yunhaowang@126.com>


## Introduction

MeRIP-seq (N6-methyladenosine/m6A specific methylated RNA immunoprecipitation followed by high-throughput sequencing) is an experimental approach to map RNAs with specific chemical/epigenetic modifications, such as N(6)-methyladenosine (m6A). MeRipBox is a bioinformatics tool/pipeline to analyze MeRIP-seq data, and it includes 6 sections: (1) Quality control of sequencing reads; (2) Align sequencing reads to reference genome; (3) Remove multiply-aligned reads, PCR duplicates and ribosomal RNA-derived reads, and make bigWig file for data visualization; (4) Quantify gene and transcript expression; (5) Call peaks; (6) Search consensus motifs in identified peaks.


## Prerequisite

- Linux system

- python 2.7

- FastQC (v0.11.8) (https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

- Cutadapt (v1.8.1) (https://cutadapt.readthedocs.io/en/v1.8.1/installation.html#quickstart)

- HISAT2 (v2.1.0) (http://daehwankimlab.github.io/hisat2/download/#version-hisat2-210)

- SAMtools (v1.9) (https://sourceforge.net/projects/samtools/files/samtools/1.9/)

- BEDTools (v2.28.0) (https://github.com/arq5x/bedtools2/releases)

- deepTools (v3.2.0) (https://deeptools.readthedocs.io/en/develop/index.html)

- StringTie (v1.3.5) (https://ccb.jhu.edu/software/stringtie/)

- MACS2 (v2.1.2) (https://pypi.org/project/MACS2/2.1.2/)

- Homer (v4.11.1) (http://homer.ucsd.edu/homer/)

Note: (1) For all dependencies/tools above, only the versions indicated have been tested under Linux system. (2) All dependencies above should be in your environment path, which means they can be called/executed without specifying the entire path.


## Install and Run

1. Download the package (e.g., `MeRipBox-0.1.tar.gz`) to a directory (e.g., `/home/`)

2. Unpack it using the command `tar -zxvf /home/MeRipBox-0.1.tar.gz`

3. Now, you can run MeRipBox by the executable file `/home/MeRipBox-0.1/bin/meripboxPE` (for paired-end sequencing data) or `/home/MeRipBox-0.1/bin/meripboxSE` (for single-end sequencing data). Optional, you can add MeRipBox into your PATH so that you can run MeRipBox without having to specify the entire path. For example, you can add one line `export PATH=/home/MeRipBox-0.1/bin:$PATH` to your `~/.bashrc`


## Input

### 1. Raw sequencing reads (FASTQ.GZ format)

Note: MeRipBox supports both single-end and paired-end sequencing data. For single-end sequencing data, in total, 1 (INPUT sample) + 1 (IP sample) = 2 fastq.gz files should be provided. For paired-end sequencing data, in total, 2 (INPUT sample: read mate 1 and read mate 2) + 2 (IP sample: read mate 1 and read mate 2) = 4 fastq.gz files should be provided.  

### 2. Sequencing adapter sequences (for adapter trimming)

This is for trimming the bases from sequencing adapters. The adapter sequences can be obtained from the sequencing service providers or the QC report generated by FastQC.

### 3. Hisat2 index files (for alignment)

Note: the Hisat2 index files must be prepared before running MeRipBox. Please refer the website (http://daehwankimlab.github.io/hisat2/manual/) to build the index files against the reference genome of your interest.

The code used to build the hisat2 index for testing data can be found in the installation folder (/home/MeRipBox-0.1/example/hisat2_index_mm10/run_hista2-build.sh).

### 4. Gene annotation files (GTF and BED format, for gene quantification and motif searching)

The gene annotation library (GTF format) matching the reference genome version of your interest can be downloaded from NCBI, UCSC, Ensembl, GENCODE, or others.

The two BED format files (both all genes and ribosomal RNAs) can be extracted from the GTF file using your own script, with the 6 columns: (1) chromosome ID, (2) start, (3) end, (4) transcript ID, (5) gene ID, and (6) strand.

The code used to generate BED format files for testing data can be found in the installation folder (/home/MeRipBox-0.1/example/gencode_vM23/py_gtf2bed_and_get_rRNA_ann.py).

### 5. Transcriptome size (for peak calling)

Note: the parameter "--gsize" of MACS2 is NOT the size of reference genome here because MeRIP-seq is transcriptome data. Please see the description of the paper (doi: 10.1038/nprot.2012.148) to know how to get the size of transcriptome of your interest. 

### 6. Version of reference genome (for motif searching)

Note: to perform motif search, the genome version of your interest (e.g., mm10 used in testing data) MUST be installed/configured in Homer software. Please see the website (http://homer.ucsd.edu/homer/introduction/configure.html) to configure Homer.


## Output

### 1. Quality control reports and Clean sequencing reads (Subfolder: QC)

Files with the suffix ".html" and ".zip": report of quality control generated by FastQC.

Files with the suffix ".trim.fastq.gz": clean reads after removing low-quality bases and sequencing adapters.
 
### 2. Aligned reads (Subfolder: Alignment)

Files with the suffix ".sam": alignment generated by Hisat2; SAM format.

Files with the suffix ".uniq.sam": uniquely aligned reads; SAM format.

### 3. Processed reads (Subfolder: Alignment)

#### 3.1 Paired-end mode (`meripboxPE`)

Files with the suffix ".uniq.fm.bam": uniquely aligned reads with the fixed mate coordinates; BAM format.

Files with the suffix ".uniq.fm.sort.bam" and ".uniq.fm.sort.bam.bai": uniquely aligned reads with the fixed mate coordinates, sort by coordinates; BAM format.

Files with the suffix ".uniq.fm.sort.rd.bam" and ".uniq.fm.sort.rd.bam.bai": uniquely aligned, PCR duplicate free reads; BAM format.

Files with the suffix ".uniq.fm.sort.rd.stat": uniquely aligned, PCR duplicate free reads; statistics from BAM file generated by samtools stats.

Files with the suffix ".uniq.fm.sort.rd.rr.sam", ".uniq.fm.sort.rd.rr.bam" and ".uniq.fm.sort.rd.rr.bam.bai": uniquely aligned, PCR duplicate free, non-rRNA-derived reads; SAM and BAM format.

Files with the suffix ".uniq.fm.sort.rd.rr.ru.sam", ".uniq.fm.sort.rd.rr.ru.bam" and ".uniq.fm.sort.rd.rr.ru.bam.bai": uniquely aligned, PCR duplicate free, non-rRNA-derived reads, paired reads; SAM and BAM format.

Files with the suffix ".uniq.fm.sort.rd.rr.ru.stat": uniquely aligned, PCR duplicate free, non-rRNA-derived reads, paired reads; statistics from BAM file generated by samtools stats.

Files with the suffix ".uniq.fm.sort.rd.rr.ru.RPKM.bigWig": uniquely aligned, PCR duplicate free, non-rRNA-derived reads, paired reads; read density in 10-bp bin generated by deepTools; normalized by RPKM; can be loaded into genome browser for visualization; BigWig format.

#### 3.2 Single-end mode (`meripboxSE`)

Files with the suffix ".uniq.sort.bam" and ".uniq.sort.bam.bai": uniquely aligned reads, sort by coordinates; BAM format.

Files with the suffix ".uniq.sort.rd.bam" and ".uniq.sort.rd.bam.bai": uniquely aligned, PCR duplicate free reads; BAM format.

Files with the suffix ".uniq.sort.rd.stat": uniquely aligned, PCR duplicate free reads; statistics from BAM file generated by samtools stats.

Files with the suffix ".uniq.sort.rd.rr.bam" and ".uniq.sort.rd.rr.bam.bai": uniquely aligned, PCR duplicate free, non-rRNA-derived reads; BAM format.

Files with the suffix ".uniq.sort.rd.rr.stat": uniquely aligned, PCR duplicate free reads, non-rRNA-derived reads; statistics from BAM file generated by samtools stats.

Files with the suffix ".uniq.sort.rd.rr.RPKM.bigWig": uniquely aligned, PCR duplicate free, non-rRNA-derived reads; read density in 10-bp bin generated by deepTools; normalized by RPKM; can be loaded into genome browser for visualization; BigWig format.

### 4. Gene and transcript quantification (Subfolder: Quantification)

File with the suffix ".gtf": transcript expression generated by StringTie; GTF format.

File with the suffix ".gene-abundance.txt": gene-level expression generated by StringTie; TXT format.

### 5. Peak calling (Subfolder: Peak)

File with the suffix ".xls": statistically significant peaks generated by MACS2; EXCEL format.

File with the suffix ".narrowPeak": statistically significant peaks generated by MACS2; can be loaded into genome broswer for visulization; BED format.

File with the suffix ".bed": the submits of statistically significant peaks generated by MACS2; used for motif searching; BED format.

### 6. Motif searching (Subfolder: Motif)

File with the suffix ".html": statistically significant motifs generated by Homer; HTML format.


## Usage and Example

Under the installation folder /home/MeRipBox-0.1/, run the command line below:

### Paired-end sequencing data

`bin/meripboxPE -n test_PE -o example/test_PE -t 10 -inputR1 example/fastq/Input_R1.fastq.gz -inputR2 example/fastq/Input_R2.fastq.gz -ipR1 example/fastq/IP_R1.fastq.gz -ipR2 example/fastq/IP_R2.fastq.gz -x example/hisat2_index_mm10/chrM -annR example/gencode_vM23/gencode.vM23.annotation.chrM.rRNA.bed -annGG example/gencode_vM23/gencode.vM23.annotation.chrM.gtf -g 242010196 -annGB example/gencode_vM23/gencode.vM23.annotation.chrM.bed -rv mm10 -s test_PE_script.sh`

### Single-end sequencing data

`bin/meripboxSE -n test_SE -o example/test_SE -t 10 -inputR example/fastq/Input_R1.fastq.gz -ipR example/fastq/IP_R1.fastq.gz -x example/hisat2_index_mm10/chrM -annR example/gencode_vM23/gencode.vM23.annotation.chrM.rRNA.bed -annGG example/gencode_vM23/gencode.vM23.annotation.chrM.gtf -g 242010196 -annGB example/gencode_vM23/gencode.vM23.annotation.chrM.bed -rv mm10 -s test_SE_script.sh`


## Citation

The manuscript is currently under review. The citation information will be updated once the manuscript is published. Please cite  Yunhao Wang's GitHub website at this moment if you use MeRipBox.
