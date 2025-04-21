# Problem 2015: Average Height of Buildings in Each Segment
# Difficulty: Medium
# Description:
# <p>A perfectly straight street is represented by a number line. The street has building(s) on it and is represented by a 2D integer array <code>buildings</code>, where <code>buildings[i] = [start<sub>i</sub>, end<sub>i</sub>, height<sub>i</sub>]</code>. This means that there is a building with <code>height<sub>i</sub></code> in the <strong>half-closed segment</strong> <code>[start<sub>i</sub>, end<sub>i</sub>)</code>.</p>
# <p>You want to <strong>describe</strong> the heights of the buildings on the street with the <strong>minimum</strong> number of non-overlapping <strong>segments</strong>. The street can be represented by the 2D integer array <code>street</code> where <code>street[j] = [left<sub>j</sub>, right<sub>j</sub>, average<sub>j</sub>]</code> describes a <strong>half-closed segment</strong> <code>[left<sub>j</sub>, right<sub>j</sub>)</code> of the road where the <strong>average</strong> heights of the buildings in the<strong> segment</strong> is <code>average<sub>j</sub></code>.</p>
# <ul>
# 	<li>For example, if <code>buildings = [[1,5,2],[3,10,4]],</code> the street could be represented by <code>street = [[1,3,2],[3,5,3],[5,10,4]]</code> because:
#     <ul>
#     	<li>From 1 to 3, there is only the first building with an average height of <code>2 / 1 = 2</code>.</li>
#     	<li>From 3 to 5, both the first and the second building are there with an average height of <code>(2+4) / 2 = 3</code>.</li>
#     	<li>From 5 to 10, there is only the second building with an average height of <code>4 / 1 = 4</code>.</li>
#     </ul>
#     </li>
# </ul>
# <p>Given <code>buildings</code>, return <em>the 2D integer array </em><code>street</code><em> as described above (<strong>excluding</strong> any areas of the street where there are no buldings). You may return the array in <strong>any order</strong></em>.</p>
# <p>The <strong>average</strong> of <code>n</code> elements is the <strong>sum</strong> of the <code>n</code> elements divided (<strong>integer division</strong>) by <code>n</code>.</p>
# <p>A <strong>half-closed segment</strong> <code>[a, b)</code> is the section of the number line between points <code>a</code> and <code>b</code> <strong>including</strong> point <code>a</code> and <strong>not including</strong> point <code>b</code>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2015.Average%20Height%20of%20Buildings%20in%20Each%20Segment/images/image-20210921224001-2.png" style="width: 500px; height: 349px;" />
# <pre>
# <strong>Input:</strong> buildings = [[1,4,2],[3,9,4]]
# <strong>Output:</strong> [[1,3,2],[3,4,3],[4,9,4]]
# <strong>Explanation:</strong>
# From 1 to 3, there is only the first building with an average height of 2 / 1 = 2.
# From 3 to 4, both the first and the second building are there with an average height of (2+4) / 2 = 3.
# From 4 to 9, there is only the second building with an average height of 4 / 1 = 4.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> buildings = [[1,3,2],[2,5,3],[2,8,3]]
# <strong>Output:</strong> [[1,3,2],[3,8,3]]
# <strong>Explanation:</strong>
# From 1 to 2, there is only the first building with an average height of 2 / 1 = 2.
# From 2 to 3, all three buildings are there with an average height of (2+3+3) / 3 = 2.
# From 3 to 5, both the second and the third building are there with an average height of (3+3) / 2 = 3.
# From 5 to 8, there is only the last building with an average height of 3 / 1 = 3.
# The average height from 1 to 3 is the same so we can group them into one segment.
# The average height from 3 to 8 is the same so we can group them into one segment.
# </pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre>
# <strong>Input:</strong> buildings = [[1,2,1],[5,6,1]]
# <strong>Output:</strong> [[1,2,1],[5,6,1]]
# <strong>Explanation:</strong>
# From 1 to 2, there is only the first building with an average height of 1 / 1 = 1.
# From 2 to 5, there are no buildings, so it is not included in the output.
# From 5 to 6, there is only the second building with an average height of 1 / 1 = 1.
# We cannot group the segments together because an empty space with no buildings seperates the segments.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= buildings.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>buildings[i].length == 3</code></li>
# 	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
# 	<li><code>1 &lt;= height<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from collections import defaultdict


