# marvelous_tools
Marvelous tools
```
conda env create -f marvelous.yml 
conda activate marvelous_tools
```

```
python3 tools.py naphtalene.xyz -l 1,2,4 -d 2.2
```
OUTPUT

```
Target: [ 1.63384     0.24096333  2.2       ]
```
Point (1.63384, 0.24096333, 2.2) is above the plane defined by atoms 1, 2 and 4 at a distance of 2.2 angstrom

If you prefer the atom on the other side of the plane then input a negative distance OR add --phase=-1.
