'''
    My solution for "Find the Index of the First Occurrence in a String"
    https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
