#!/usr/bin/env python3

# Created by venika Sem
# Created on Nov 2022
# This program displays value of rgb


def main():
    # This function displays value of rgb
    for i in range(256):
        for j in range(256):
            for k in range(256):
                print("RGB({0},{1},{2})".format(i, j, k))
    print("\nDone.")


if __name__ == "__main__":
    main()
