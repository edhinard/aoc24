# [Advent of Code 24](https://adventofcode.com/2024)

## Daily log

### [--- Day 1: Historian Hysteria ---](https://adventofcode.com/2024/day/1)

*00:08:40* **3750** / *00:11:25* **3184**

Happy to start this calendar.

### [--- Day 2: Red-Nosed Reports ---](https://adventofcode.com/2024/day/2)

*00:08:38* **1974** / *00:18:33* **2494**

Same time for first part as yesterday, but rank below 2000 (my motivation to wake up early everyday).

### [--- Day 3: Mull It Over ---](https://adventofcode.com/2024/day/3)

*00:07:09* **2672** / *00:16:05* **2597**

regexps do all the job.

### [--- Day 4: Ceres Search ---](https://adventofcode.com/2024/day/4)

*00:55:38* **10049** / *01:11:49* **8912**

So much time lost in doing complicated and useless things: building a table of horizontal then vertical then diagonal lines (ok, I know how to do it now). The second part made me realize I was in the wrong direction. Rewrite the solution afterwards seeking `MAS` around the `X`.

### [--- Day 5: Print Queue ---](https://adventofcode.com/2024/day/5)

*00:15:26* **2806** / *00:26:50* **2580**

One of the rare occasion to use the `groupby="paragraph"` option of `aoc.Input()`.

### [--- Day 6: Guard Gallivant ---](https://adventofcode.com/2024/day/6)

*00:25:21* **4869** / *00:49:33* **3220**

Brute force solution for part two (trying to put an obstacle at every location). Found afterwards that it is 4 times faster to put an obstacle only on visited places of first part.

### [--- Day 7: Bridge Repair ---](https://adventofcode.com/2024/day/7)

*00:14:10* **2467** / *00:41:32* **5047**

The same code for both parts. Only the list of operators changes. The solution for the race took 30 min to run on part 2. I rewrote the function in a recursive way while I despaired of ever having the result. Now 10 times faster.

### [--- Day 8: Resonant Collinearity ---](https://adventofcode.com/2024/day/8)

*00:17:37* **2050** / *00:49:45* **4807**

I should have read the title of the challenge before starting coding. This would have immediately made me think of using the determinant to test collinearity and avoid wasting 30 minutes.

### [--- Day 9: Disk Fragmenter ---](https://adventofcode.com/2024/day/9)

*01:15:12* **8321** / *03:47:32* **9578**

I love generators, it helped me finding an easy to read solution for part 1. It took me too much time though. I had to go to work where I finished part 2 using the no less beloved `dataclass`.

### [--- Day 10: Hoof It ---](https://adventofcode.com/2024/day/10)

*00:23:45* **3730** / *00:26:13* **3190**

I misread the instructions, as usual. So I coded the solution from part 2 for part 1 first. This served me well when it came time to code the former.

I have read that the input data should not be shared. From now on I will not push the *input.txt* file and will not write the solution in a comment.

### [--- Day 11: Plutonian Pebbles ---](https://adventofcode.com/2024/day/11)

*00:14:39* **3966** / *02:42:25* **9580**

I fell into the trap. I ran the solution of part 1 with `75` as main parameter. Not only did I not get a solution while I was looking for how to optimize the counting (hoping to do it like on day 7). But my PC froze. Finally I found it easily at the office.

## `aoc.py`

I wrote a helper module to ease reading input data. The structure of a solution script is:

```python
import aoc

if aoc.part == "one":
    # do part 1 processing

if aoc.part == "two":
    # do part 2 processing
```

At import, the `aoc` module parse the command line arguments. A `1` or a `2` is expected for obvious reason.

The `aoc`  module also defines a class named `Input` which reads the *input.txt* file found in current directory, or prints an error and exits if file is missing or empty. Once instanciated `Input` object acts as an iterator over the lines of *input.txt* file. `\n` char is removed from end of line if present