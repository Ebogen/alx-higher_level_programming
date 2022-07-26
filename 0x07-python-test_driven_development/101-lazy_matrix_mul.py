#!/usr/bin/python3
"""

a function that multiplies 2 matrices


"""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b

    """

    return (npy.matmul(m_a, m_b))
