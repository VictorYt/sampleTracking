#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
:Author: Victor Ythier
:Date: 02.12.2020

This script check all calling in file directory and report a resum table at specific position
List of seven rs :
    - rs1801133
    - rs1045642
    - rs1128503
    - rs2306283
    - rs9934438
    - rs2108632
    - rs1135840
"""

# IMPORT
import os, glob
import pandas as pd
from collections import OrderedDict
from scripts import sampleTracking_function
from _version import __version__


REFERENCE = OrderedDict([('rs1801133','G/G'),
                         ('rs1045642','A/A'),
                         ('rs1128503','A/A'),
                         ('rs2306283','A/A'),
                         ('rs9934438','G/G'),
                         ('rs2108622','C/C'),
                         ('rs4680','G/G'),
                         ('rs1135840','C/C')])
cols = list(REFERENCE.keys())
cols.insert(0, 'Samples')
dfFinal = pd.DataFrame(columns=cols)

def main(dfinal):
    """
    Create a genotype summary table of all Variant to Table in the current directory
    :return:
    """
    # List of file
    all_samples = glob.glob("*.tsv")
    output = os.path.basename(os.getcwd()) + '.tsv'
    for s in all_samples:
        iterarray = []
        df = pd.read_csv(s, header=0, sep="\t")
        sample = s.replace(".tsv", "")
        iterarray.append(sample)
        for key, value in REFERENCE.items():
            if key not in df['ID'].tolist():
                iterarray.append(value)
            else:
                idx = df[df['ID']==key].index[0]
                genotype = sampleTracking_function.getGenotype(df, idx)
                iterarray.append(genotype)
        iterdict = dict(zip(dfinal.columns, iterarray))
        dfinal = dfinal.append(iterdict, ignore_index=True)

    #dfinal = dfinal.groupby(dfinal.columns.tolist()).size().reset_index().rename(columns={0: 'records'})
    dfinal = dfinal.set_index(dfinal.columns[0])
    dup_info = dfinal.duplicated(keep=False)
    dup_info.to_csv("Duplication_information.tsv", sep="\t", header=['Duplication_information'])
    dfinal.to_csv(output, sep="\t", index=True)

# Execution
if __name__ == "__main__":
    main(dfFinal)
