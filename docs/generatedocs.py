#!/usr/bin/env python3
import os
import argparse
import sys
from pathlib import Path

try:
    import fluidtools
    from emlib import doctools
    
except ImportError:
    import textwrap
    msg = ("**WARNING**: Trying to update documentation, but the python present in the current environment"
           " does not have the needed packages. Documentation will not be"
           " updated")
    print()
    print("\n".join(textwrap.wrap(msg, width=72)))
    print()
    sys.exit(0)


def findRoot():
    p = Path(__file__).parent
    if (p/"index.md").exists():
        return p.parent
    if (p/"setup.py").exists():
        return p
    raise RuntimeError("Could not locate the root folder")
        

def main(destfolder: str):
    renderConfig = doctools.RenderConfig(splitName=True, fmt="markdown", docfmt="markdown")
    dest = Path(destfolder)
    reference = doctools.generateDocsForModule(fluidtools, 
                                               renderConfig=renderConfig, 
                                               exclude={},
                                               title="Reference")
    open(dest / "reference.md", "w").write(reference)
    
    
if __name__ == "__main__":
    root = findRoot()
    docsfolder = root / "docs"
    assert docsfolder.exists()
    main(docsfolder)
    os.chdir(root)
    os.system("mkdocs build")
