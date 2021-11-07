#!/usr/bin/python3 

import random
import math

def getTopSites():
    sites = []
    with open('topsites.txt', 'r') as f:
        data = f.readline()
        while data:
            sites.append(data)
            data = f.readline()
    return sites

def buildUserProfile(parentSet):
    n = max(len(parentSet), 30)
    browsingHistory = random.choices(parentSet, k=randint(20,n))
    return browsingHistory

# simhash: https://pythonrepo.com/repo/hybridtheory-floc-simhash-python-python-implementation-of-algorithms-and-design-patterns
# wicg-floc: https://github.com/WICG/floc 