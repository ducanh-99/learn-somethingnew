
"""
File: mm_writing.py
Author: Anthony Nguyen
Date: September 3, 2023
Description: Demo Memory Mapping writing using mmap library
"""


import mmap

"""
Python’s mmap module doesn’t allow memory mapping of an empty file. 
This is reasonable because, conceptually,
an empty memory-mapped file is just a buffer of memory, 
so no memory mapping object is needed.
"""


def mmap_io_write(filename):
    with open(filename, mode="r+") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj[10:16] = b"python"
            mmap_obj.flush()


mmap_io_write("memory_mapping/output_file.txt")
