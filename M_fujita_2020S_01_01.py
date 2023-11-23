#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# M_fujita_2020S_01_01.py
#
# Copyright (c) 2021-2023 shihashi
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

from os.path import basename
import sys
import itertools

DEFAULT_ONE_SIDE_LENGTH = 3


def fujita_MMXX_S(osl: int) -> int:
    cc = itertools.product(itertools.combinations(range(1, osl* 2 - 1), osl - 1), repeat=2)
    answer = 0
    for r1, r2 in cc:
        cross = False
        for i in range(len(r1)):
            if r1[i] > r2[i]:
                cross = True
                break
        if not cross:
            answer += 1

    return answer

def main():
    one_side_length = DEFAULT_ONE_SIDE_LENGTH
    if len(sys.argv) == 2:
        try:
            one_side_length = int(sys.argv[1])
            if one_side_length <= 0:
                raise ValueError("The auguments must be positive integer: '{}'"
.format(one_side_length))
        except ValueError as e:
            print(e, file = sys.stderr)
            sys.exit(1)
    elif len(sys.argv) != 1:
        usage()

    answer = fujita_MMXX_S(one_side_length)
    print(answer * 2)

def usage():
    print("""
usage:

    python {} [one_side_length]

""".format(basename(sys.argv[0])))
    sys.exit(1)


if __name__ == '__main__':
    main()
