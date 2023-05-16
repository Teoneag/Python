import os
import pathlib
dir_path = "C:/Users/teodo/Downloads/New folder (2)/New folder/"
for count, file_name in enumerate(os.listdir(dir_path)):
    if pathlib.Path(file_name).suffix == ".mp4":
        os.rename(dir_path + file_name, dir_path + "Photo_" + str(count) + ".mp4")