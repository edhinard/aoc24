# [Advent of Code 24](https://adventofcode.com/2024)

## [--- Day 1: Historian Hysteria ---](https://adventofcode.com/2024/day/1)

*00:08:40* **3750** / *00:11:25* **3184**

Happy to start this calendar.

## [--- Day 2: Red-Nosed Reports ---](https://adventofcode.com/2024/day/2)

*00:08:38* **1974** / *00:18:33* **2494**

Same time for first part as yesterday, but rank below 2000 (my goal for all *).

## [--- Day 3: Mull It Over ---](https://adventofcode.com/2024/day/3)

*00:07:09* **2672** / *00:16:05* **2597**

regexps do all the job.

## [--- Day 4: Ceres Search ---](https://adventofcode.com/2024/day/4)

*00:55:38* **10049** / *01:11:49* **8912**

So much time lost in doing complicated and useless things: building a table of horizontal then vertical then diagonal lines (ok, I know how to do it now). The second part made me realize I was in the wrong direction. Rewrite the solution afterwards.

## [--- Day 5: Print Queue ---](https://adventofcode.com/2024/day/5)

*00:15:26* **2806** / *00:26:50* **2580**

One of the rare occasion to use the `groupby="paragraph"` option of `aoc.Input()`.

## [--- Day 6: Guard Gallivant ---](https://adventofcode.com/2024/day/6)

*00:25:21* **4869** / *00:49:33* **3220**

Brute force solution for part two (trying to put an obstacle at every location). Found afterwards that it is 4 times faster to put an obstacle only on visited places of first part.

## [--- Day 7: Bridge Repair ---](https://adventofcode.com/2024/day/7)

*00:14:10* **2467** / *00:41:32* **5047**

The same code for both parts. Only the list of operators changes. The solution for the race took 30 min to run on part 2. I rewrote the function in a recursive way while I despaired of ever having the result. Now 10 times faster but came too late.

## [--- Day 8: Resonant Collinearity ---](https://adventofcode.com/2024/day/8)

*00:17:37* **2050** / *00:49:45* **4807**

I should have read the title of the challenge before starting coding. This would have immediately made me think of using the determinant to test collinearity and avoid wasting 30 minutes.

## [--- Day 9: Disk Fragmenter ---](https://adventofcode.com/2024/day/9)

*01:15:12* **8321** / *03:47:32* **9578**

I love generators, it helped me finding an easy to read solution for part 1. It took me too much time though. I had to go to work where I finished part 2 using the no less beloved `dataclass`.

## [--- Day 10: Hoof It ---](https://adventofcode.com/2024/day/10)

*00:23:45* **3730** / *00:26:13* **3190**

