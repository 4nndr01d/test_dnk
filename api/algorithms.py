import re

CHAIN = 'tgacccactaatcagcaacatagcactttgagcaaaggcctgtgttggagctattggccccaaaactgcctttccctaaacagtgttcaccattgtagacctcaccactgttcgcgtaacaactggcatgtcctgggggttaatactcac'

chain_arr = re.findall(r'.{3}', CHAIN)


def linear_search(codon):
    for chain in chain_arr:
        if chain == codon:
            return True
    return False


def simple_search(codon):
    return codon in chain_arr
