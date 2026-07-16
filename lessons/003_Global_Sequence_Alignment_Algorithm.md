# Global Sequence Alignment Algorithm

In the last lesson we learned the motivation behind sequence alignment. We learned how it can help us measure similarity between two DNA sequences by explaining the most likely series of mutations that transformed one sequence into the other.

In this lesson we'll go deeper into learning how a sequence alignment algorithm actually works. More specifically, we'll look at <b>Global Sequence Alignment</b> which just means that we are aligning the entirety of both sequences to each other.

## 1. Scoring Scheme

First, we can define our scoring scheme as a function `f()` that takes in two strings representing single characters. It checks if the characters match or if one of them is a gap and returns their score.

The code for this would look as follows (you can also find it in `002_003_sequence_alignment.ipynb`):

```
GAP = "-"
MATCH = 1
MISMATCH = -1
GAP_PENALTY = -1

def f(char_1, char_2):
    if char_1 == GAP or char_2 == GAP:
        return GAP_PENALTY
    elif char_1 == char_2:
        return MATCH
    else:
        return MISMATCH
```

This helps us abstract the scoring scheme from the actual algorithm so that we can change in the future and it won't change the code for our algorithm.

## 2. Intuition

Next, we need to think about how we actually go about aligning the sequences.

Maybe we start reading left to right and check whether adding a gap in the next spot would lead to an optimal score scheme?

We have 3 possible cases:

1. We add a gap in the top sequence
2. We add a gap in the bottom sequence
3. We don't insert any gaps and just align the next two characters

<br>

![alt text](..\data\images\image-2.png)

We could do this, but let's think about it a little more...

The problem is that every decision affects all future decisions. A gap that looks bad right now might allow many future matches.

Using the previous example:

> ACGTC<br>
> ACGC

If we are currently at this step and want to choose the next alignment:

> ACG<br>
> ACG

It might be tempting to avoid adding a gap right away and to try to align all the characters:

> ACGTC <br>
> ACGC-

But as we saw, this gives a suboptimal score of 1 + 1 + 1 + (-1) + (-1) = 2. Whereas, adding a gap first gives the optimal score of 1 + 1 + 1 + (-1) + 1 = 3:

> ACGTC<br>
> ACG-C

So, to guarantee that we make the right choice, we need to make calculations for all of the future steps that come after it.

If we work by reading left to right, then for each of the 3 cases for one step, we need to calculate the 3 cases for the next step right and so on, and so on...

![alt text](..\data\images\image-1.png)

This ends up taking a lot longer than we want. Also, we end up <b>repeating work unnecessarily</b>.

For example, say we are at the following step:

> ACG<br>
> ACG

We would need to calculate all future paths for each of the 3 cases, including the path highlighted by the purple circles:
![alt text](..\data\images\image-3.png)

We then determine that the correct next step is case 1. So, we move on to calculating the optimal next step. However, we see that we have to recalculate the path starting at the purple circle once again:
![alt text](..\data\images\image-4.png)

This repeated work can become very inefficient, especially as the DNA sequences get longer.

## 3. Dynamic Programming

Luckily, there is a better way of going about this which is done by using <b>dynamic programming</b>.

> Dynamic Programming is a technique that breaks down complex problems into simpler subproblems, solving them once and reusing them as needed.

The way we do this for sequence alignment is by splitting the sequences into many smaller alignment problems.

Instead of asking:

> "What is the best alignment for these two entire DNA sequences?"

we ask many smaller questions such as:

> "What is the best alignment for just the first 3 letters of each sequence?"

or

> "What is the best alignment for the first 5 letters of one sequence and the first 4 letters of the other?"

Each of these smaller problems depends only on a few even smaller problems. By solving them in the right order and storing the answers in a table, we never have to solve the same problem twice.

The algorithm fills in this table one cell at a time until the final cell contains the score of the optimal alignment for the two full sequences.

We can also keep track of which previous cell gave the best score, allowing us to reconstruct the actual alignment after the table has been filled.

At this point, the important idea is not to memorize every detail of the algorithm, but to understand why it works: <b>rather than exploring every possible alignment over and over again, we solve each smaller problem once and reuse its answer whenever we need it.</b>

If you're interested in algorithms or computer science, there's much more to explore about dynamic programming and why this approach is guaranteed to find the optimal alignment. For this course, however, understanding the overall idea is enough, we'll focus on using the algorithm rather than proving why it works.

## Activities

Continue working through `002_003_sequence_alignment.ipynb` and experiment with how different scoring schemes affect the alignment for different sequences!
