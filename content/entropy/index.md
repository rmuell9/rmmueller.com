# Short Primer on Entropy

#### One of the most important concepts in thermodynamics and information theory has a beautiful generalization

### Shannon Entropy

Count freq. of each letter in a string:

`c = Counter(string)`

Percentage share of each letter:

`freqs = [c[i] / float(len(string)) for i in c]`

Shannon entropy:

`return -1 * sum([f * log(f, 2) for f in freqs])`
