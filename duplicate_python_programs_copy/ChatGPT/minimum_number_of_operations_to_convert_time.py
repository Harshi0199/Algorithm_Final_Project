# Problem 2224: Minimum Number of Operations to Convert Time
# Difficulty: Easy
# Description:
# <p>You are given two strings <code>current</code> and <code>correct</code> representing two <strong>24-hour times</strong>.</p>
# <p>24-hour times are formatted as <code>&quot;HH:MM&quot;</code>, where <code>HH</code> is between <code>00</code> and <code>23</code>, and <code>MM</code> is between <code>00</code> and <code>59</code>. The earliest 24-hour time is <code>00:00</code>, and the latest is <code>23:59</code>.</p>
# <p>In one operation you can increase the time <code>current</code> by <code>1</code>, <code>5</code>, <code>15</code>, or <code>60</code> minutes. You can perform this operation <strong>any</strong> number of times.</p>
# <p>Return <em>the <strong>minimum number of operations</strong> needed to convert </em><code>current</code><em> to </em><code>correct</code>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> current = &quot;02:30&quot;, correct = &quot;04:35&quot;
# <strong>Output:</strong> 3
# <strong>Explanation:
# </strong>We can convert current to correct in 3 operations as follows:
# - Add 60 minutes to current. current becomes &quot;03:30&quot;.
# - Add 60 minutes to current. current becomes &quot;04:30&quot;.
# - Add 5 minutes to current. current becomes &quot;04:35&quot;.
# It can be proven that it is not possible to convert current to correct in fewer than 3 operations.</pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> current = &quot;11:00&quot;, correct = &quot;11:01&quot;
# <strong>Output:</strong> 1
# <strong>Explanation:</strong> We only have to add one minute to current, so the minimum number of operations needed is 1.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>current</code> and <code>correct</code> are in the format <code>&quot;HH:MM&quot;</code></li>
# 	<li><code>current &lt;= correct</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

from typing import *

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        diff = to_minutes(correct) - to_minutes(current)
        operations = 0
        for step in [60, 15, 5, 1]:
            operations += diff // step
            diff %= step
        return operations


# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.convertTime('13:45', '22:45') == 9
assert solution.convertTime('12:11', '21:27') == 11
assert solution.convertTime('15:40', '22:47') == 10
assert solution.convertTime('15:29', '20:33') == 9
assert solution.convertTime('09:40', '09:55') == 1
assert solution.convertTime('15:48', '15:57') == 5
assert solution.convertTime('06:40', '18:52') == 16
assert solution.convertTime('07:28', '12:54') == 9
assert solution.convertTime('14:46', '20:49') == 9
assert solution.convertTime('20:57', '23:57') == 3
assert solution.convertTime('12:33', '19:39') == 9
assert solution.convertTime('18:55', '23:55') == 5
assert solution.convertTime('21:11', '22:43') == 5
assert solution.convertTime('21:22', '21:56') == 6
assert solution.convertTime('13:09', '23:26') == 13
assert solution.convertTime('00:43', '14:43') == 14
assert solution.convertTime('00:33', '23:48') == 24
assert solution.convertTime('03:04', '12:18') == 15
assert solution.convertTime('16:21', '21:38') == 8
assert solution.convertTime('13:49', '17:54') == 5
assert solution.convertTime('12:40', '16:59') == 9
assert solution.convertTime('11:01', '14:37') == 7
assert solution.convertTime('09:57', '22:57') == 13
assert solution.convertTime('19:43', '20:48') == 2
assert solution.convertTime('21:35', '21:53') == 4
assert solution.convertTime('09:05', '12:24') == 8
assert solution.convertTime('10:22', '20:25') == 13
assert solution.convertTime('03:29', '05:40') == 5
assert solution.convertTime('12:57', '18:59') == 8
assert solution.convertTime('23:46', '23:47') == 1
assert solution.convertTime('12:54', '20:57') == 11
assert solution.convertTime('12:41', '21:43') == 11
assert solution.convertTime('15:52', '16:57') == 2
assert solution.convertTime('05:04', '21:09') == 17
assert solution.convertTime('02:40', '10:48') == 12
assert solution.convertTime('13:27', '18:59') == 9
assert solution.convertTime('16:15', '21:32') == 8
assert solution.convertTime('19:11', '22:47') == 7
assert solution.convertTime('15:58', '20:59') == 6
assert solution.convertTime('03:58', '13:58') == 10
assert solution.convertTime('07:25', '20:42') == 16
assert solution.convertTime('06:42', '12:56') == 12
assert solution.convertTime('22:49', '23:49') == 1
assert solution.convertTime('11:49', '14:55') == 5
assert solution.convertTime('20:59', '22:59') == 2
assert solution.convertTime('03:30', '16:37') == 16
assert solution.convertTime('03:12', '12:43') == 12
assert solution.convertTime('19:15', '20:36') == 4
assert solution.convertTime('23:17', '23:53') == 4
assert solution.convertTime('22:50', '23:56') == 3
assert solution.convertTime('06:14', '20:55') == 19
assert solution.convertTime('00:06', '14:57') == 19
assert solution.convertTime('10:26', '16:28') == 8
assert solution.convertTime('15:12', '21:41') == 13
assert solution.convertTime('23:35', '23:35') == 0
assert solution.convertTime('12:35', '15:36') == 4
assert solution.convertTime('09:57', '21:57') == 12
assert solution.convertTime('22:20', '22:55') == 3
assert solution.convertTime('13:55', '13:56') == 1
assert solution.convertTime('14:53', '16:57') == 6
assert solution.convertTime('23:32', '23:32') == 0
assert solution.convertTime('20:27', '20:32') == 1
assert solution.convertTime('09:54', '19:59') == 11
assert solution.convertTime('06:36', '18:45') == 17
assert solution.convertTime('13:11', '16:34') == 8
assert solution.convertTime('19:45', '19:46') == 1
assert solution.convertTime('08:26', '11:57') == 6
assert solution.convertTime('23:53', '23:58') == 1
assert solution.convertTime('01:58', '11:58') == 10
assert solution.convertTime('11:59', '13:59') == 2
assert solution.convertTime('20:34', '22:44') == 4
assert solution.convertTime('23:49', '23:55') == 2
assert solution.convertTime('03:31', '06:52') == 6
assert solution.convertTime('02:54', '22:58') == 24
assert solution.convertTime('06:06', '06:33') == 5
assert solution.convertTime('20:02', '20:12') == 2
assert solution.convertTime('13:41', '15:44') == 5
assert solution.convertTime('11:05', '17:49') == 14
assert solution.convertTime('16:39', '20:40') == 5
assert solution.convertTime('16:34', '21:37') == 8
assert solution.convertTime('14:58', '16:58') == 2
assert solution.convertTime('17:53', '20:58') == 4
assert solution.convertTime('12:37', '16:51') == 10
assert solution.convertTime('01:53', '18:54') == 18
assert solution.convertTime('04:13', '04:57') == 8
assert solution.convertTime('10:05', '21:41') == 15
assert solution.convertTime('19:13', '20:57') == 9
assert solution.convertTime('22:17', '23:58') == 6
assert solution.convertTime('15:56', '21:56') == 6
assert solution.convertTime('02:08', '08:23') == 7
assert solution.convertTime('18:32', '21:51') == 8
assert solution.convertTime('03:15', '12:16') == 10
assert solution.convertTime('13:34', '14:39') == 2
assert solution.convertTime('14:58', '15:58') == 1
assert solution.convertTime('14:17', '16:29') == 6
assert solution.convertTime('12:05', '19:25') == 9
assert solution.convertTime('20:22', '22:48') == 6
assert solution.convertTime('20:07', '23:34') == 8
assert solution.convertTime('14:54', '23:54') == 9
assert solution.convertTime('00:29', '07:46') == 10

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass