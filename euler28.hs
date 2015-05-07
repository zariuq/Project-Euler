{-
49 - 6 - 6 - 6 -
25 - 4 - 4 - 4 -
9 - 2 - 2 - 2 - 
1

So, the four corners are (n-1) apart, and then on to the lower square.
Wow, n^2 - 4*(n-1) = (n-2)^2  (n^2 - 4n + 4... yep)

Thank Haskell for preventing me from brute-forcing it due to filling an array seeming a pain :p

73 74 75 76 77 78 79 80 81
72 43 44 45 46 47 48 49 50
71 42 21 22 23 24 25 26 51
70 41 20  7  8  9 10 27 52
69 40 19  6  1  2 11 28 53
68 39 18  5  4  3 12 29 54
67 38 17 16 15 14 13 30 55
66 37 36 35 34 33 32 31 56
65 64 63 62 61 60 59 58 57
-}


cornerSum :: Int -> Int
cornerSum 1 = 1
cornerSum n
    | even n    = -1
    | otherwise = s*4 - (n-1)*6 + cornerSum (n - 2)
    where s = n^2 
