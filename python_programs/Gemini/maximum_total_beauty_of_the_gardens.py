import bisect

class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        n = len(flowers)
        flowers.sort()

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + flowers[i]

        max_beauty = 0
        suffix_cost = 0

        for num_complete in range(n + 1):
             if num_complete > 0:
                  garden_idx = n - num_complete
                  # Cost to make garden complete only if it's below target
                  needed = max(0, target - flowers[garden_idx])
                  suffix_cost += needed

             if suffix_cost > newFlowers:
                  break

             remaining_flowers = newFlowers - suffix_cost
             num_incomplete = n - num_complete

             # Calculate score from complete gardens FIRST
             beauty_from_full = num_complete * full
             beauty_from_partial = 0 # Initialize partial score to 0

             # Only calculate partial score if there are potentially incomplete gardens
             if num_incomplete > 0:
                  # *** ADDED CHECK ***
                  # Check if there's AT LEAST one garden among the potential incomplete ones
                  # that could actually BE incomplete (i.e., starts below target).
                  # If the highest-valued garden in this group (flowers[num_incomplete-1])
                  # already meets the target, then NONE of them can be incomplete after adding flowers.
                  if flowers[num_incomplete - 1] < target:
                       # --- Perform binary search to find max achievable min level < target ---
                       # Only proceed if a partial score is possible
                       low = 0
                       high = target - 1 # Max level for incomplete is target - 1
                       best_level = 0
                       while low <= high:
                           mid_level = low + (high - low) // 2
                           if mid_level == 0:
                               cost_partial = 0
                           else:
                               # Find cost to bring gardens 0..p-1 up to mid_level
                               p = bisect.bisect_left(flowers, mid_level, 0, num_incomplete)
                               cost_partial = p * mid_level - prefix_sum[p]

                           if cost_partial <= remaining_flowers:
                               best_level = mid_level
                               low = mid_level + 1
                           else:
                               high = mid_level - 1
                       # --- End Binary Search ---

                       # Assign the partial beauty if a valid level was found
                       min_level_incomplete = best_level
                       beauty_from_partial = min_level_incomplete * partial
                  # else: # flowers[num_incomplete - 1] >= target
                       # All gardens in the "incomplete" group are already >= target.
                       # No planting can make them incomplete. Partial score is 0.
                       # beauty_from_partial remains 0

             # Combine the scores for this configuration
             current_beauty = beauty_from_full + beauty_from_partial
             max_beauty = max(max_beauty, current_beauty)

        return max_beauty
    
solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.maximumBeauty([1, 6, 29, 53, 54, 85, 91, 93, 96, 100], 3, 56, 22, 46) == 294
assert solution.maximumBeauty([20, 50, 60, 68], 6, 31, 39, 94) == 2561
assert solution.maximumBeauty([13, 44, 54, 74, 77, 79, 91], 43, 73, 88, 57) == 3202
assert solution.maximumBeauty([2, 6, 41, 51, 80], 72, 1, 30, 38) == 150
assert solution.maximumBeauty([5, 26, 34, 51, 77, 87, 88], 91, 73, 48, 67) == 3561
assert solution.maximumBeauty([9, 14, 19, 41, 66, 73, 80, 81, 90], 39, 79, 39, 59) == 1710
assert solution.maximumBeauty([10, 28, 29, 37, 42, 50, 57, 91, 92], 12, 20, 62, 61) == 1655
assert solution.maximumBeauty([13, 18, 68], 73, 20, 98, 25) == 671
assert solution.maximumBeauty([4, 35, 38, 69], 81, 86, 82, 63) == 3276
assert solution.maximumBeauty([2, 5, 24, 37, 41, 48, 50, 69, 78], 96, 20, 9, 46) == 946
assert solution.maximumBeauty([2, 9, 16, 17, 23, 37, 39, 77, 82, 95], 47, 28, 34, 78) == 1886
assert solution.maximumBeauty([3, 74], 97, 56, 35, 65) == 3610
assert solution.maximumBeauty([3, 5, 7, 36, 72, 87, 100], 75, 51, 10, 82) == 2490
assert solution.maximumBeauty([79, 100], 54, 92, 63, 62) == 5705
assert solution.maximumBeauty([9, 19, 50, 58, 69, 71, 75, 78, 84, 93], 31, 53, 60, 41) == 1628
assert solution.maximumBeauty([9, 17, 28, 52, 57, 65, 89, 96, 98], 3, 58, 87, 94) == 1476
assert solution.maximumBeauty([1, 9, 26, 27, 29, 56, 61, 77, 92, 98], 67, 5, 83, 76) == 1051
assert solution.maximumBeauty([4, 32, 53, 59, 61, 65, 75, 76, 81, 88], 96, 77, 96, 15) == 1326
assert solution.maximumBeauty([38, 44, 46, 60], 91, 15, 79, 3) == 316
assert solution.maximumBeauty([31, 37, 65, 72, 73, 94], 33, 27, 33, 23) == 198
assert solution.maximumBeauty([32, 48, 50, 57, 68, 72, 78], 57, 101, 8, 4) == 244
assert solution.maximumBeauty([24, 36, 76], 35, 30, 37, 92) == 2742
assert solution.maximumBeauty([69, 99], 52, 101, 7, 15) == 1507
assert solution.maximumBeauty([14, 23, 25, 53, 72], 47, 19, 101, 65) == 1574
assert solution.maximumBeauty([12, 32, 47, 58, 69], 78, 13, 61, 20) == 484
assert solution.maximumBeauty([61, 74], 92, 96, 16, 53) == 5051
assert solution.maximumBeauty([6, 13, 19, 30, 36, 89, 91, 95, 96], 93, 72, 67, 28) == 1360
assert solution.maximumBeauty([1, 16, 41, 66, 72], 55, 32, 36, 86) == 2810
assert solution.maximumBeauty([21, 54, 74, 78], 4, 77, 24, 100) == 2524
assert solution.maximumBeauty([67, 89], 30, 83, 33, 11) == 935
assert solution.maximumBeauty([15, 23, 38, 45, 49, 56, 57, 73, 82], 47, 9, 84, 17) == 756
assert solution.maximumBeauty([15, 21, 34, 44, 54, 96], 82, 60, 81, 9) == 639
assert solution.maximumBeauty([62, 68], 55, 99, 45, 54) == 4968
assert solution.maximumBeauty([24, 42, 45, 52, 57, 98], 80, 34, 8, 76) == 2548
assert solution.maximumBeauty([37, 92], 34, 84, 30, 98) == 6988
assert solution.maximumBeauty([37, 54, 78, 80, 89, 96], 12, 41, 12, 21) == 900
assert solution.maximumBeauty([21, 38, 56, 58, 73, 82, 91, 99, 100], 63, 50, 84, 88) == 4984
assert solution.maximumBeauty([12, 15, 19, 39, 44, 76, 98], 40, 80, 11, 78) == 2195
assert solution.maximumBeauty([8, 19, 33, 50, 66, 70, 76, 82, 89, 96], 77, 90, 72, 75) == 3519
assert solution.maximumBeauty([1, 5, 10, 13, 23, 29, 31, 32, 53, 72], 37, 19, 9, 2) == 100
assert solution.maximumBeauty([14, 42, 53], 1, 7, 82, 95) == 246
assert solution.maximumBeauty([6, 18, 25, 43, 47, 67], 83, 74, 96, 93) == 3999
assert solution.maximumBeauty([3, 40, 73, 89, 97], 73, 59, 54, 97) == 5788
assert solution.maximumBeauty([2, 21, 25, 46, 53, 57, 62], 46, 67, 43, 64) == 1984
assert solution.maximumBeauty([29, 44, 59, 61, 83, 86, 92], 77, 58, 45, 29) == 1923
assert solution.maximumBeauty([26, 92, 100], 39, 33, 57, 6) == 306
assert solution.maximumBeauty([1, 10, 12, 36, 44, 52, 63, 95], 29, 62, 92, 36) == 796
assert solution.maximumBeauty([14, 51, 65, 99], 80, 3, 38, 25) == 152
assert solution.maximumBeauty([25, 46], 86, 51, 88, 73) == 3738
assert solution.maximumBeauty([17, 74, 93], 94, 91, 63, 88) == 8046
assert solution.maximumBeauty([12, 26, 34, 36, 39, 50, 51, 61, 72, 99], 53, 41, 76, 17) == 1296
assert solution.maximumBeauty([24, 27, 43, 54, 69, 89, 90, 97, 98], 31, 52, 85, 25) == 1535
assert solution.maximumBeauty([41, 46, 48, 55, 60, 71, 98], 59, 21, 18, 37) == 126
assert solution.maximumBeauty([9, 43], 85, 23, 37, 94) == 2105
assert solution.maximumBeauty([6, 14, 30, 37, 38, 43, 95], 41, 35, 44, 67) == 2186
assert solution.maximumBeauty([6, 56, 86, 88], 76, 40, 6, 83) == 3255
assert solution.maximumBeauty([21, 37, 86, 92, 96], 7, 75, 97, 80) == 2531
assert solution.maximumBeauty([5, 28, 39, 46, 50, 62, 68, 71, 96], 101, 77, 71, 64) == 3470
assert solution.maximumBeauty([22, 35, 36, 50, 100], 68, 96, 92, 6) == 412
assert solution.maximumBeauty([4, 9, 32, 42, 66, 72, 73, 82], 9, 75, 72, 93) == 1095
assert solution.maximumBeauty([2, 10, 11, 32, 46, 48, 64, 74, 79, 93], 12, 83, 94, 23) == 418
assert solution.maximumBeauty([3, 22, 26, 31, 33, 37, 79, 86, 87], 7, 75, 62, 54) == 726
assert solution.maximumBeauty([4, 14, 29, 41, 48, 50, 64, 67, 69], 52, 15, 49, 90) == 1652
assert solution.maximumBeauty([65, 94], 88, 65, 34, 35) == 68
assert solution.maximumBeauty([1, 4, 48, 55, 74, 94], 36, 65, 51, 10) == 303
assert solution.maximumBeauty([20, 65], 90, 98, 73, 23) == 2001
assert solution.maximumBeauty([10, 56], 100, 64, 22, 68) == 4306
assert solution.maximumBeauty([32, 67], 2, 96, 17, 3) == 102
assert solution.maximumBeauty([1, 17, 60, 69, 76], 10, 45, 19, 62) == 739
assert solution.maximumBeauty([10, 19, 55, 59, 60, 64, 67], 90, 21, 64, 99) == 2364
assert solution.maximumBeauty([11, 14, 32, 39, 66, 85], 85, 84, 64, 95) == 4339
assert solution.maximumBeauty([28, 32, 36, 37, 44, 68, 72, 97, 99], 58, 87, 72, 49) == 2447
assert solution.maximumBeauty([37, 52, 54, 61, 63, 65, 84, 86, 89, 100], 34, 60, 14, 6) == 468
assert solution.maximumBeauty([13, 32, 48, 67, 72, 73, 99], 20, 12, 39, 81) == 273
assert solution.maximumBeauty([11, 25, 48, 57, 63, 64, 70, 76, 95], 1, 93, 24, 97) == 1188
assert solution.maximumBeauty([70, 75, 78], 73, 97, 65, 14) == 1474
assert solution.maximumBeauty([32, 98], 13, 8, 55, 34) == 110
assert solution.maximumBeauty([3, 15, 29, 37, 58, 69, 74, 76, 99], 13, 9, 87, 25) == 896
assert solution.maximumBeauty([4, 25, 45, 60, 67, 79, 91, 92], 28, 65, 70, 63) == 2044
assert solution.maximumBeauty([9, 36, 39, 44, 64, 67, 78, 85], 51, 61, 49, 35) == 1736
assert solution.maximumBeauty([16, 28, 31, 38, 41, 71, 80], 12, 86, 61, 69) == 1932
assert solution.maximumBeauty([32, 87], 45, 66, 25, 57) == 3730
assert solution.maximumBeauty([7, 18, 35, 37, 47, 51, 59, 82, 90, 92], 78, 62, 89, 58) == 2850
assert solution.maximumBeauty([35, 36, 49, 60, 63, 87, 92, 99], 96, 75, 38, 74) == 5072
assert solution.maximumBeauty([11, 21, 22, 53, 83], 36, 98, 26, 13) == 390
assert solution.maximumBeauty([2, 28, 30, 40, 47, 49, 50, 58, 72], 82, 97, 9, 35) == 1575
assert solution.maximumBeauty([86, 94], 68, 49, 71, 89) == 142
assert solution.maximumBeauty([14, 22, 23, 35, 46, 49, 54, 57, 85, 93], 62, 37, 75, 11) == 1071
assert solution.maximumBeauty([8, 27, 34, 46, 56], 50, 61, 56, 49) == 1918
assert solution.maximumBeauty([7, 23, 75], 15, 73, 11, 28) == 627
assert solution.maximumBeauty([3, 15, 31, 49, 55, 56, 64, 68, 97], 19, 57, 75, 7) == 527
assert solution.maximumBeauty([63, 65, 74], 56, 7, 77, 18) == 231
assert solution.maximumBeauty([9, 12, 20, 30, 68, 73, 82], 81, 89, 78, 92) == 3496
assert solution.maximumBeauty([74, 86], 5, 66, 26, 96) == 52
assert solution.maximumBeauty([12, 19, 26, 31, 38, 44, 57, 62, 70], 49, 31, 7, 60) == 1856
assert solution.maximumBeauty([1, 58, 69, 74, 76], 61, 31, 77, 11) == 638
assert solution.maximumBeauty([9, 81], 52, 60, 87, 81) == 4866
assert solution.maximumBeauty([61, 71, 79], 37, 70, 2, 67) == 4627
assert solution.maximumBeauty([65, 71], 8, 67, 12, 41) == 2718
assert solution.maximumBeauty([1, 32, 38, 61, 81, 83], 11, 73, 26, 5) == 112
