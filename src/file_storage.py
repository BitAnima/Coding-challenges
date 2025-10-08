"""File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
"""
import math

def number_of_files(file_size, file_unit, drive_size_gb):
    files_in_drive = 0

    if file_unit == "B":
        bytes_file_size = file_size
    if file_unit == "KB":
        bytes_file_size = file_size * 1000
    if file_unit == "MB":
        bytes_file_size = file_size * 1000 * 1000
    if file_unit == "GB":
        bytes_file_size = file_size * 1000 * 1000 * 1000

    files_in_drive = math.floor(drive_size_gb * 1000 * 1000 * 1000 / (bytes_file_size))

    print(f"The hard drive has {files_in_drive} files")

    return files_in_drive

number_of_files(500, "KB", 1) # 2000.
number_of_files(50000, "B", 1) # 20000.
number_of_files(5, "MB", 1) # 200.
number_of_files(4096, "B", 1.5) # 366210.
number_of_files(220.5, "KB", 100) # 453514.
number_of_files(4.5, "MB", 750) # 166666.