"""
Options:
  Linear
  Binary
  Jump

Problem = [False, False, False, True, True, True, True], when is it true, and how do we find where the most optimized way.
"""
import math

def crystal_ball(height, break_height):
    jump_size = int(math.sqrt(height))
    left = 0
    right = jump_size

    # Perform jump search to find the breaking point of the first ball
    while right < height and height[right] < break_height:
        left = right
        right += jump_size

    # Perform linear search to find the exact breaking point
    for floor in range(left, min(right + 1, height)):
        if floor >= break_height:
            breaking_point = floor
            break
    else:
        breaking_point = -1  # First ball didn't break

    highest_point = breaking_point + 1

    return breaking_point, highest_point
