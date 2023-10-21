#!/usr/bin/env python3
"""
Leetcode 1. Two Sum
Category: Easy

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Example 4:
Input: nums = [2, 5, 1, 3], target = 4
Output: [1, 3]
"""
from typing import List


def solution1(nums: List[int], target: int) -> List[int]:
    """Solution 1: Brute Force
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def solution2(nums: List[int], target: int) -> List[int]:
    """Solution 2: Hasmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    hmap = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff not in hmap:
            hmap.update({num: i})
        else:
            return [hmap.get(diff), i]
    
    return


if __name__ == '__main__':
    with open('input.txt') as file:
        tests = []
        lines = file.readlines()

        for i in range(0, len(lines), 3):
            nums = [int(num) for num in lines[i].strip().split()]
            target = int(lines[i + 1].strip())
            expected = [int(num) for num in lines[i + 2].strip().split()]

            test = {
                'nums': nums,
                'target': target,
                'expected': expected
            }

            tests.append(test)

    for i, test in enumerate(tests, start=1):
        nums = test.get('nums')
        target = test.get('target')
        expected = test.get('expected')
        got = solution2(nums, target)

        print(f"Example {i}:")
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {test.get('expected')}")
        print(f"Got: {got}")

        if got == expected:
            print('Test Passed! ✅')
        else:
            print('Test Passed! ❌')

        print()