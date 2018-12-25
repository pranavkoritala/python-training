# Calendar module exercises

import calendar

print(calendar.isleap(2016))
print(calendar.month(2018, 4))
print(calendar.calendar(2019, 2, 1, 5))  # Year, width, lines, space betwwen each month
print(calendar.calendar(2010, 2, 1, 2))

'''
Output:
---------------------------------------
True
     April 2018
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

                                 2019

      January                  February                  March
Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                  1  2  3                  1  2  3
 7  8  9 10 11 12 13      4  5  6  7  8  9 10      4  5  6  7  8  9 10
14 15 16 17 18 19 20     11 12 13 14 15 16 17     11 12 13 14 15 16 17
21 22 23 24 25 26 27     18 19 20 21 22 23 24     18 19 20 21 22 23 24
28 29 30 31              25 26 27 28              25 26 27 28 29 30 31

       April                     May                      June
Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7            1  2  3  4  5                     1  2
 8  9 10 11 12 13 14      6  7  8  9 10 11 12      3  4  5  6  7  8  9
15 16 17 18 19 20 21     13 14 15 16 17 18 19     10 11 12 13 14 15 16
22 23 24 25 26 27 28     20 21 22 23 24 25 26     17 18 19 20 21 22 23
29 30                    27 28 29 30 31           24 25 26 27 28 29 30

        July                    August                 September
Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7               1  2  3  4                        1
 8  9 10 11 12 13 14      5  6  7  8  9 10 11      2  3  4  5  6  7  8
15 16 17 18 19 20 21     12 13 14 15 16 17 18      9 10 11 12 13 14 15
22 23 24 25 26 27 28     19 20 21 22 23 24 25     16 17 18 19 20 21 22
29 30 31                 26 27 28 29 30 31        23 24 25 26 27 28 29
                                                  30

      October                  November                 December
Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su     Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                  1  2  3                        1
 7  8  9 10 11 12 13      4  5  6  7  8  9 10      2  3  4  5  6  7  8
14 15 16 17 18 19 20     11 12 13 14 15 16 17      9 10 11 12 13 14 15
21 22 23 24 25 26 27     18 19 20 21 22 23 24     16 17 18 19 20 21 22
28 29 30 31              25 26 27 28 29 30        23 24 25 26 27 28 29
                                                  30 31

                              2010

      January               February               March
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
             1  2  3   1  2  3  4  5  6  7   1  2  3  4  5  6  7
 4  5  6  7  8  9 10   8  9 10 11 12 13 14   8  9 10 11 12 13 14
11 12 13 14 15 16 17  15 16 17 18 19 20 21  15 16 17 18 19 20 21
18 19 20 21 22 23 24  22 23 24 25 26 27 28  22 23 24 25 26 27 28
25 26 27 28 29 30 31                        29 30 31

       April                  May                   June
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
          1  2  3  4                  1  2      1  2  3  4  5  6
 5  6  7  8  9 10 11   3  4  5  6  7  8  9   7  8  9 10 11 12 13
12 13 14 15 16 17 18  10 11 12 13 14 15 16  14 15 16 17 18 19 20
19 20 21 22 23 24 25  17 18 19 20 21 22 23  21 22 23 24 25 26 27
26 27 28 29 30        24 25 26 27 28 29 30  28 29 30
                      31

        July                 August              September
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
          1  2  3  4                     1         1  2  3  4  5
 5  6  7  8  9 10 11   2  3  4  5  6  7  8   6  7  8  9 10 11 12
12 13 14 15 16 17 18   9 10 11 12 13 14 15  13 14 15 16 17 18 19
19 20 21 22 23 24 25  16 17 18 19 20 21 22  20 21 22 23 24 25 26
26 27 28 29 30 31     23 24 25 26 27 28 29  27 28 29 30
                      30 31

      October               November              December
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
             1  2  3   1  2  3  4  5  6  7         1  2  3  4  5
 4  5  6  7  8  9 10   8  9 10 11 12 13 14   6  7  8  9 10 11 12
11 12 13 14 15 16 17  15 16 17 18 19 20 21  13 14 15 16 17 18 19
18 19 20 21 22 23 24  22 23 24 25 26 27 28  20 21 22 23 24 25 26
25 26 27 28 29 30 31  29 30                 27 28 29 30 31

'''
