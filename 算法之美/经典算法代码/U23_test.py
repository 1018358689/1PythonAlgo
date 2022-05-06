# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:38:20 2019

@author: 111
"""

def sunday_find(src, dst):
    len_src = len(src)
    len_dst = len(dst)
    i = 0
    while i < len_src - len_dst + 1:
        flag = 0
        shift = len_dst
        for j in range(0, len_dst):
            if src[i+j] != dst[j]:
                flag = -1
                break

        if flag == 0:
            return i

        p = dst.rfind(src[i+shift])
        if p == -1:
            shift = len_dst + 1
        else:
            shift = len_dst - p

        i = i + shift

    return -1


if __name__ == "__main__":
    text = "here_examplfe_v_example"
    pattern = "ple"
    pos = sunday_find(text, pattern)
    print(pos)
