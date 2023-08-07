#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return
values with the appropriate types


"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Write a type-annotated function make_multiplier that takes a 
    float multiplier as argument and returns a function that 
    multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Function Callable"""
        return x * multiplier
    return multiplier_function