class Solution:
    def averageHeightOfBuildings(self, buildings):
        height = defaultdict(int)
        cnt = defaultdict(int)
        for s, e, h in buildings:
            cnt[s] += 1
            cnt[e] -= 1
            height[s] += h
            height[e] -= h
        ans = []
        i = h = n = 0
        for j in sorted(cnt.keys()):
            if n:
                t = [i, j, h // n]
                if ans and ans[-1][1] == i and ans[-1][2] == t[-1]:
                    ans[-1][1] = j
                else:
                    ans.append(t)
            i = j
            h += height[j]
            n += cnt[j]
        return ans

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.averageHeightOfBuildings([[7, 12, 7], [6, 8, 5]]) == [[6, 7, 5], [7, 8, 6], [8, 12, 7]]
assert solution.averageHeightOfBuildings([[3, 9, 2], [10, 15, 4], [3, 9, 1], [7, 12, 3]]) == [[3, 7, 1], [7, 9, 2], [9, 12, 3], [12, 15, 4]]
assert solution.averageHeightOfBuildings([[1, 11, 10], [7, 14, 1]]) == [[1, 7, 10], [7, 11, 5], [11, 14, 1]]
assert solution.averageHeightOfBuildings([[8, 15, 1], [2, 10, 4], [8, 14, 8], [6, 15, 9], [9, 19, 6]]) == [[2, 6, 4], [6, 8, 6], [8, 10, 5], [10, 14, 6], [14, 15, 5], [15, 19, 6]]
assert solution.averageHeightOfBuildings([[3, 9, 2], [3, 12, 1], [9, 12, 3]]) == [[3, 9, 1], [9, 12, 2]]
assert solution.averageHeightOfBuildings([[9, 12, 3], [9, 10, 4], [4, 9, 4], [5, 7, 5]]) == [[4, 9, 4], [9, 12, 3]]
assert solution.averageHeightOfBuildings([[3, 8, 2], [7, 9, 7], [5, 15, 2], [3, 9, 7], [2, 7, 3]]) == [[2, 3, 3], [3, 5, 4], [5, 7, 3], [7, 8, 4], [8, 9, 5], [9, 15, 2]]
assert solution.averageHeightOfBuildings([[8, 16, 1], [8, 9, 4]]) == [[8, 9, 2], [9, 16, 1]]
assert solution.averageHeightOfBuildings([[4, 8, 1]]) == [[4, 8, 1]]
assert solution.averageHeightOfBuildings([[6, 10, 6], [6, 16, 2]]) == [[6, 10, 4], [10, 16, 2]]
assert solution.averageHeightOfBuildings([[5, 14, 10], [6, 14, 7], [3, 10, 10], [8, 15, 10]]) == [[3, 6, 10], [6, 14, 9], [14, 15, 10]]
assert solution.averageHeightOfBuildings([[7, 14, 3], [10, 12, 4], [8, 9, 5], [3, 6, 6]]) == [[3, 6, 6], [7, 8, 3], [8, 9, 4], [9, 14, 3]]
assert solution.averageHeightOfBuildings([[1, 2, 3], [10, 12, 1]]) == [[1, 2, 3], [10, 12, 1]]
assert solution.averageHeightOfBuildings([[1, 5, 5]]) == [[1, 5, 5]]
assert solution.averageHeightOfBuildings([[4, 9, 5], [3, 13, 8], [2, 10, 1]]) == [[2, 3, 1], [3, 10, 4], [10, 13, 8]]
assert solution.averageHeightOfBuildings([[5, 13, 4], [4, 10, 8]]) == [[4, 5, 8], [5, 10, 6], [10, 13, 4]]
assert solution.averageHeightOfBuildings([[3, 12, 10], [1, 3, 7], [10, 19, 8]]) == [[1, 3, 7], [3, 10, 10], [10, 12, 9], [12, 19, 8]]
assert solution.averageHeightOfBuildings([[6, 8, 7], [2, 5, 7], [5, 12, 8], [10, 17, 6], [7, 11, 10]]) == [[2, 5, 7], [5, 6, 8], [6, 7, 7], [7, 8, 8], [8, 10, 9], [10, 11, 8], [11, 12, 7], [12, 17, 6]]
assert solution.averageHeightOfBuildings([[3, 13, 5], [6, 14, 10]]) == [[3, 6, 5], [6, 13, 7], [13, 14, 10]]
assert solution.averageHeightOfBuildings([[4, 11, 2]]) == [[4, 11, 2]]
assert solution.averageHeightOfBuildings([[10, 14, 9], [1, 6, 7], [5, 15, 1]]) == [[1, 5, 7], [5, 6, 4], [6, 10, 1], [10, 14, 5], [14, 15, 1]]
assert solution.averageHeightOfBuildings([[9, 16, 7]]) == [[9, 16, 7]]
assert solution.averageHeightOfBuildings([[10, 12, 9], [1, 8, 4], [10, 19, 4]]) == [[1, 8, 4], [10, 12, 6], [12, 19, 4]]
assert solution.averageHeightOfBuildings([[6, 10, 7], [10, 20, 10], [4, 7, 1]]) == [[4, 6, 1], [6, 7, 4], [7, 10, 7], [10, 20, 10]]
assert solution.averageHeightOfBuildings([[1, 10, 9], [7, 14, 10], [3, 8, 9], [10, 15, 3], [1, 11, 4]]) == [[1, 3, 6], [3, 7, 7], [7, 8, 8], [8, 10, 7], [10, 11, 5], [11, 14, 6], [14, 15, 3]]
assert solution.averageHeightOfBuildings([[1, 9, 2], [3, 11, 8]]) == [[1, 3, 2], [3, 9, 5], [9, 11, 8]]
assert solution.averageHeightOfBuildings([[10, 15, 7], [6, 9, 8], [2, 5, 6], [8, 18, 8]]) == [[2, 5, 6], [6, 10, 8], [10, 15, 7], [15, 18, 8]]
assert solution.averageHeightOfBuildings([[10, 16, 5]]) == [[10, 16, 5]]
assert solution.averageHeightOfBuildings([[5, 15, 3], [5, 6, 2], [10, 18, 7]]) == [[5, 6, 2], [6, 10, 3], [10, 15, 5], [15, 18, 7]]
assert solution.averageHeightOfBuildings([[6, 16, 6], [6, 13, 2], [7, 8, 6], [3, 6, 8], [6, 16, 2]]) == [[3, 6, 8], [6, 7, 3], [7, 8, 4], [8, 13, 3], [13, 16, 4]]
assert solution.averageHeightOfBuildings([[6, 8, 10], [9, 11, 10], [5, 11, 6], [6, 8, 10]]) == [[5, 6, 6], [6, 8, 8], [8, 9, 6], [9, 11, 8]]
assert solution.averageHeightOfBuildings([[9, 17, 7], [5, 6, 9], [1, 7, 1], [10, 11, 5], [4, 10, 1]]) == [[1, 5, 1], [5, 6, 3], [6, 9, 1], [9, 10, 4], [10, 11, 6], [11, 17, 7]]
assert solution.averageHeightOfBuildings([[6, 14, 5], [8, 10, 10], [2, 6, 3], [4, 8, 8], [10, 17, 9]]) == [[2, 4, 3], [4, 6, 5], [6, 8, 6], [8, 14, 7], [14, 17, 9]]
assert solution.averageHeightOfBuildings([[10, 12, 9], [1, 10, 7]]) == [[1, 10, 7], [10, 12, 9]]
assert solution.averageHeightOfBuildings([[1, 8, 2], [7, 10, 9], [8, 15, 9], [2, 12, 7], [10, 18, 1]]) == [[1, 2, 2], [2, 7, 4], [7, 8, 6], [8, 10, 8], [10, 15, 5], [15, 18, 1]]
assert solution.averageHeightOfBuildings([[2, 3, 7]]) == [[2, 3, 7]]
assert solution.averageHeightOfBuildings([[10, 14, 1], [9, 15, 8], [10, 13, 5], [9, 15, 7]]) == [[9, 10, 7], [10, 14, 5], [14, 15, 7]]
assert solution.averageHeightOfBuildings([[6, 12, 9], [8, 17, 2], [6, 13, 10]]) == [[6, 8, 9], [8, 12, 7], [12, 13, 6], [13, 17, 2]]
assert solution.averageHeightOfBuildings([[10, 18, 2], [9, 15, 10], [2, 4, 4]]) == [[2, 4, 4], [9, 10, 10], [10, 15, 6], [15, 18, 2]]
assert solution.averageHeightOfBuildings([[3, 6, 5]]) == [[3, 6, 5]]
assert solution.averageHeightOfBuildings([[1, 2, 9], [6, 8, 5]]) == [[1, 2, 9], [6, 8, 5]]
assert solution.averageHeightOfBuildings([[3, 11, 8], [10, 14, 1], [9, 18, 2], [10, 14, 10], [7, 13, 8]]) == [[3, 9, 8], [9, 10, 6], [10, 13, 5], [13, 14, 4], [14, 18, 2]]
assert solution.averageHeightOfBuildings([[8, 11, 1], [4, 5, 3], [6, 8, 3]]) == [[4, 5, 3], [6, 8, 3], [8, 11, 1]]
assert solution.averageHeightOfBuildings([[2, 9, 3], [10, 17, 4], [10, 20, 7]]) == [[2, 9, 3], [10, 17, 5], [17, 20, 7]]
assert solution.averageHeightOfBuildings([[10, 16, 7], [10, 12, 10]]) == [[10, 12, 8], [12, 16, 7]]
assert solution.averageHeightOfBuildings([[3, 9, 8], [1, 4, 5], [9, 11, 7], [5, 10, 10], [8, 14, 2]]) == [[1, 3, 5], [3, 4, 6], [4, 5, 8], [5, 8, 9], [8, 10, 6], [10, 11, 4], [11, 14, 2]]
assert solution.averageHeightOfBuildings([[2, 12, 3], [10, 13, 3]]) == [[2, 13, 3]]
assert solution.averageHeightOfBuildings([[9, 10, 4], [8, 16, 7], [1, 6, 8], [3, 9, 2], [7, 11, 10]]) == [[1, 3, 8], [3, 6, 5], [6, 7, 2], [7, 9, 6], [9, 10, 7], [10, 11, 8], [11, 16, 7]]
assert solution.averageHeightOfBuildings([[5, 14, 2], [7, 14, 6], [6, 8, 8], [7, 8, 6], [5, 13, 7]]) == [[5, 6, 4], [6, 13, 5], [13, 14, 4]]
assert solution.averageHeightOfBuildings([[10, 15, 9], [2, 12, 1], [6, 14, 7], [10, 18, 2], [9, 12, 9]]) == [[2, 6, 1], [6, 9, 4], [9, 12, 5], [12, 14, 6], [14, 15, 5], [15, 18, 2]]
assert solution.averageHeightOfBuildings([[10, 12, 6], [5, 12, 9], [7, 11, 5]]) == [[5, 7, 9], [7, 10, 7], [10, 11, 6], [11, 12, 7]]
assert solution.averageHeightOfBuildings([[10, 13, 8], [4, 14, 5], [10, 20, 1], [10, 20, 3], [7, 12, 3]]) == [[4, 7, 5], [7, 13, 4], [13, 14, 3], [14, 20, 2]]
assert solution.averageHeightOfBuildings([[7, 15, 2], [3, 4, 9], [9, 17, 9], [6, 11, 9], [9, 12, 9]]) == [[3, 4, 9], [6, 7, 9], [7, 9, 5], [9, 11, 7], [11, 12, 6], [12, 15, 5], [15, 17, 9]]
assert solution.averageHeightOfBuildings([[8, 13, 4], [3, 12, 8], [2, 6, 9], [5, 9, 6]]) == [[2, 3, 9], [3, 5, 8], [5, 8, 7], [8, 12, 6], [12, 13, 4]]
assert solution.averageHeightOfBuildings([[7, 16, 5]]) == [[7, 16, 5]]
assert solution.averageHeightOfBuildings([[8, 10, 4], [3, 10, 7], [8, 17, 3]]) == [[3, 8, 7], [8, 10, 4], [10, 17, 3]]
assert solution.averageHeightOfBuildings([[6, 9, 9], [3, 8, 8]]) == [[3, 8, 8], [8, 9, 9]]
assert solution.averageHeightOfBuildings([[4, 14, 3], [10, 19, 4]]) == [[4, 14, 3], [14, 19, 4]]
assert solution.averageHeightOfBuildings([[4, 13, 8], [10, 19, 7], [6, 10, 2], [6, 16, 9], [7, 17, 9]]) == [[4, 6, 8], [6, 7, 6], [7, 10, 7], [10, 17, 8], [17, 19, 7]]
assert solution.averageHeightOfBuildings([[7, 8, 10], [9, 19, 6], [2, 12, 5], [10, 19, 3], [5, 9, 1]]) == [[2, 5, 5], [5, 7, 3], [7, 8, 5], [8, 9, 3], [9, 10, 5], [10, 19, 4]]
assert solution.averageHeightOfBuildings([[6, 13, 10], [4, 13, 3], [9, 15, 8], [4, 10, 3], [6, 9, 4]]) == [[4, 6, 3], [6, 9, 5], [9, 10, 6], [10, 13, 7], [13, 15, 8]]
assert solution.averageHeightOfBuildings([[3, 4, 6], [5, 14, 6], [2, 9, 6], [8, 10, 6], [7, 14, 9]]) == [[2, 7, 6], [7, 8, 7], [8, 9, 6], [9, 14, 7]]
assert solution.averageHeightOfBuildings([[10, 19, 10], [10, 14, 1]]) == [[10, 14, 5], [14, 19, 10]]
assert solution.averageHeightOfBuildings([[7, 12, 2], [5, 6, 9]]) == [[5, 6, 9], [7, 12, 2]]
assert solution.averageHeightOfBuildings([[1, 3, 9], [3, 10, 7], [3, 11, 1], [8, 18, 5]]) == [[1, 3, 9], [3, 10, 4], [10, 11, 3], [11, 18, 5]]
assert solution.averageHeightOfBuildings([[2, 7, 2], [9, 10, 9], [9, 13, 9]]) == [[2, 7, 2], [9, 13, 9]]
assert solution.averageHeightOfBuildings([[6, 8, 2], [6, 8, 5], [1, 6, 9], [3, 9, 8], [5, 15, 1]]) == [[1, 3, 9], [3, 5, 8], [5, 6, 6], [6, 9, 4], [9, 15, 1]]
assert solution.averageHeightOfBuildings([[5, 11, 3], [5, 14, 5], [4, 9, 7], [5, 15, 2], [3, 7, 4]]) == [[3, 4, 4], [4, 5, 5], [5, 9, 4], [9, 14, 3], [14, 15, 2]]
assert solution.averageHeightOfBuildings([[7, 17, 10], [1, 2, 8], [9, 14, 1]]) == [[1, 2, 8], [7, 9, 10], [9, 14, 5], [14, 17, 10]]
assert solution.averageHeightOfBuildings([[9, 15, 4], [10, 16, 2]]) == [[9, 10, 4], [10, 15, 3], [15, 16, 2]]
assert solution.averageHeightOfBuildings([[1, 10, 10], [7, 10, 4], [9, 10, 5], [8, 14, 8]]) == [[1, 7, 10], [7, 9, 7], [9, 10, 6], [10, 14, 8]]
assert solution.averageHeightOfBuildings([[8, 9, 2]]) == [[8, 9, 2]]
assert solution.averageHeightOfBuildings([[6, 16, 2], [5, 12, 9], [3, 8, 10], [6, 14, 4], [1, 8, 4]]) == [[1, 3, 4], [3, 6, 7], [6, 12, 5], [12, 14, 3], [14, 16, 2]]
assert solution.averageHeightOfBuildings([[2, 5, 9], [6, 14, 6], [3, 8, 3]]) == [[2, 3, 9], [3, 5, 6], [5, 6, 3], [6, 8, 4], [8, 14, 6]]
assert solution.averageHeightOfBuildings([[2, 9, 6]]) == [[2, 9, 6]]
assert solution.averageHeightOfBuildings([[9, 17, 10]]) == [[9, 17, 10]]
assert solution.averageHeightOfBuildings([[7, 8, 7], [4, 9, 5]]) == [[4, 7, 5], [7, 8, 6], [8, 9, 5]]
assert solution.averageHeightOfBuildings([[9, 16, 6], [4, 13, 9], [3, 9, 3], [9, 15, 1]]) == [[3, 4, 3], [4, 9, 6], [9, 13, 5], [13, 15, 3], [15, 16, 6]]
assert solution.averageHeightOfBuildings([[8, 18, 3], [10, 18, 4]]) == [[8, 18, 3]]
assert solution.averageHeightOfBuildings([[10, 13, 5], [7, 9, 7], [4, 9, 8]]) == [[4, 7, 8], [7, 9, 7], [10, 13, 5]]
assert solution.averageHeightOfBuildings([[1, 6, 6], [6, 12, 1]]) == [[1, 6, 6], [6, 12, 1]]
assert solution.averageHeightOfBuildings([[2, 5, 8], [9, 17, 9], [2, 10, 6]]) == [[2, 5, 7], [5, 9, 6], [9, 10, 7], [10, 17, 9]]
assert solution.averageHeightOfBuildings([[3, 12, 5], [5, 10, 3], [3, 9, 8]]) == [[3, 5, 6], [5, 9, 5], [9, 10, 4], [10, 12, 5]]
assert solution.averageHeightOfBuildings([[8, 15, 3], [10, 12, 9], [3, 12, 2], [5, 11, 7]]) == [[3, 5, 2], [5, 10, 4], [10, 11, 5], [11, 12, 4], [12, 15, 3]]
assert solution.averageHeightOfBuildings([[2, 5, 4], [2, 8, 5]]) == [[2, 5, 4], [5, 8, 5]]
assert solution.averageHeightOfBuildings([[1, 8, 1], [9, 14, 2], [8, 18, 8]]) == [[1, 8, 1], [8, 9, 8], [9, 14, 5], [14, 18, 8]]
assert solution.averageHeightOfBuildings([[1, 8, 2], [10, 14, 4], [5, 9, 5], [7, 10, 6]]) == [[1, 5, 2], [5, 7, 3], [7, 8, 4], [8, 9, 5], [9, 10, 6], [10, 14, 4]]
assert solution.averageHeightOfBuildings([[5, 8, 3], [3, 10, 8]]) == [[3, 5, 8], [5, 8, 5], [8, 10, 8]]
assert solution.averageHeightOfBuildings([[7, 8, 6], [6, 9, 10], [5, 6, 5], [1, 3, 9]]) == [[1, 3, 9], [5, 6, 5], [6, 7, 10], [7, 8, 8], [8, 9, 10]]
assert solution.averageHeightOfBuildings([[3, 10, 6], [2, 12, 10], [5, 14, 3], [9, 14, 7], [4, 5, 10]]) == [[2, 3, 10], [3, 5, 8], [5, 12, 6], [12, 14, 5]]
assert solution.averageHeightOfBuildings([[4, 14, 6], [9, 19, 5], [8, 16, 8], [7, 15, 4], [10, 15, 9]]) == [[4, 7, 6], [7, 8, 5], [8, 9, 6], [9, 10, 5], [10, 16, 6], [16, 19, 5]]
assert solution.averageHeightOfBuildings([[8, 16, 10]]) == [[8, 16, 10]]
assert solution.averageHeightOfBuildings([[8, 12, 2]]) == [[8, 12, 2]]
assert solution.averageHeightOfBuildings([[10, 11, 8], [5, 15, 5]]) == [[5, 10, 5], [10, 11, 6], [11, 15, 5]]
assert solution.averageHeightOfBuildings([[5, 13, 5], [2, 12, 5], [2, 6, 7]]) == [[2, 5, 6], [5, 13, 5]]
assert solution.averageHeightOfBuildings([[4, 5, 10]]) == [[4, 5, 10]]
assert solution.averageHeightOfBuildings([[7, 10, 3], [2, 3, 5], [4, 7, 2]]) == [[2, 3, 5], [4, 7, 2], [7, 10, 3]]
assert solution.averageHeightOfBuildings([[1, 5, 4], [10, 17, 3], [2, 3, 3], [2, 9, 1]]) == [[1, 2, 4], [2, 5, 2], [5, 9, 1], [10, 17, 3]]
assert solution.averageHeightOfBuildings([[9, 13, 5], [1, 7, 9], [1, 10, 7], [9, 14, 9], [10, 15, 4]]) == [[1, 7, 8], [7, 10, 7], [10, 14, 6], [14, 15, 4]]
assert solution.averageHeightOfBuildings([[9, 16, 9], [5, 15, 6]]) == [[5, 9, 6], [9, 15, 7], [15, 16, 9]]

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
