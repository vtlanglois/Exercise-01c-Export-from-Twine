#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {}

if "name" in world and "passages" in world:
    print(world["name"])
    print()
    for passage in world["passages"]:
        print(passage["name"])
        print(passage["cleanText"])
        for link in passage["links"]:
            print(link["linkText"])
        print()