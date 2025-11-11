# Short Primer on Entropy

#### Why Information Theory is the most fundamental field of all

![Short Primer on Entropy](/images/entropy.png)
Composition VII (1913) - high entropy abstract art

### Shannon Entropy

Count freq. of each letter in a string:

`c = Counter(string)`

Percentage share of each letter:

`freqs = [c[i] / float(len(string)) for i in c]`

Shannon entropy:

`return -1 * sum([f * log(f, 2) for f in freqs])`

{{< postfoot >}}
**In Progress** Published on 11-09-25
{{</ postfoot >}}
