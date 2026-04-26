# Assignment1-ASB
A repository for scripts used in "Assignment 1" of "Análise de Sequências Biológicas".

### ncbi_batch_fetch.py
'ncbi_batch_fetch.py' is a script used to automate the process of accessing NCBI's api to download the desired list of sequences from a txt file (one acession number per line).
- Use example: python ncbi_batch_fetch.py -db <database> -i <file.txt>

### geneIdentificator.py
'geneIdentificator.py' is a script used to indentify and separate the 3 "COI,SSU,EF1A" genes from a single FASTA file.
- Use example: geneIdentificator.py -f <file.fasta>

### seq_renamer.py
'seq_renamer.py' is a script used to shorten the lenght of the titles of a FASTA file.
- Use example: python seq_renamer.py -f <file.fasta>

### addmrbayesblock.py
'addmrbayesblock.py' is a script used to automate the process of editing a desired NEXUS file for the non interactive and continuous use of MrBayes.
- Use example: addmrbayesblock.py <file.nexus>