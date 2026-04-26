import argparse
from pathlib import Path

def args_parse():
    parser = argparse.ArgumentParser(description="Split FASTA by gene type")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    return parser.parse_args()

args = args_parse()

# mapping keywords → output file suffix
name_map = {
    "cytochrome": "COI",
    "COI": "COI",
    "18S": "SSU",
    "SSU": "SSU",
    "elongation": "EF1A",
    "EF1A": "EF1A"
}

# prepare output files
outfiles = {
    "COI": open("COI.fasta", "a"),
    "SSU": open("SSU.fasta", "a"),
    "EF1A": open("EF1A.fasta", "a"),
}

current_header = None
current_sequence = []
current_gene = None

with open(args.file) as infile:
    for line in infile:
        line = line.strip()

        if line.startswith(">"):
            # save previous entry
            if current_header and current_gene:
                outfiles[current_gene].write(current_header)
                outfiles[current_gene].write("\n".join(current_sequence) + "\n")

            if current_header and current_gene is None:
                print(f"Warning: no gene detected for {current_header}")

            # reset for new entry
            current_header = line
            current_sequence = []
            current_gene = None

            # detect gene type
            for key, value in name_map.items():
                if key.lower() in line.lower():
                    current_gene = value
                    break

        else:
            current_sequence.append(line)

    # write last entry
    if current_header and current_gene:
        outfiles[current_gene].write(current_header)
        outfiles[current_gene].write("\n".join(current_sequence) + "\n")

# close files
for f in outfiles.values():
    f.close()