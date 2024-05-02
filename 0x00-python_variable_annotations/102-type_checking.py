from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

# Added type annotations for zoom_2x and zoom_3x
zoom_2x: List[int] = zoom_array(array)
zoom_3x: List[int] = zoom_array(array, 3)

