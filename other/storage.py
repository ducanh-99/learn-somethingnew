import ctypes

# Define constants for disk I/O
GENERIC_READ = 0x80000000
OPEN_EXISTING = 3
FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2

# Replace '\\\\.\\PhysicalDrive0' with the appropriate disk device name
# The number indicates the physical drive you want to access.
disk_path = r'\\.\PhysicalDrive0'

# Open the disk for reading
disk_handle = ctypes.windll.kernel32.CreateFileW(
    disk_path, GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0, None
)

if disk_handle == -1:
    print("Error opening the disk.")
else:
    try:
        # Seek to the desired sector (replace 0 with the sector number you want to read)
        sector_number = 0
        bytes_per_sector = 512  # Standard sector size
        offset = sector_number * bytes_per_sector
        ctypes.windll.kernel32.SetFilePointer(disk_handle, offset, None, 0)

        # Read data from the sector
        buffer_size = bytes_per_sector
        buffer = ctypes.create_string_buffer(buffer_size)
        bytes_read = ctypes.c_ulong(0)

        if ctypes.windll.kernel32.ReadFile(disk_handle, buffer, buffer_size, ctypes.byref(bytes_read), None):
            print(f"Data from sector {sector_number}: {buffer.raw[:bytes_read.value].hex()}")

    finally:
        # Close the disk handle
        ctypes.windll.kernel32.CloseHandle(disk_handle)
