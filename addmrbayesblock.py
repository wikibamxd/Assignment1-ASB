import sys
from pathlib import Path

MRBAYES_BLOCK = """
begin mrbayes;

    set autoclose=yes nowarn=yes;

    lset nst=6 rates=gamma;

    mcmc nruns=2 nchains=4 ngen=4000000 samplefreq=100 diagnfreq=1000 stoprule=yes stopval=0.01;

    sump burnin=10000;
    sumt burnin=10000;

end;
"""

def add_mrbayes_block(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Check if mrbayes block already exists
    if "begin mrbayes" in content.lower():
        print(f"[SKIP] {file_path} already has a MrBayes block")
        return

    # Append block at the end
    with open(file_path, "a") as f:
        f.write("\n" + MRBAYES_BLOCK)

    print(f"[OK] Added MrBayes block to {file_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python add_mrbayes.py file1.nex file2.nex ...")
        sys.exit(1)

    for file in sys.argv[1:]:
        path = Path(file)
        if path.exists():
            add_mrbayes_block(path)
        else:
            print(f"[ERROR] File not found: {file}")


if __name__ == "__main__":
    main()