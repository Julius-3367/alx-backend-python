#!/usr/bin/env python3

from typing import Tuple

def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int, ...]:
  """Zooms in on an array by repeating each element multiple times.

  Args:
      lst: A tuple of integers.
      factor: The number of times to repeat each element (default is 2).

  Returns:
      A new tuple containing the zoomed-in elements.
  """

  zoomed_in: Tuple[int, ...] = tuple(item for item in lst for _ in range(factor))
  return zoomed_in

# Example usage
array = (12, 72, 91)  # Changed to a tuple as required by the type hint

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)  # Output: (12, 12, 72, 72, 91, 91)
print(zoom_3x)  # Output: (12, 12, 12, 72, 72, 72, 91, 91, 91)
