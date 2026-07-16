# Lesson 001: k-mers

Recall that DNA strands are incredibly long strings and
we want to be able to detect genomic signatures within these strings.

In the last lesson, we learned the first way of detecting these signatures: GC content. At the base, this was essentially counting the number of 'G' and 'C' characters that appeared in a string.

If you looked at the bonus section of the exercise, you saw that we could also just as easily count how many 'A's there were or how many 'T's.

We can now extend this idea to counting not just individual characters but groups of letters too!

For example, in the sequence "ATCGATGCTAT", we can count how many times the subsequence "AT" appears: "<b>AT</b>CG<b>AT</b>GCT<b>AT</b>"

That brings us to k-mers!

## 1. k-mers

> A k-mer is a substring of length _k_ taken from a DNA sequence.

Following the idea above, if we were to now try finding the count of how many times the string "AT" appears in a sequence of DNA, we are looking for a string of length 2. So, this is a 2-mer.

Similarly to how scientists noticed that some organisms exhibit larger numbers of certain nucleotides (like 'G' or 'C') in their DNA, it is possible that certain organisms exhibit larger counts of certain 2-mers than others.

We can test this idea by looking at the counts for all possible 2-mers in an organism's DNA.

There would $4 \times 4$ possibilities of 2-mers:

- "AA", "AC", "AG", "AT"
- "CA", "CC", "CG", "CT"
- "GA", "GC", "GG", "GT"
- "TA", "TC", "TG", "TT"

For example, say we had the sequence "ATCGATGCTAT", then we would go through it from the start:

1. Index 0: the first two characters are "AT", so we can count 1 of "AT" so far
2. Index 1: the two characters are "TC", so we can can count 1 of "TC" so far
3. Index 2: we count 1 of "CG"
4. Index 3: we count 1 of "GA"
5. Index 4: we come across "AT" again and now have 2 counts of "AT"

And we go through this until we reach the last 2 characters of the sequence.

## 2. Larger _k_

Remember: we don't have to limit ourselves to only 2-mers. We could use any subsequence length we want: 3-mers, 10-mers, etc.

It's important to note that as _k_ gets larger, the amount of possible strings increases exponentially. So if we were using 3-mers, we would have $4^3$ possible strings: "AAA", "AAC", "AAG", ...

In fact, for a k-mer, we have $4^k$ possible strings. This is because there are k possible spaces: \_\_, \_\_, ..., \_\_. Each space has 4 options ('A', 'C', 'G', 'T') and we multiply the number of options for each of the spaces: <br> $4 \times 4 \times ... \times 4 = 4^k$.

So, if we use very long k-mers, then we would have to store a very large dictionary to keep track of all the counts.

At some point, if we have a longer string, it loses generality and makes it less likely that we find k-mers with significantly large counts. This is why it's important to find a tradeoff between the length of your k-mer and what kind of detail you want to capture. Common k-mer lengths are often between 3-6.

## 3. How to store k-mer counts in Python

Before, we were getting away with just counting the individual characters and storing them in a variable (e.g. `g_count`). But now we have to be more organized if we want to keep track of the counts for all of these possible k-mers.

We can use a great data structure called a <b>dictionary</b> which is perfect for storing counts.

> A dictionary stores information as a list of key-value pairs.

We can use this so that the k-mer strings are the keys and their counts in a DNA sequence are the values:

```
{
    "AA": 1,
    "AC": 2,
    "AG: 1,
    ...
}
```

This k-mer count dictionary serves as a new type of genomic signature!

## 5. Activity

If you open `001_kmers.ipynb`, we will implement what we have learned in this lesson and see how k-mer counts can be used to differentiate between organisms.
