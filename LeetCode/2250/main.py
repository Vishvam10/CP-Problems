class Solution:

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def binarySearch(arr, target):
            left, right = 0, len(arr)
            ans = None
            while left < right:
                mid = left + ((right-left)//2)
                if arr[mid] >= target:
                    ans = mid
                    right = mid
                else:
                    left = mid + 1
            return ans

        rectangles.sort()
        lengths = {}
        for x, y in rectangles:
            if y in lengths:
                lengths[y].append(x)
            else:
                lengths[y] = [x]

        heights = sorted(list(lengths.keys()))
        count = [0] * len(points)

        for idx, point in enumerate(points):
            x, y = point
            minHeightRectIdx = binarySearch(heights, y)
            if minHeightRectIdx is not None:
                for h in heights[minHeightRectIdx:]:
                    minLenRectIdx = binarySearch(lengths[h], x)
                    if minLenRectIdx is not None:
                        count[idx] += len(lengths[h]) - minLenRectIdx

        return count
