# Lesson 002: Sequence Alignment

We previously learned about detecting genomic signatures using GC content (Lesson 000) and k-mers (Lesson 001).

Genetic signatures can be useful for:

- Identifying mystery organisms by matching their signatures to ones you already have in a database
- Determining how similar organisms are genetically based on the similarity of their genomic signatures

It's important to remember: it is possible for genetic signatures between two organisms to be similar even if they are not closely related.

## Aside

In fact, there is some very cool research being done that shows how some organisms that are not closely related share similar signatures due to environmental pressures being coded into their DNA!

Bonus reading if you have time: <br>
https://uwaterloo.ca/computer-science/news/microbial-organisms-extreme-environments-similar-genomic-signatures-even-though-unrelated

## 1. Comparing DNA sequences

Genomic signatures are not the only way we can detect evolutionary relationships between organisms. We can also compare the DNA sequences directly between pairs of organisms and see what differences they have.

## 2. Hamming Distance

We can start with a simple example. Say we are comparing 2 DNA sequences of the same length:

> ATCTTAGAG<br>
> ATGATAGCG

The first thing we might want to do is count in how many places the nucleotides differ. This is known as the <b>Hamming Distance</b>.

We see that in the example above, the characters differ in 3 different positions. Hence, the Hamming Distance is 3.

> AT<b>C</b><b>T</b>TAG<b>A</b>G<br>
> AT<b>G</b><b>A</b>TAG<b>C</b>G

Intuitively, we can tell that the smaller the Hamming Distance, the more similar two sequences are.

So, if we were dealing with two very long strands of DNA, we could code a program that reads through both entirely and calculates the Hamming Distance.

That would be a metric that tells us something about how similar the two DNA sequences are.

## 3. Sequence Alignment

However, the key assumption with Hamming Distance is that the sequences will be the same length.

We don't want to limit ourselves with this assumption which is why we'll learn about a more sophisticated way of comparing DNA: <b>Sequence Alignment</b>.

> Instead of simply lining up the sequences from left to right and counting the differences, <b>Sequence Alignment</b> positions the sequences and inserts gaps to <b>achieve the highest number of matching characters</b>.

> Global Sequence Alignment is when you want to align the entirety of both sequences.

We'll use a simple example. Say we have two organisms who each have the corresponding DNA:

> ACGTC <br>
> ACGC

We see that the first 3 characters align and after that we're not sure what to do.

### Types of Edits

We hold the assumption that two organisms who have the above DNA originally came from the same ancestor and evolved separately (this means that they are <b>homologs</b>). Then, we have several choices for what could have happened:

#### 1. Indel

1. The ancestor's DNA was: "ACGC" and the 'T' was inserted into the top organism's DNA:

   > ACGC -> ACG<b>T</b>C<br>
   > ACGC -> ACG<b>-</b>C

2. The ancestor's DNA was: "ACGTC" and the 'T' was deleted from the bottom organism's DNA:

   > ACGTC -> ACG<b>T</b>C<br>
   > ACGTC -> ACG<b>-</b>C

These first two cases can be grouped into one type of edit called an <b>indel</b> (short for "insertion/deletion"). From the aligned sequences alone, we cannot determine whether the T was inserted into one DNA strand or deleted from the other and so we represent the change as an indel with a gap symbol "-".

#### 2. Substitution

3. The ancestor's DNA was: "ACGC", then 'C' was substituted with 'T' in the top organism's DNA. Then an extra 'C' was added afterwards,

   > ACGC -> ACG<b>T</b> -> ACGT<b>C</b> <br>
   > ACGC -> ACG<b>C</b> -> ACGC<b>-</b>

4. The ancestor's DNA was: "ACGC", then an extra 'C' was added afterwards. Then 'C' was substituted with 'T' in the top organism's DNA.
   > ACGC -> ACGC<b>C</b> -> ACG<b>T</b>C <br>
   > ACGC -> ACGC<b>-</b> -> ACG<b>C</b>-

Similarly, we can't differentiate between these last two cases based on the sequences alone. But we know that they both involve a substitution from 'C' to 'T'.

We can come up with more cases for what could have happened (hint: cases 3 or 4 but the ancestor's DNA was: "ACGTC") but they will still involve these 2 fundamental types of edits: <b>indels and substitutions</b>.

## 4. Optimal Alignment

We have just seen that there are many ways that we could align these two sequences.

If we chose that an indel happened for 'T', we would have ended up with the following alignment:

> ACGTC<br>
> ACG-C

Now, if we count the number of matching characters we get 4!

If we chose the substitution case, we would end up with the alignment:

> ACGTC <br>
> ACGC-

Here, the number of matching characters is only 3 since 'T' and 'C' don't match and 'C' and the gap '-' also don't match.

### So, which alignment is better?

From a biological perspective, we want to find the alignment that best explains the most likely series of mutations that transformed one sequence into the other.

Finding the optimal alignment helps us measure how similar two DNA sequences are and provides insight into their evolutionary relationship.

At first, the intuitive idea might be that the optimal alignment is the one that inserts gaps (indels) to achieve the highest number of matching characters.

For a simpler example, we start with:

> ACGT <br>
> AGGT

We can just add two insertions to get 3 matches.

> <b>A</b>C-<b>G</b><b>T</b> <br>
> <b>A</b>-G<b>G</b><b>T</b>

However, in real DNA sequences, <b>not all mutations are equally likely</b>. Insertions and deletions generally occur less frequently than substitutions and can have larger effects on a sequence.

This means that we want to be sensible about how often we use these gaps. Plus, they sometimes might be unnecessary to get the optimal number of matches. With the same example, we can see that if we hadn't inserted any gaps, there still would have been 3 matches:

> <b>A</b>C<b>G</b><b>T</b> <br>
> <b>A</b>G<b>G</b><b>T</b>

This motivates us to develop better ways of scoring alignments, where different types of mutations are assigned different scores to find the most biologically meaningful alignment.

## 5. Scoring Alignments

Remember how we defined Sequence Alignment above as rearranging the sequences and inserting gaps to <b>achieve the highest number of matching characters</b>.

Now, we are going to correct this definition to "<b>achieve the highest score.</b>"

Up until now, we have been scoring an alignment by giving <b>+1</b> for each matching character and <b>0</b> for everything else.

But, we can also decide to penalize mismatches. This means that we score them as a negative number like <b>-1</b>, <b>-2</b> or even <b>-10</b>. This will prevent us from using too many indels as in the example above.

Let's stick with scoring matches as <b>+1</b> and mismatches as <b>-1</b> and go back to the first example:

For the indel case, the score would now be 1 + 1 + 1 + (-1) + 1 = 3:

> ACGTC<br>
> ACG-C

For the substitution case, the score would be 1 + 1 + 1 + (-1) + (-1) = 2:

> ACGTC <br>
> ACGC-

Since we are trying to find the optimal score, the first alignment is better (3 > 2).

We can come up with many different scoring schemes to reflect biological contexts. A common one is having a separate penalty for gaps versus character mismatches since indels are less likely to occur than substitutions in real life DNA mutations.

## Activities

In `002_003_sequence_alignment.ipynb`, work up to section 3. Hamming Distance. To then move onto Section 4, you should first go through the next Lesson 003: Global Sequence Alignment to learn about how the algorithm works!
