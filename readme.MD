# Rule-based layer compositing library

## Problem
Rule-based layer compositing is a creative challenge at the heart of modern day digital image creation. If we

- Need to generate large image sets (10k+)
- Programatically control image variation through traditional layer scaffolding
- Implement special rules as a form of artistic controls

a handy generator will come a long way!

There are a million of different, valid approaches to this problem. Here, we present a simple, and easily extendable Python implementation.

## How does it work

All application modules are placed in `generator`, which contains the following scripts:
- `composite.py` image compositing happens here using the `wand` (default) or `pillow` python libraries
- `metadata.py` templated based metadata generation to save image specific information
- `rules.py` rules processing algorithm that controls logic of layer combination rules
-`logic.py` the generation engine, extracting run parameters from the config file

The application reads layer data from `layers\`, where a pre-specified number of subfolders must contain your images.

The `config.json` file let's you specify:
- each of the filenames to process in layer folders
- how many to make of them each
- the total number of composites to generate
- whatever special rules you want to apply

Rules may be applied by declaring an item in the config file's `"exceptions"` field. For example entering `"rule_1":["background_1","mid-layer","foreground"]`
will prevent any image that contain all of the contents of the `rule_1` array simultanously to be generated.

### Randomness and generation
- the generation is based on a probabilistic shuffling method, and therefore is a random variable
- we can specify the exact number of each layers we want, but we won't be able to control how they will combine with other layers
- unless setting a random seed (currently hardcoded in `logic.py`)

Furthermore, the total number of generated will files be less than specified in `config.json` if rules are applied, which can depending on their size impact the total number of combinations possible.

## How to use
### Pre-requisites
- Python3, pip, imagemagick
- run `pip install -r requirements.txt` for dependencies

### Layers and rules
- Replace layer folder with your own, where each layer of your image is saved in a folder named `layer_{# layer here}`. `layer_1` corresponding to the background layer. Multiple layers in one subfolders are allowed, being kinda the whole point!
- Edit image generation parameters in `config.json`

### Run
`python3  run.py --mode "logic"` will start the image generation algorithm.