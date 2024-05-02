                                README

This repository serves as a practice ground for exploring type annotations in Python. It consists of various exercises that involve implementing functions with type hints for arguments and return values.

Exercises:

1. Basic Annotations:

add(a: float, b: float) -> float: Defines a function add that takes two floats a and b and returns their sum as a float.
2. Basic Annotations - String Concatenation:

concat(str1: str, str2: str) -> str: Defines a function concat that takes two strings str1 and str2 and returns the concatenated string.
3. Basic Annotations - Floor Function:

floor(n: float) -> int: Defines a function floor that takes a float n and returns the floor (integer part) of the number.
4. Basic Annotations - To String:

to_str(n: float) -> str: Defines a function to_str that takes a float n and returns its string representation.
5. Define Variables:

Defines several variables with specific types:
a: int = 1 (integer)
pi: float = 3.14 (float)
i_understand_annotations: bool = True (boolean)
school: str = "Holberton" (string)
6. Complex Types - List of Floats:

sum_list(input_list: List[float]) -> float: Defines a function sum_list that takes a list input_list containing floats and returns their sum as a float.
7. Complex Types - Mixed List:

sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float: Defines a function sum_mixed_list that takes a list mxd_lst containing integers or floats and returns their sum as a float.
8. Complex Types - String and Int/Float to Tuple:

to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]: Defines a function to_kv that takes a string k and an integer/float v and returns a tuple (k, v**2) where v**2 is the square of v (a float).
9. Complex Types - Functions:

make_multiplier(multiplier: float) -> Callable[[float], float]: Defines a function make_multiplier that takes a float multiplier and returns a new function that multiplies any input float by the original multiplier.
10. Duck Typing an Iterable:

element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]: Annotates an existing function element_length that takes an iterable lst containing sequences (strings or lists) and returns a list of tuples where each tuple contains the sequence and its length (integer).
