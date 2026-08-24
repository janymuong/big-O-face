---
number: 393
title: "utf-8 validation"
difficulty: medium
tags: [character arrays]
url: https://leetcode.com/problems/utf-8-validation/
---

## problem

given an integer array `data` representing the data, return whether it is a valid UTF‑8 encoding (i.e. it translates to a sequence of valid UTF‑8 encoded characters).

a character in UTF‑8 can be from 1 to 4 bytes long, subjected to the following rules:

- For a 1‑byte character, the first bit is a `0`, followed by its Unicode code.
- For an n‑bytes character, the first n bits are all one's, the n+1 bit is `0`, followed by n‑1 bytes with the most signifExample 2:

Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

 

Constraints:

    1 <= data.length <= 2 * 104
    0 <= data[i] <= 255
icant 2 bits being `10`.

## examples

```
Example 1:

Input:  data = [197,130,1]
Output: true
explanation: data represents the octet sequence: 11000101 10000010 00000001.
it is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

Input: data = [235,140,4]
Output: false
explanation: data represented the octet sequence: 11101011 10001100 00000100.
the first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
the next byte is a continuation byte which starts with 10 and that's correct.
but the second continuation byte does not start with 10, so it is invalid.
```
 

## Constraints:

    1 <= data.length <= 2 * 104
    0 <= data[i] <= 255



