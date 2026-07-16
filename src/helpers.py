from Bio import SeqIO
import numpy as np
from collections import defaultdict

#============================
# FASTA file Functions
def get_fasta_info(file_path):
    # Open the FASTA file
    with open(file_path, "r", encoding="utf-8") as fasta_file:
        record = SeqIO.read(fasta_file, "fasta")  # read in the FASTA records
        print(f"Description: {record.description}")
        print(f"Sequence: {record.seq[:20]}...")  # Print first 20 bases
        print(f"Length: {len(record)}\n")

def get_dna_seq(file_path):
    # Open the FASTA file
    with open(file_path, "r", encoding="utf-8") as fasta_file:
        record = SeqIO.read(fasta_file, "fasta")
        return record.seq

#============================
# GC content Functions
def get_nucleotide_count(dna_seq, nucleotide):
    return dna_seq.count(nucleotide)

def get_GC_content(dna_seq):
    g_count = get_nucleotide_count(dna_seq, "G")
    c_count = get_nucleotide_count(dna_seq, "C")
    dna_length = len(dna_seq)
    return ((g_count + c_count) / dna_length) * 100

def print_gc_content(dna_seq, organism):
    blue_font = "\033[34m"
    reset_font = "\033[0m"
    gc_content = get_GC_content(dna_seq)
    print(f"{organism}: {blue_font}{gc_content:.2f}%{reset_font}")

#============================
# k-mer Functions
def print_kmer_count(kmer_count, organism, extra_info: str = ""):
    blue_font = "\033[34m"
    reset_font = "\033[0m"
    if extra_info:
        extra_info_str = f" ({extra_info})"
    else:
        extra_info_str = ""
    print(f"{organism}: {blue_font}{kmer_count:.2f}%{reset_font} {extra_info_str}")

def count_kmers(dna_seq, k):
    """Returns the kmer counts dictionary and the total
       number of kmers in the sequence."""
    kmer_counts = defaultdict(int)
    for i in range(len(dna_seq) - k):
        kmer = dna_seq[i:i+k]
        kmer_counts[kmer] += 1

    return kmer_counts, len(dna_seq) - k

def get_kmer_percentage(kmer_count, total_kmer_count):
  return (kmer_count / total_kmer_count) * 100

#============================
# Hamming Distance
def get_hamming_distance(seq_1, seq_2):
    hamming_distance = 0
    seq_1_print = []
    seq_2_print = []
    red_font = "\033[31m"
    reset_font = "\033[0m"

    for char_1, char_2 in zip(seq_1, seq_2):
        if char_1 != char_2:
            hamming_distance += 1

            # Rewrite both sequences with red font where the characters differ
            seq_1_print.append(f"{red_font}{char_1}{reset_font}")
            seq_2_print.append(f"{red_font}{char_2}{reset_font}")

        else:
            seq_1_print.append(char_1)
            seq_2_print.append(char_2)

    seq_1_print = "".join(seq_1_print)
    seq_2_print = "".join(seq_2_print)

    return hamming_distance, seq_1_print, seq_2_print

#============================
# Global Sequence Alignment
GAP = "-"

def f(char_1: str, char_2: str) -> int:
    if char_1 == GAP or char_2 == GAP:
        return GAP_PENALTY
    elif char_1 == char_2:
        return MATCH
    else:
        return MISMATCH

def get_dp_matrices(S: str, T: str) -> tuple[np.ndarray, np.ndarray]:
    m = len(S)
    n = len(T)
    scores = np.zeros((m + 1, n + 1), dtype=int)
    pointers = np.zeros((m + 1, n + 1), dtype=int)

    # set top-left corner of pointers matrix to
    # having no further pointers
    pointers[0, 0] = 3

    # setting negative decrements for each '-' that
    # is matched with a character in S or T
    for i in range(1, m+1):
        scores[i,0] = scores[i-1, 0] + f(S[i-1], GAP)
        pointers[i,0] = 1

    for i in range(1, n+1):
        scores[0, i] = scores[0, i-1] + f(GAP, T[i-1])
        pointers[0, i] = 2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # calculate all possible scores
            score_options = np.array([
                scores[i - 1, j - 1] + f(S[i - 1], T[j - 1]), # diagonal
                scores[i - 1, j] + f(S[i - 1], GAP),          # up
                scores[i, j - 1] + f(GAP, T[j - 1]),          # left
            ])

            # find the largest score
            scores[i, j] = np.max(score_options)

            # find and set the parent of largest score
            pointers[i, j] = int(np.argmax(score_options))

    return scores, pointers

def backtrack(
    i: int,
    j: int,
    pointers: np.ndarray,
    S: str,
    T: str,
) -> tuple[str, str]:
    # Initialize the S and T alignments as lists of strings
    # The characters from S and T will be added to these lists
    # from right to left
    S_aligned = []
    T_aligned = []

    # Recursive Case
    # Make your way from the bottom-right corner of the pointers matrix
    # up to the top-left corner
    while pointers[i, j] != 3:
        if pointers[i, j] == 0:
            S_aligned.append(S[i - 1])
            T_aligned.append(T[j - 1])
            i -= 1
            j -= 1
        elif pointers[i, j] == 1:
            S_aligned.append(S[i - 1])
            T_aligned.append(GAP)
            i -= 1
        elif pointers[i, j] == 2:
            S_aligned.append(GAP)
            T_aligned.append(T[j - 1])
            j -= 1

    # Reverse the strings
    S_aligned = "".join(reversed(S_aligned))
    T_aligned = "".join(reversed(T_aligned))

    return S_aligned, T_aligned

def get_alignment(S: str, T: str) -> tuple[str, str, int]:
    m = len(S)
    n = len(T)

    # run the alignment score calculations
    scores, pointers = get_dp_matrices(S, T)

    # max score is at the bottom-right corner of the scores matrix
    max_score = int(scores[m, n])

    # call the backtrack function starting at the bottom-right corner
    S_aligned, T_aligned = backtrack(m, n, pointers, S, T)

    return S_aligned, T_aligned, max_score