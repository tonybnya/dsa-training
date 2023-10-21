#!/usr/bin/python3
"""
Leetcode 217. Contains duplicate
Category: Easy

Given an integer array 'nums'.
Return 'true' if any value appears "at least twice" in the array,
and return 'false' if every element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
"""
from typing import List


def solution1(nums: List[int]) -> bool:
    """Solution1: Brute Force 
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums) - 1): # O(n)
        if nums[i] in nums[i + 1:]: # O(n)
            return True

    return False


def solution2(nums: List[int]) -> bool:
    """Solution2: Sorting
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    nums.sort() # O(nlogn)
    for i in range(len(nums) - 1): # O(n)
        if nums[i] == nums[i + 1]:
            return True

    return False


def solution3(nums: List[int]) -> bool:
    """Solution3: Hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hmap = {} # O(n)

    for num in nums: # O(n)
        if num in hmap:
            return True
        hmap[num] = hmap.get(num, 0) + 1

    return False


def solution4(nums: List[int]) -> bool:
    """Solution 4: Hashset
    Time Complexity: O()
    Space Complexity: O()
    """
    hset = set()

    for num in nums:
        if num in hset:
            return True
        hset.add(num)

    return False


if __name__ == '__main__':
    tests = []

    with open('input.txt') as file:
        lines = file.readlines()

        for line in lines:
            test = {}
            nums = []

            lst = line.strip().split()
            for item in lst:
                if item is not lst[-1]:
                    nums.append(int(item))
                else:
                    expected = eval(lst[-1])
            
            got = solution4(nums)
            test_passed = got == expected
            test.update({
                'input': nums,
                'expected': expected,
                'got': got,
                'test_passed': test_passed 
            })

            tests.append(test)

    for i, test in enumerate(tests, start=1):
        print(f'Example {i}:')
        print(f'Input: nums = {test.get("input")}')
        print(f'Expected: {test.get("expected")}')
        print(f'Got: {test.get("got")}')

        if test.get('test_passed'):
            print("Test Passed! ✅")
        else:
            print("Test Failed! ❌")

        print()
