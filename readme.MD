# Image Compositing
I set up this repo so we can: 
1. generate all possible variations given our layers  (FEATURE ALREADY WORKING)
2. probabilistically control the composited output. (WILL ADD ONCE LAYERS READY)

## Requirements
- Python3 (https://www.python.org/downloads/)
- Layers must be in PNG format
- Layers must all have the same size

## How to use
Start by adding the layers in to the `layers/` folders. This program currently supports 6 layers. Layer1 corresponds to the background, an Layer6 is the foremost layer.

To generate composites open terminal and type following:
1. `source venv/bin/activate`
2. `python3 run.py --mode "permute"` for generating permutations (this will take time with a lot of layers)
3. Check `output` folder for composited images.