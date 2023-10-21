#!/usr/bin/python3
"""
Leetcode 242. Valid Anagram
Category: Easy

Given two strings 's' and 't'.
Return 'true' if 't' is an anagram of 's', and 'false' otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
def helper(chars: str) -> dict:
    """Helper function to create an hashmap/dict corresponding to
    the char/occurence (key/value) of a string
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hmap = {}

    for ch in chars:
        hmap[ch] = hmap.get(ch, 0) + 1

    return hmap


def solution1(s: str, t: str) -> bool:
    """Solution 1: Hashmap
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    if len(s) != len(t):
        return False

    hmap_s = helper(s)
    hmap_t = helper(t)

    for key in hmap_s:
        if hmap_s[key] != hmap_t.get(key, 0):
            return False

    return True


def solution2(s: str, t: str) -> bool:
    """Solution 2: Hashset
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    if len(s) != len(t):
        return False

    hset_s = set(s)
    hset_t = set(t)

    return hset_s == hset_t


def solution3(s: str, t: str) -> bool:
    """Solution 3: Sorting
    Time Complexity: O(nlogn + mlogm)
    Space Complexity: O(1)
    """
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    for i in range(len(s)):
        if s[i] != t[i]:
            return False
        
    return True


def solution4(s: str, t: str) -> bool:
    """Solution4: Counter class of collections module
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    from collections import Counter

    return Counter(s) == Counter(t)


def solution5(s: str, t: str) -> bool:
    """Solution 5: Sorting & two pointers comparisons
    Time Complexity: O(nlogn + mlogm)
    Space Complexity: O(1)
    """
    s = sorted(s)
    t = sorted(t)

    if len(s) != len(t):
        return False

    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            return False
    
    return True


if __name__ == '__main__':
    tests = []

    with open('input.txt') as file:
        lines = file.readlines()

        for line in lines:
            test = {}
            lst = (line.strip().split())

            s = lst[0]
            t = lst[1]
            got = solution3(s, t)
            expected = eval(lst[-1])

            test.update({
                's': s,
                't': t,
                'got': got,
                'expected': expected
            })

            tests.append(test)

    for i, test in enumerate(tests, start=1):
        print(f"Example {i}:")
        print(f"Input: s = {test.get('s')}, t = {test.get('t')}")
        print(f"Expected: {test.get('expected')}")
        print(f"Got: {test.get('got')}")

        if test.get('got') == test.get('expected'):
            print('Test Passed! ✅')
        else:
            print('Test Passed! ❌')
        print()