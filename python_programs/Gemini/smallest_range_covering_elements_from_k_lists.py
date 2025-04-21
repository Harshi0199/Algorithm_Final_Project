import heapq
import math

class Solution(object):
    def smallestRange(self, nums):
        """
        Finds the smallest range that includes at least one number from each of the k sorted lists.

        :type nums: List[List[int]]
        :rtype: List[int]

        The algorithm uses a min-heap to efficiently track the smallest element across the current pointers
        of all lists. It maintains a window defined by the minimum element in the heap and the maximum
        element seen so far among the elements currently considered (one from each list).

        Steps:
        1. Initialize a min-heap. Store tuples of (value, list_index, element_index).
        2. Initialize `current_max` to track the maximum value currently in our considered set.
        3. Add the first element from each list to the heap and update `current_max`.
        4. Initialize the `result_range` (start, end) and `min_range_diff` based on the initial elements.
        5. Loop while the heap contains elements from all k lists:
           a. Pop the smallest element (min_val, list_idx, element_idx) from the heap.
           b. Check if the list from which the element was popped has more elements.
           c. If yes:
              i. Get the next element from that list.
              ii. Push (next_element, list_idx, next_element_idx) onto the heap.
              iii. Update `current_max = max(current_max, next_element)`.
              iv. Get the new minimum element from the heap (heap's top).
              v. Calculate the new range difference: `new_diff = current_max - new_min`.
              vi. If `new_diff` is smaller than `min_range_diff`, or if they are equal but the new start is smaller,
                  update `min_range_diff` and `result_range`.
           d. If no (the list is exhausted): Break the loop.
        6. Return the `result_range`.
        """
        k = len(nums)
        min_heap = []
        current_max = -math.inf

        # Initialize the heap with the first element from each list
        for i in range(k):
            if not nums[i]: # Handle empty lists if necessary per constraints (though constraints say >= 1)
                return [] # Or handle as appropriate
            element = nums[i][0]
            heapq.heappush(min_heap, (element, i, 0)) # (value, list_index, element_index)
            current_max = max(current_max, element)

        # Initial range calculation
        min_val, _, _ = min_heap[0] # Smallest element is at the top
        min_range_diff = current_max - min_val
        result_range = [min_val, current_max]

        # Process elements using the heap
        while True:
            # Get the smallest element currently considered
            min_val, list_idx, element_idx = heapq.heappop(min_heap)

            # Check if we can advance the pointer in the list from which min_val came
            if element_idx + 1 < len(nums[list_idx]):
                next_element_idx = element_idx + 1
                next_val = nums[list_idx][next_element_idx]

                # Add the next element from this list to the heap
                heapq.heappush(min_heap, (next_val, list_idx, next_element_idx))

                # Update the maximum value seen so far in the window
                current_max = max(current_max, next_val)

                # Get the new minimum from the heap
                new_min_val, _, _ = min_heap[0]

                # Calculate the new range difference
                new_range_diff = current_max - new_min_val

                # Check if this new range is smaller than the best range found so far
                # Condition: new_diff < min_diff OR (new_diff == min_diff AND new_start < old_start)
                if new_range_diff < min_range_diff or \
                   (new_range_diff == min_range_diff and new_min_val < result_range[0]):
                    min_range_diff = new_range_diff
                    result_range = [new_min_val, current_max]
            else:
                # If any list is exhausted, we cannot form a valid range anymore
                break

        return result_range

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.smallestRange([[-69875, -35265, 66745, 81080, 90155], [-13229, -1144, 13630, 27302, 51116, 79012, 80807, 92818, 98613, 98719], [-49847, -15112, 11490, 52288, 58462, 77626, 92717]]) == [90155, 92818]
assert solution.smallestRange([[-64755, -30440, -16167, -13582, 28361, 71464], [-76567, -69129, -55573, -46459, 15861, 25358, 33994, 46222, 92643], [-95491, -84265, -83126, -62289, -11384, -4225, 42022, 43984, 77918, 86408]]) == [-69129, -62289]
assert solution.smallestRange([[-63257, -32989, -31737, -9558, 24380, 40503, 54943, 67851, 73896, 92347]]) == [-63257, -63257]
assert solution.smallestRange([[-12364, 12067, 18885, 43694]]) == [-12364, -12364]
assert solution.smallestRange([[-83549, -81472, -71560, -67232, -25024, 4298, 19746, 97542], [-93798, -84031, -42978, 956, 62202, 82518]]) == [-84031, -83549]
assert solution.smallestRange([[-37812, -22525, -17000, 43372, 46071, 81724], [-45852, 64460], [-70031, -47109, -42662, -20471, 21383, 35469, 38576, 67089, 89326]]) == [-45852, -37812]
assert solution.smallestRange([[-93055, -79997, -8832, -5910, -1057, 48470, 93871], [-90950, -81519, -80427, -67945, -46812, -5614, 22791], [-81142, -56149]]) == [-81142, -79997]
assert solution.smallestRange([[-95723, -91595, -62722, -25520, -21272, 7889, 30147]]) == [-95723, -95723]
assert solution.smallestRange([[-65598], [-81928, -28196, 26910, 83674], [-33378, -20384, -1539, 1008, 46505, 47212, 71956, 77492, 95146]]) == [-65598, -28196]
assert solution.smallestRange([[-3961, -1444, 8979, 16866, 44154, 69991, 96263], [-55352, 61600], [-82565, -76846, -73634, -48739, -18794, 15701], [-61821, 20232, 39283, 52232, 65344]]) == [15701, 61600]
assert solution.smallestRange([[-96769, -84278, -40650, -33721, -23618, 2312, 9446, 50794, 69722, 89034], [-90157, -36942, -36146, 52982, 54495, 54824, 59505]]) == [50794, 52982]
assert solution.smallestRange([[-79901]]) == [-79901, -79901]
assert solution.smallestRange([[-98688, -97943, -97764, -81465, -45129, -22667, 33871, 85370], [-95202, 13566, 54786, 65386], [-89323, -83089, -79095, -32238, -7916, -4888, 27445, 61155, 68470, 85230]]) == [-97764, -89323]
assert solution.smallestRange([[-76526, -55591, -8478, 82761, 84042]]) == [-76526, -76526]
assert solution.smallestRange([[-84406, -36877, -29144, -18923, 1608], [-77403, -55350, -38214, -34131, -17752, 19205, 42064, 86160], [8727, 10172, 19152, 20658, 34639, 52742, 77444, 95011, 96607], [-72594, -48612, 51717]]) == [1608, 51717]
assert solution.smallestRange([[-73426, -30329, 15095], [-60776, 6296], [-98367, -7650, 90883], [5138, 26062, 29907, 78946, 80115, 90176]]) == [-7650, 15095]
assert solution.smallestRange([[-8795, 33506], [-96481, -80530, -70722, -64868, -49156, -44331, -5386, 12995, 20563, 97504], [-27441, -27393, -21991, -17795, 13058, 44614]]) == [-17795, -5386]
assert solution.smallestRange([[-72643, -52001, -39571, -30824, 55994, 56778, 63494, 84622, 90897], [-64312, 19074, 28346, 93830], [-32331], [-92216, -59696, -51746, -7038, 64734, 65072]]) == [-64312, -32331]
assert solution.smallestRange([[-68101, -60833, -38642, 49438, 66601, 69664], [-85133, -84075, -81983, -67777, -24280, 63085, 73010, 97850, 98349], [-45225, -21904, 49454]]) == [49438, 63085]
assert solution.smallestRange([[-73161, -44933, 49092, 54081], [20260], [43310], [-64334, -54491, -22301, 15808]]) == [15808, 49092]
assert solution.smallestRange([[-96945, -90828, -71855, 40738, 50312, 64760, 91943], [-75662], [-65137, 21989, 65627], [41092]]) == [-75662, 41092]
assert solution.smallestRange([[-44379, -21747, -9357, 46473, 47868]]) == [-44379, -44379]
assert solution.smallestRange([[-86550, -32145, -27545, 27742, 42921, 55401], [-72434, -63004, -24345, 13740, 25506, 65226, 74359, 85082], [15964, 74560, 80505]]) == [15964, 27742]
assert solution.smallestRange([[-97222, -70046, -33964, -22423, -13584, 6182, 67114, 86837, 99833]]) == [-97222, -97222]
assert solution.smallestRange([[-78692, -47956, -33429, -24909, 3855, 18097, 24830, 29312, 66503], [-99573, -80931, -54867, -49957, -10416, 4916, 27687, 54385, 69339, 87254]]) == [3855, 4916]
assert solution.smallestRange([[-95937, -83914, -39327, 52905]]) == [-95937, -95937]
assert solution.smallestRange([[51595, 60803, 62384], [-85415, -81094, -76385, -42214, -33823, 25098, 40837, 92476], [-50670, -48194, -36867, -32901, 98664], [-86974, -81036, -63526, -56249, -44604, -10799, 13961, 39450]]) == [39450, 98664]
assert solution.smallestRange([[49658]]) == [49658, 49658]
assert solution.smallestRange([[-98361, -32179, -4768, -336, 62366, 73275, 88023], [-49006, -42109, -9581, 195, 18555, 47514], [-98430, -90297, -88336, -88228, -87822, -82134, 19773, 51487]]) == [47514, 62366]
assert solution.smallestRange([[-73414, -64246, 45384, 74487, 90006, 96873]]) == [-73414, -73414]
assert solution.smallestRange([[-97605, -61230, -28577, -17277, 3835], [-89763, -84842, -58920, -40112, -22354, -19962, -9823, 58122, 89971]]) == [-61230, -58920]
assert solution.smallestRange([[-89350, -70409, -41344, 36863], [-52835, -11118, 9555, 29396, 37167], [-97402, -94909, -62104, -45856, -811, 8215, 12261, 23235, 71783]]) == [-52835, -41344]
assert solution.smallestRange([[-67883, -18120, -16318, 32902, 34316, 49931], [-79384, -69692, -22912, 16350, 16439, 38089, 58168, 60683, 97166]]) == [-69692, -67883]
assert solution.smallestRange([[-47903, -22116, 52174]]) == [-47903, -47903]
assert solution.smallestRange([[-56924, 77179], [-76428, -19509, -13507, -5604, 69056], [-70397, -66202, -53014, -45633, -37905, 13756]]) == [-76428, -56924]
assert solution.smallestRange([[-88123, -70367, -40869, 29690, 29878, 42443, 77790]]) == [-88123, -88123]
assert solution.smallestRange([[-90210, -89302, 39388], [-86837, -86515, -82992, -44153, -21732, -10210, 28953], [-98199, -19327, 36744], [-79719, 20491]]) == [-98199, -79719]
assert solution.smallestRange([[-9854, 36125, 43625, 65236], [-90293, -55230, -49078, -47061, -9990, 6053], [-87598, -52691, -21688, 31527, 62447, 86631, 92189]]) == [-21688, -9854]
assert solution.smallestRange([[-47528, 97602], [-39507, 20232]]) == [-47528, -39507]
assert solution.smallestRange([[-79623, -68934, -67054, -18148, -14030, -12451, -1435, 29018, 40305]]) == [-79623, -79623]
assert solution.smallestRange([[-41817, -30530, 89507], [-46239, -29337, 6515], [-95929, -27552, 11528, 15106, 17535, 50989], [-63767, -54425, -6249, 17139, 43626, 54440, 65432]]) == [-30530, -6249]
assert solution.smallestRange([[-98437, -97820, -94862, -92041, -78457, -61001, -49924, -42011, 43154], [-95183, -73006, -66069, -52731, 2382, 12305, 29875], [-94144, -46734, -19587, 6660, 78250], [-32458, -3299, 21855, 41132, 46778, 52492, 69046, 73126, 84676]]) == [-52731, -32458]
assert solution.smallestRange([[-65717], [-97682, -75279, -19034, 65536, 74891], [-78759, -36165]]) == [-78759, -65717]
assert solution.smallestRange([[-61091, -52165, -15794, -9149, 1886], [-43775], [-33784, -5455, 59091, 69565]]) == [-52165, -33784]
assert solution.smallestRange([[-63364, -11283], [-15995, 65545], [-28752, -25807, -11398, -695, 41232, 91428], [-1842, 4240, 19936, 39045, 39642, 83030, 90108]]) == [-15995, -1842]
assert solution.smallestRange([[-56761, -28093, 13971, 14992, 69867], [-14098, 58284, 93445], [-80235, -77103, -55971, -36392, -24288, 3700, 20876, 30188, 47275, 83965], [-90772, -85615, -78206, -38824, -26069, -21533, -2967, -879, 65451]]) == [-28093, -14098]
assert solution.smallestRange([[-52102, -45988, -1853, 6492, 40386, 99077], [-83429, -72661, -12951, -11012, 30977, 47327, 62462], [-16373, -8788, 34924, 75645]]) == [-11012, -1853]
assert solution.smallestRange([[-84727, -79567, 15502, 58396, 65912], [14314, 49200], [-47539, -36902, -29179, 20384, 58840, 85621, 98786]]) == [14314, 20384]
assert solution.smallestRange([[-47264], [-10224, 14646, 64064, 64318, 66945], [-78454, -47395, -23806, -22569, 38408, 55653, 98625], [-72811, -52215, -48001, -13510, 12316, 25116, 47857]]) == [-47264, -10224]
assert solution.smallestRange([[-92892, -89947, -76253, -63693, -48218, -42691, -25584, 96844], [-74768, 73958]]) == [-76253, -74768]
assert solution.smallestRange([[-91088, 39286], [-68328, 27183, 29245, 54913, 65911, 77279, 84322]]) == [29245, 39286]
assert solution.smallestRange([[-68816, -52243, 36317], [-96096, -88997, -69239, -11503, 3870, 29882, 45857, 48621, 52176, 87152], [-13219, -2823, 8702, 75761], [-94200, -93361, -77167, -75303, -37633, -29098, 17167]]) == [8702, 36317]
assert solution.smallestRange([[-81062, -33209, -16835, 18294, 54117, 90017, 97285], [4082, 6773, 52891]]) == [52891, 54117]
assert solution.smallestRange([[-78054, -22192, -15171, 21269]]) == [-78054, -78054]
assert solution.smallestRange([[-80629, -50798, -21989, -15578, 14773, 22152, 37339, 99859], [-79323], [-78679, -69446, -28338, 19177, 47151, 48725, 56861], [-37423, -1437, 63493]]) == [-79323, -37423]
assert solution.smallestRange([[-67020, -23744, 77485, 98962], [-92804, -22570, -14331, -3529, -1956, 30349, 60043]]) == [-23744, -22570]
assert solution.smallestRange([[21705], [-36407, 2820, 38146, 96027]]) == [21705, 38146]
assert solution.smallestRange([[-74491, -49280, 10836, 80121], [-92412, -74118, -73470, -56094, 22430, 42450, 80951], [-42916, -40748, -38138, 3634, 41093, 46928], [-86894, -80943, -74651, -55260, -7360, -5886, 3099, 10682, 32053, 39475]]) == [-56094, -42916]
assert solution.smallestRange([[8896]]) == [8896, 8896]
assert solution.smallestRange([[-92633, -66104, -35048, -14601, -5298, 8262, 12033, 66484, 75623, 98399], [-95828, -76651, -60809, -45085, -35127, -16683, -11942, 24943, 37869, 38636], [-39265, -663]]) == [-39265, -35048]
assert solution.smallestRange([[-77557, -58254, -16497, 59822], [-89986, 46318, 48219, 54420, 67454, 70362], [-96437, -95306, -59540, -39851, -39132, 12857, 28976, 38212, 58307]]) == [54420, 59822]
assert solution.smallestRange([[-96552, -26686, 66328, 90062], [-45728]]) == [-45728, -26686]
assert solution.smallestRange([[-57038, -42915, -29235, -18583, 13464, 39736], [-72482, -68160, -59492, -42198], [-76464, -69610, -3368, 24525, 31280, 64765], [-7759]]) == [-42198, -3368]
assert solution.smallestRange([[-92035, 26805, 30042, 63867], [-67413, 46546], [-39071, -32173, -20899, 68237, 74410, 89247], [-44371]]) == [-92035, -39071]
assert solution.smallestRange([[-72387]]) == [-72387, -72387]
assert solution.smallestRange([[-63737, -44679, 17240, 22514, 42235, 44403, 95295], [-67939, -56126, -55842, -42727, -42587, -35673, -25679, 14498, 62899, 64196], [-96787, -21592, 5052, 8159, 34020]]) == [8159, 17240]
assert solution.smallestRange([[-42885, -13871, 27689]]) == [-42885, -42885]
assert solution.smallestRange([[-38292, 13439, 35254]]) == [-38292, -38292]
assert solution.smallestRange([[-82795, -71151, -50311, -47478, -34373, -23035, -12363, 77595, 78876, 80107], [-94637, -18943, 64518, 76620, 87981, 95463, 99050]]) == [76620, 77595]
assert solution.smallestRange([[47479]]) == [47479, 47479]
assert solution.smallestRange([[24919, 91167, 99921], [-51249, -32163, 77725], [-96677, -75203, -74158, -26336, -19021, -13149, 40140, 60702, 88977], [63807, 64140, 64888, 86102, 96489]]) == [77725, 91167]
assert solution.smallestRange([[-88588, -52467, -8335, 6835], [-65177, -59589, -40642, 21592, 57551], [47131, 48245]]) == [6835, 47131]
assert solution.smallestRange([[86701, 89936], [-66519], [-884, 29019]]) == [-66519, 86701]
assert solution.smallestRange([[-92937, -50679, -44009, -6526, 2003, 3050, 9783, 19680, 20808, 39454], [15675, 55038, 76928], [-48652, -29157, 7900, 51914, 53108, 84900, 88931]]) == [7900, 15675]
assert solution.smallestRange([[-61546, -15252, 36683], [-79045, -52335, -50678, -22825, 25653, 35888, 53288, 65531], [-83819, -83377, 902, 39732, 55174, 55203], [-63044, -42358, -12942, -8412, 27253, 81654, 89581]]) == [27253, 39732]
assert solution.smallestRange([[54814, 92488]]) == [54814, 54814]
assert solution.smallestRange([[-98499, -82102, -64453, -60241, -50785, -32446, 61171, 93921]]) == [-98499, -98499]
assert solution.smallestRange([[-80634, 95125], [-25806, 59, 40438, 51378], [-25143, 61619, 63280]]) == [51378, 95125]
assert solution.smallestRange([[-88060, -70009, -43682, -17053, 65974, 93847], [-87567, -83456, -47327, -43124, -24901], [-89091, -55701, -37813, 23218], [-80648, -65963, -58445, -48003, -3752, 33457, 77786, 89483]]) == [-89091, -80648]
assert solution.smallestRange([[-61570, -42791, -11817, 42477]]) == [-61570, -61570]
assert solution.smallestRange([[-85675, -26443, -14713, 28338, 72877, 77604, 93869, 97146], [-67138, -55708, -28117, -26207, -4779, 17855, 42813, 43713, 58278, 91198]]) == [-26443, -26207]
assert solution.smallestRange([[-48124, -40600, -32340, 489, 54598, 55695, 71535, 95122], [-50289, -37511, -17907], [-93131, -8508, -7643], [-45389, -33271, 3976, 15101, 27202, 28212]]) == [-17907, 3976]
assert solution.smallestRange([[-73861, 61268, 64666, 85079]]) == [-73861, -73861]
assert solution.smallestRange([[-36241, -21138, 45115, 59883, 77727, 85735, 87783, 95858], [-41376], [-84597, -82783, -82249, -59661, -55505, -10046, 66121, 72504], [-67270, -51278, -28627, -11064, -5040, 9501, 19295, 29480, 32799]]) == [-55505, -36241]
assert solution.smallestRange([[-84567, -69253, -63331, -60953, 34843], [-98491, -45818, 9398, 10632, 26866, 87887, 97351], [94635], [-87684, -82016, 1655, 22519]]) == [22519, 94635]
assert solution.smallestRange([[13276, 58791], [-43057, 30276, 65137, 87060], [-19512, 43392], [-55890, -44482, -15946, 50794, 80552, 95523]]) == [43392, 65137]
assert solution.smallestRange([[-72838, -62886, -29118], [-96493, -48391, -45648, -29390, -6642, 21732, 36085, 45405, 83217], [-51888, -26994, -21009, -14915, 19772, 34370, 38830, 94165, 97719], [-92254, -78717, -76209, -47882, 23541, 52469, 56920, 75591, 84675]]) == [-62886, -47882]
assert solution.smallestRange([[-82955, 33286, 80281]]) == [-82955, -82955]
assert solution.smallestRange([[-78078, -62543, -57724, -41439, 26666, 62584]]) == [-78078, -78078]
assert solution.smallestRange([[34096, 50237, 51210]]) == [34096, 34096]
assert solution.smallestRange([[-67918], [-78162, -69113, -57366, -42414, -24182, 28666, 80336, 87352], [-99129, -89563, -68526, 17856]]) == [-69113, -67918]
assert solution.smallestRange([[-92931, -75548, -66061, -15132, -7784, 12647, 54721], [-83668, -34799, -29428, 41597, 49289, 66625, 96118]]) == [49289, 54721]
assert solution.smallestRange([[-99895, -25223, -22404, -14041, 13097, 16608, 20534, 73215, 98547], [-88560, -67462, -29651, -25637, -17166, 71006, 76394, 93722, 94187]]) == [-25637, -25223]
assert solution.smallestRange([[-16552, -5770, 53001], [-90260, -88640, -81674], [-14607, 20241, 96011], [-32362, 24990]]) == [-81674, -14607]
assert solution.smallestRange([[-81568, -51289, -1953, 15993, 20741, 44310, 86394]]) == [-81568, -81568]
assert solution.smallestRange([[80103, 83746, 98444], [-15435, 9568, 18567, 53003], [-11511, 63646], [-90652, -84870, -73880, -45468, -21941, -8505, -5340, 140, 14565]]) == [14565, 80103]
assert solution.smallestRange([[-73431, -45338, -35135, -34140, 555, 3367, 39893, 52635, 84387], [99201]]) == [84387, 99201]
assert solution.smallestRange([[-94551, 64440, 70911, 76733, 88631], [-81838, -31811, -18355, 7503, 15302, 20485, 53856, 54720, 64867, 70578]]) == [70578, 70911]
assert solution.smallestRange([[-98293, -86569, -71805, -71416, -52009, -15077, -14827, 1941, 50040, 71960], [-41554, -40378, -29910, -29279, -19191, 24475, 39479, 58260, 72461], [-86509, -57879, -55788, -25283, -12278, 6987, 41726, 51501, 97973, 98458], [-58104, 72909]]) == [-58104, -41554]
assert solution.smallestRange([[-22070], [49339]]) == [-22070, 49339]