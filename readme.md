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

### [--- Day 12: Garden Groups ---](https://adventofcode.com/2024/day/12)

*00:47:02* **5278** / *14:38:50* **19503**

I will eventually learn how to quickly code a Depth Fisrt Search. A debug phase is still necessary. I had the whole work day (and dinner too) to find a way to count the sides of a polygon. I like it when both parts share the same code structure and differ by one function like here.

### [--- Day 13: Claw Contraption ---](https://adventofcode.com/2024/day/13)

*00:33:05* **3623** / *01:00:47* **2850**

The statement misled me (I think it was intentional). Seeing that the brute force solution of part 1 would not work for part 2, and that all the *arithmetic* tracks were doomed to failure, I finally found the *analytical* solution that fits. + a little improvement in `aoc` module related to spliting with regexp.

### [--- Day 14: Restroom Redoubt ---](https://adventofcode.com/2024/day/14)

*00:22:27* **2403** / *>24h* **28920**

I tried a bunch of things to detect what might be a "Christmas tree" on Saturday. I gave up on Sunday and decided to build PNG files with 200 cards per image (I learned to use the [Pillow](https://pillow.readthedocs.io/en/stable/) module on this occasion.). A visual analysis finally gave me the solution.

### [--- Day 15: Warehouse Woes ---](https://adventofcode.com/2024/day/15)

*00:27:40* **1866** / *04:33:43* **5964**

### [--- Day 16: Reindeer Maze ---](https://adventofcode.com/2024/day/16)

*01:44:05* **5322** / *04:47:22* **6128**

### [--- Day 17: Chronospatial Computer ---](https://adventofcode.com/2024/day/17)

*01:01:05* **4542** / *10:03:01* **7821**

### [--- Day 18: RAM Run ---](https://adventofcode.com/2024/day/18)

*00:25:36* **3011** / *00:33:41* **2710**

Dijkstra again! Only the length is needed, not the path. The length of the shortest path is stored in the memory. That is easy. Brute force solution for part 2, testing each labyrinth in turn - 31sec. Maybe a search by dichotomy would have been better.

## `aoc.py`

All solutions use a helper module to ease reading input data. The structure of a solution script is:

```python
import aoc

if aoc.part == "one":
    # do part 1 processing

if aoc.part == "two":
    # do part 2 processing
```

At import, the `aoc` module parse the command line arguments. A `1` or a `2` is expected for obvious reason.

The `aoc`  module also defines a class named `Input`:

`Input(split=NoSplit, convert=None, groupby=None)`
Reads the *input.txt* file found in current directory (or the *test.txt* file if `-t`option is present in the command line), or prints an error and exits if file is missing or empty.

Once instanciated the object acts as an iterator over the lines of the file (`\n` char is removed from end of lines if present).
 The simplest usage is then:

```python
for line in aoc.Input():
	# do something with the line which is a str
```

`split` is an optional parameter. When used the iterator yields `list` instead of `str`:
 - `split=""`: yields the list of chars in line `==list(line)`

```python
# aoc24/12-GardenGroups
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
garden = list(aoc.Input(split="")) # list of lists of chars
rowmax = len(garden)
colmax = len(garden[0])
...
for row in range(rowmax):
    for col in range(colmax):
        # do something with garden[row][col]
```

 - `split=<str|None>`: yields `line.split(<str|None>)`

```python
# aoc24/07-BridgeRepair
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
for equationresult, equationumbers in aoc.Input(split=":"):
    ...
```

```python
# aoc23/12-HotSprings
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
 for springs, stats in aoc.Input(split=None):
     ...
```

 - `split=<re object>`: yields the matched groups of the regexp over the line or the entire line if no match. Examples:

```python
# aoc22/16_ProboscideaVolcanium
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
for valve, flow, tunnels in aoc.Input(split=re.compile(r'Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')):
```

`convert` is an optional callable that is applied on each items of the splitted line (or on the whole line if not splitted). The item is replaced by the result of the `convert()` call unless an exception is raised in which case the item is left unchanged.

```python
# aoc24/02-RedNosedReports
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
print(sum(safe(report) for report in aoc.Input(convert=int, split=" ")))
```

If specified, `groupby` should be a positive integer or the string "paragraph". In all cases, the `Input` object acts as an iterator of iterator. The inner iterators are those already described above. The outer iterator groups the lines by a constant number or depending of the presence of blank lines.

```python
# aoc22/03_RucksackReorganization
# dvvhtHJhwd
# SzRSM
# ffLer
# GCZfe
# nMzrffzefez
for rucksack1, rucksack2, rucksack3 in aoc.input(convert=set, groupby=3):
    ...
```

```python
# aoc24/13-ClawContraption
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176
for (Ax,Ay),(Bx,By),(Px,Py) in aoc.Input(split=re.compile(r"X[+=](\d+).*Y[+=](\d+)"), convert=int, groupby="paragraph"):    ...
```

