# Short Primer on Entropy

#### Why Information Theory is the most fundamental field of all

![Short Primer on Entropy](/images/entropy.png)
Composition VII (1913) - high entropy abstract art

{{< blocky >}}
**TLDR:** It can be argued that Information Theory is the most fundamental field of all
given that every physical law can be interpreted as an information processing algorithm. 
This implies that reality is computational. 
{{</ blocky >}}

### What is Information Theory?

[Formalized in the mid-20th century by Claude Shannon](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)

The field of understanding the properties of data sources
like how much "surprise" is in a source and how to package data such that
communication contains only meaningful content.


**Entropy = average amount of surprise of a data source**

### Binary Digit vs Bit

There's a difference, okay!!

__Binary Digit__ = 0 or 1

**Bit = store of information**

- log_2(n) bits of information in an event with n possible outcomes ([Why?](why/))
- Intuitively: how many yes/no questions must I ask to know the outcome of a random event?

Example: __Flipping a Coin:__

- Two possible outcomes: heads or tails
- log_2(2) = 1 bit of information per outcome
- "Is the outcome tails?" is False -> Heads; same for the inverse

Example: __Rolling a Dice:__

- Six possible outcomes
- log_2(6) = ~2.58 bits per outcome
- "Is the outcome even?" is False and "1 or 3?" is False -> 5
- "Is the outcome even?" is False and "1 or 3?" is True and "1?" is False -> 3
- Why 2.58 bits makes sense: sometimes 2 questions are needed, sometimes 3 - but never more

You may be thinking: "What if I get lucky and guess the right outcome, first try?":

**Information Theory is concerned with averages** - given an infinite amount of 
__independent events__, an average of log_2(n) bits are contained in each outcome.




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
