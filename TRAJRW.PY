# %%
"""
read is read file
write is writing files
"""
import warnings
from glob import glob
from typing import Dict, List, Union
import matplotlib.pyplot as plt
#import numpy as np
#import torch
#import cv2
#import matplotlib


# %%
import numpy as np
from typing import Dict, List, Union, AnyStr
import struct


def read_traj(read_path_str: AnyStr):
    with open(read_path_str, "r") as rf:
        first_line = rf.readline().split("\t")
        data = np.loadtxt(rf, skiprows=0, dtype="float")
        return first_line, data


def write_traj(write_path_str: AnyStr, Headers: List, data: np.ndarray) -> None:
    with open(write_path_str, "w") as wf:
        for i in Headers[:-1]:
            #assr exception
            print(i)
            head = i + "\t"
            wf.write(head)
        wf.write("\n")
        np.savetxt(wf, data, fmt="%20.6f", delimiter="\t", newline="\t\n")



# %%
# with open("C:\\Users\\ORIYU\\Desktop\\K_trajectory\\K_test.txt", "r") as f:
#     all_data = [line.strip("\t") for line in f.readlines()]
#     header_line = all_data[0]
#     h = header_line.split("\t")
#     data = all_data[1:]
# %%
# import numpy as np

# read_path_str = "tests/K_test.txt"
# write_path_str = "tests/new_K_test.txt"
# read_path_str = "C:\\Users\\ORIYU\\Desktop\\K_trajectory\\K_test.txt"
# write_path_str = "C:\\Users\\ORIYU\\Desktop\\K_trajectory\\new_K_test.txt"

read_path_str = "K_test.txt"
write_path_str = "new_K_test.txt"


with open(read_path_str, "r") as rf:
    first_line = rf.readline().split("\t")
    data = np.loadtxt(rf, skiprows=0, dtype="float")

with open(write_path_str, "w") as wf:
    for i in first_line[:-1]:
        print(i)
        head = i + "\t"
        wf.write(head)
    wf.write("\n")
    np.savetxt(wf, data, fmt="%20.6f", delimiter="\t", newline="\t\n")

# %%
import filecmp

# a = "tests/K_test.txt"
# b = "tests/new_K_test.txt"

a = "K_test.txt"
b = "new_K_test.txt"
#b = "b.txt"

cmp_res = filecmp.cmp(a, b)
print(cmp_res)
# %%
