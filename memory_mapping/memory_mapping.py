"""
File: memory_mapping.py
Author: Anthony Nguyen
Date: September 3, 2023
Description: Demo Memory Mapping using mmap library
"""


import mmap
"""
Memory mapping is a technique that uses lower-level operating system APIs 
to load a file directly into computer memory. 
It can dramatically improve file I/O performance in your program. 
To better understand how memory mapping improves performance, 
as well as how and when you can use the mmap module to take advantage 
of these performance benefits, it’s useful to first learn a bit about
computer memory.
"""
with open('memory_mapping/large_file.txt', 'rb') as file:
    mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

# Now, mmapped_file behaves like a bytes object containing the file's contents
print(mmapped_file[:100])  # Print the first 100 bytes
mmapped_file.close()  # Close the memory map when done
