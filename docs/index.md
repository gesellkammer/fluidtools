# Home

Welcome to the **fluidtools** documentation!

**fluidtools** is a python library to help working with soundfonts, using fluidsynth. It needs
fluidsynth >= 2 to be installed. The library itself is written in c with glue code written in cython

## Installation

``` bash
pip install fluidtools
```

## Quick Introduction

### Query the programs (presets) present in a soundfont

```python

import fluidtools
presets = fluidtools.list_presets("/path/to/soundfont.sf2")
for preset in presets:
    bank, presetnum, name = preset
    print(f"Preset: {bank:03d} - {presetnum:03d} {name}")

```

## Reference

See [reference](reference.md)

