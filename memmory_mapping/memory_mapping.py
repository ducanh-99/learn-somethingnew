import mmap

with open('large_file.txt', 'rb') as file:
    mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

# Now, mmapped_file behaves like a bytes object containing the file's contents
print(mmapped_file[:100])  # Print the first 100 bytes
mmapped_file.close()  # Close the memory map when done
