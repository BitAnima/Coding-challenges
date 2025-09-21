"""Video Storage
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
If not given one of the video units above, return "Invalid video unit".
The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
If not given one of the hard drive units above, return "Invalid drive unit".
Return the number of whole videos the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB
For example, given 500, "MB", 100, and "GB as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
"""

import math

def number_of_videos(video_size, video_unit, drive_size, drive_unit):

    video_allowed_capacity_units = {'KB', 'MB', 'GB'} #Set of allowed units (no duplicates allowed, no position either)
    hard_drive_allowed_capacity_units = {'GB', 'TB'}

    if video_unit not in video_allowed_capacity_units:
        print("Invalid video unit")
        return "Invalid video unit"
    if drive_unit not in hard_drive_allowed_capacity_units:
        print("Invalid drive unit")
        return "Invalid drive unit"

    if video_unit == "B":
        bytes_video_size = video_size
    if video_unit == "KB":
        bytes_video_size = video_size * 1000
    if video_unit == "MB":
        bytes_video_size = video_size * 1000 * 1000
    if video_unit == "GB":
        bytes_video_size = video_size * 1000 * 1000 * 1000
    if drive_unit == "GB":
        bytes_drive_size = drive_size * 1000 * 1000 * 1000
    if drive_unit == "TB":
        bytes_drive_size = drive_size * 1000 * 1000 * 1000 * 1000

    videos_in_drive = math.floor(bytes_drive_size / bytes_video_size)
    print(videos_in_drive)

    return videos_in_drive

number_of_videos(500, "MB", 100, "GB") # 200.
number_of_videos(2000, "B", 1, "TB") # "Invalid video unit".
number_of_videos(2000, "MB", 100000, "MB") # "Invalid drive unit".
number_of_videos(500000, "KB", 2, "TB") # 4000.
number_of_videos(1.5, "GB", 2.2, "TB") # 1466.