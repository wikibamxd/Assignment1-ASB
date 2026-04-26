import argparse
import re
from pathlib import Path

def args_parse():
    parser = argparse.ArgumentParser(description="Process files")
    parser.add_argument("-f", "--file", required=True, help="File to open")
    return parser.parse_args()

args = args_parse()
p = Path(args.file)
output_file_name = p.with_stem("c_" + p.stem)

name_map = {
    "fallax": "DIDfal",
    "alpestroides": "LEPals",
    "carestianum": "LEPcar",
    "chailletii": "LEPcha",
    "crustaceum": "LEPcru",
    "granuliferum": "LEPgra",
    "peyerimhoffii": "LEPpey"
}

with open(args.file) as infile, open(output_file_name, "w") as outfile:
    for line in infile:
        if line.startswith(">"):
            title = line.split()
            species_title = title[2]
            locus = title[4]
            if len(locus) < 8:
                locus = title[0][1:]
            for full_name, short_name in name_map.items():
                if full_name in species_title:
                    species_title = short_name

            outfile.write(f">{locus}_{species_title}\n")
        else:
            outfile.write(line)