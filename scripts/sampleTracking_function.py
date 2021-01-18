#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
:Author: Victor Ythier
:Date: 24.09.2020

This script content function for the RunWatcher script:
    - getGenotype

"""

# IMPORT
import pandas as pd


def getGenotype(df, index):
    """
    Using the information about the rsID return the genotype in the wanted format
    :param df: [DataFrame] The table containing Variant calling
    :param index: [int] index of the rs ID
    :return: [str] Genotype in the format NT/NT
    """
    geno = None
    if df.iat[index, 6] == "[G*, A]":
        geno = "G/A"
    elif df.iat[index, 6] == "[A, A]":
        geno = "A/A"
    elif df.iat[index, 6] == "[A*, G]":
        geno = "A/G"
    elif df.iat[index, 6] == "[G, G]":
        geno = "G/G"
    elif df.iat[index, 6] == "[C*, T]":
        geno = "C/T"
    elif df.iat[index, 6] == "[T, T]":
        geno = "T/T"
    elif df.iat[index, 6] == "[G*, C]" and df.iat[index, 2] == "rs1135840":
        geno = "C/G"
    elif df.iat[index, 6] == "[G*, C]":
        geno = "G/C"
    elif df.iat[index, 6] == "[C, C]":
        geno = "C/C"
    return geno

