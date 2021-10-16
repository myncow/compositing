import argparse
from generator import logic

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, required=True)
args = parser.parse_args()

logic_main=logic.composite_probabilistically

if args.mode == "permute":
    pass
elif args.mode == "logic":
    logic_main()

else:
    print("Specify a flag: either --mode permute or --mode probabilistic")


