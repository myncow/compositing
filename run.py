import argparse
from composit import composite_all_permutations,composite_probabilistically,display_random

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, required=True)
args = parser.parse_args()

if args.mode == "permute":
    composite_all_permutations()
elif args.mode == "probabilistic":
    composite_probabilistically()
elif args.mode == "display":
    display_random()
else:
    print("Specify a flag: either --mode permute or --mode probabilistic")


