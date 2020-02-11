# Design leetcode examples

This modules provide sample python code solving the leet code problems related to Design

# Category : Easy problems

## Problem 1: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
## Problem 2: shuffle array

Shuffle a set of numbers without duplicates.
Example:// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);
// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();
// Resets the array back to its original configuration [1,2,3].
solution.reset();
// Returns the random shuffling of array [1,2,3].
solution.shuffle();


## Problem 3 : Top k frequent words   ???????

Top K Frequent WordsYour answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1: Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2 Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words. Note that "i" comes before "love" due to a lower alphabetical order.
Example 2: Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"] Explanation: "the", "is", "sunny" and "day" are the four most frequent words,with the number of occurrence being 4, 3, 2 and 1 respectively.

## Problem 4 : Last 3 websites visited

Example 1:  AABBBCCCCDDDDDDABBBBB 
output : BAD


