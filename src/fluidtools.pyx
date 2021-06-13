import os

from libc.stdio cimport *
from libc.stdlib cimport *
from libc.string cimport *

cdef extern from 'sflspresets.c':

    # struct preset_list

    struct preset_list:
        char name[256]
        preset_list *next
    
    preset_list *_list_presets(const_char *sfpath)  
    void _preset_list_free(preset_list *node)  


def list_presets(str sfpath):
    """
    List the presets in a soundfont

    Args:
        sfpath (str): the path to the soundfont

    Returns:
        (list[tuple[int, int, str]) - a list of tuples of the form 
        (bank:int, num:int, name:str)
    """
    if not os.path.exists(sfpath):
        raise OSError("Soundfont path not found")
    cdef preset_list *pl = _list_presets(sfpath.encode("ASCII", errors="ignore"))
    cdef list out = []
    while True:
        if pl == NULL:
            break
        preset = pl.name.decode('ASCII').strip()
        bank = int(preset[:3])
        num = int(preset[4:7])
        name = preset[8:]
        out.append((bank, num, name))
        pl = pl.next   
    _preset_list_free(pl) 
    return out