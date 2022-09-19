# -*- coding: utf-8 -*-
import os
import re
import random
from random import sample
from Bio import SeqIO
from math import floor
from typing import List
from pecanpy.wrappers import Timer


@Timer('load DNA seqs')
def parse_seq(path_to_input: str):
    """ Return a list containing DNA seqment(s) captured in fna file(s)."""
    seq_files = list()
    for input_file_dir in path_to_input:
        for root, dirs, files in os.walk(input_file_dir):
            for file in files:
                if file.endswith('.fna'):
                    seq_files.append(os.path.join(root, file))

    seqs = list()
    for seq_file in seq_files:
        for seq_record in SeqIO.parse(seq_file, 'fasta'):
            seq = re.sub('[^ACGTacgt]+', '', str(seq_record.seq))
            seqs.append(seq.upper())

    print('There are ' + str(len(seqs)) + ' seqs')

    return seqs


def extract_kmer(seq: str, mer: int):
    """ Return a DNA sequence's k-mers. Slide only a single nucleotide """
    return [seq[i:i + mer] for i in range(len(seq) - mer + 1)]


@Timer('seg2sentence')
def seg2sentence(segs: List[str], mer: int = 8):
    """ Express a segment in NLP sentence style.
    Note:
        ['segments'] --> ['seg egm gme men ent nts']
    """
    return [' '.join(extract_kmer(seg, mer)) for seg in segs]

