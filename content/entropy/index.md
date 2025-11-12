# Short Primer on Entropy

#### Why Information Theory is the most fundamental field of all

![Short Primer on Entropy](/images/entropy.png)
Composition VII (1913) - high entropy abstract art

### What is Information Theory?

The field of understanding the properties of data sources
like how much "surprise" is in a source and how to package data such that
communication contains only meaningful content.


**Entropy = average amount of surprise of a data source**

### Binary Digit vs Bit

There's a difference, okay!!

_Binary Digit_ = 0 or 1

**Bit = store of information**

- log2(n) bits of information in an event with n possible outcomes
- Intuitively: how many yes/no questions must I ask to know the outcome of a random event?

_Example:_ Flipping a Coin:

- Two possible outcomes: heads or tails
- log2(2) = 1 bit of information required
- "Is the outcome tails?" is False -> Heads; same for the inverse

_Example:_ Rolling a Dice:

- Six possible outcomes
- log2(6) = ~2.58 bits required
- "Is the outcome even?" is False and "1 or 3?" is False -> 5
- "Is the outcome even?" is False and "1 or 3?" is True and "1?" is False -> 3
- Why 2.58 bits makes sense: sometimes 2 questions are needed, sometimes 3 - but never more




### Shannon Entropy

Count freq. of each letter in a string:

`c = Counter(string)`

Percentage share of each letter:

`freqs = [c[i] / float(len(string)) for i in c]`

Shannon entropy:

`return -1 * sum([f * log(f, 2) for f in freqs])`

{{< postfoot >}}
**In Progress** Published on 11-09-25 Updated on 11-12-25
{{</ postfoot >}}
