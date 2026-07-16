# Lesson 0: How is DNA stored as data?

## 1. What is DNA?

DNA contains all the instructions an organism needs to build, maintain itself and reproduce. It consists of 4 different molecules called <b>nucleotides</b> that are joined together in long strands. The molecules are:

- Adenine (A)
- Thymine (T)
- Cytosine (C)
- Guanine (G)

The way DNA is structured is actually as a double-helix where the nucelotides A and T must match together and C and G must match together:

![alt text](..\data\images\image.png)

## 2. How does a computer store DNA?

In order to analyze DNA, we first need to answer: <b>How does a computer store DNA?</b>

First, we shorten the names of the nucleotides to just their letters. So, a piece of DNA could look like:

> A T C G A T<br>
> T A G C T A

Second, since we know that A and T must match together and C and G must match together, storing both strings would be redundant. So, we pick only one of the strings to store:

> A T C G A T

And this is exactly how computers store DNA! As strings made of these 4 letters.

The standard method used in bioinformatics to store DNA is through a <b>FASTA file</b>. Its format is very simple and just consists of a header line starting with '>' that contains the name and a description of the organism, followed by the DNA string:

> \>NM_001301720.2 Homo sapiens BRCA1, DNA repair associated
> ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAA
> ATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGA
> CCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACA...

## 3. How is DNA analyzed?

Because DNA strands are significantly longer than the examples shown, computing has become essential for analyzing DNA.

There are many reasons why we would want to analyze DNA. Some examples include:

- Finding the organism with the closest-matching DNA
- Tracking DNA mutations of an organism over time (e.g. COVID virus tracking)
- Discovering the evolutionary history between different organisms

> The core idea is that we want to be able to find <b>genomic signatures</b> within the DNA that give clues about its evolution.

There are so many ways that we can go about analyzing DNA and there is no one correct answer. Oftentimes, scientists use a mix of different techniques which is what we will do by the end of the week!

## 4. GC Content

The first analysis we can do is actually quite simple! We can calculate the <b>GC content</b>.

This is essentially just a count of the total number Gs and Cs over the total number of letters in the string. We count both because we know that they bind to each other so if one appears on a strand, the other will appear on the other strand.

The formula is:
$$ GC\% = \frac{\# G + \# C}{\# G + \# C + \# A + \# T} \times 100$$

Why exactly would we want to analyze this? Well, it is a very simple <b>genomic signature</b>.

It has been observed that different organisms tend to have different average GC contents. By measuring the GC content of an unknown DNA sequence, scientists can sometimes narrow down which organism it came from or identify unusual regions of a genome.

## 5. Activity

If you open `000_GC_content.ipynb`, we will implement reading from a FASTA file and calculating GC content!
