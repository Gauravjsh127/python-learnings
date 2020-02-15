# Strings leetcode examples

This modules provide sample python code solving the leet code problems related to Strings

# Category : Easy problems

## Problem 1 : Reverse string

Write a function that reverses a string. The input string is given as an array of characters char[]
Example 1: Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

## Problem 2 : Number Reverse

Given a 32-bit signed integer, reverse digits of an integer.
Example 1: Input: 123 Output: 321
Example 2: Input: -123 Output: -321
Example 3: Input: 120 Output: 21

## Problem 3 : First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples: s = "leetcode" return 0.
s = "loveleetcode", return 2.


## Problem 4 : Valid anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1: Input: s = "anagram", t = "nagaram" Output: true 
Example 2: Input: s = "rat", t = "car" Output: false

## Problem 5 : Valid palindrom

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1: Input: "A man, a plan, a canal: Panama" Output: true
Example 2: Input: "race a car" Output: false

## Problem 6 : String to Integer

String to Integer
Example 1: Input: "42" Output: 42

## Problem 7 : First-occurance of substring in string : KMP algorithm

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1: Input: haystack = "hello", needle = "ll" Output: 2
Example 2: Input: haystack = "aaaaa", needle = "bba" Output: -1

String : M substring :N
Brute force : https://nulpointerexception.com/2019/02/10/a-beginner-guide-to-brute-force-algorithm-for-substring-search/  O(M * N)


KMP algorithm:  O(M + N)

Firts compute longest suffix that is also prefix : ie kmp matrx 
https://www.youtube.com/watch?v=KG44VoDtsAA


## Problem 8 : Longest prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1: Input: ["flower","flow","flight"] Output: "fl"
Example 2: Input: ["dog","racecar","car"] Output: ""
Explanation: There is no common prefix among the input strings.

## Problem 9 : Find all anagrams in the string
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1: Input: ["flower","flow","flight"] Output: "fl"
Example 2: Input: ["dog","racecar","car"] Output: ""
Explanation: There is no common prefix among the input strings.

Example 1: Input:
s: "cbaebabacd" p: "abc" Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2: Input: s: "abab" p: "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

## Problem 10

Photo album order

Input :
photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22

output :
'Warsaw02.jpg', 'London1.png'