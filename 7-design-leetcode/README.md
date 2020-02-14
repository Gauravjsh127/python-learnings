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

## Problem 5 : Breadth First Algorithm python

 BFS implements a specific strategy for visiting all the nodes (vertices) of a graph

 BFS starts from a node, then it checks all the nodes at distance one from the starting node, then it checks all the nodes at distance two and so on. In order to remember the nodes to be visited, BFS uses a queue. The algorithm can keep track of the vertices it has already checked to avoid revisiting them, in case a graph had one or more cycles.

BFS :  Use Queue

## Problem 6 : Depth first search Algorithm

 BFS implements a specific strategy for visiting all the nodes (vertices) of a graph

Depth First Traversal (or Search) for a graph is similar to Depth First Traversal (DFS) of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array.

DFS :  Use Stack


## Problem 7 : Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
