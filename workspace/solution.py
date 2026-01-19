from typing import List

class InvalidHeightError(Exception):
    pass

def trap(height: List[int]) -> int:
    if any(not isinstance(h, int) or h < 0 for h in height):
        raise InvalidHeightError("Heights must be non-negative integers.")

    n = len(height)
    if n < 3:
        return 0

    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])

    return water_trapped