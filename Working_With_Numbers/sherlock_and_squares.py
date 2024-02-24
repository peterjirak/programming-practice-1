"""
SHERLOCK AND SQUARES

Source: https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

Watson likes to challenge Sherlock's math ability. He will provide a starting
and ending value that describe a range of integers, inclusive of the endpoints.
Sherlock must determine the number of square integers within that range.

Note: A square integer is an integer which is the square of an integer, e.g. 1, 4, 9, 16, 25.

Example:
a: 24
B: 40

There are three square integers in the range: 25, 36 and 49. Return 3.

Function Description

Complete the squares function in the editor below. It should return an integer
representing the number of square integers in the inclusive range from  a to b.

squares has the following parameter(s):
 * int a: the lower range boundary
 * int b: the upper range boundary

Returns
 * int: the number of square integers in the range

Input Format
 * The first line contains q, the number of test cases.
 * Each of the next q lines contains two space-separated integers, a and b, the
   starting and ending integers in the ranges.

Constraints
 * 1 ≤ q ≤ 100
 1 ≤ a ≤ b ≤ 10 ** 9

Sample Input

    2
    3 9
    17 24

Sample Output

    2
    0

Explanation

 * Test Case #00: In range [3, 9], 4 and 9 are the two square integers.
 * Test Case #01: In range [17, 24], there are no square integers.

"""

def is_square(num):
    root = num ** 0.5
    root_floor = float(math.floor(root))
    return True if root == root_floor else False

def squares(a, b):
    # Write your code here
    square_count = 0
    for i in range(a, b + 1):
        square_count += 1 if is_square(i) else 0
    return square_count
