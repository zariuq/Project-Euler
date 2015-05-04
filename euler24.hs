import Data.List

f :: Int -> Int
f 0 = 1
f i = i * f (i-1)

mult :: Int -> [Int]
mult i = [n * i | n <- [1..]]

toP = [0..9] ::[Int]

bigN = 1000000 :: Int

next lim prenum n = takeWhile (\x -> x + prenum < lim) (mult $ f n)

nextIter :: Int -> Int -> [Int] -> [ [Int] ]
nextIter _ _ [] = []
nextIter lim su (x:xs)
    | l /= []   = [l] ++ ( nextIter lim (su + last l) xs)
    | otherwise = [[0]]
    where l = next lim su x
    
digN = (map length $ nextIter bigN 0 [9,8..1]) ++ [0]

apply :: [Int] -> [Int] -> [Int]
apply [] _    = []
apply _ []    = []
apply digs li = [m] ++ (apply (tail digs) (delete m li))
    where k = head digs
          m = li !! k

answer = apply digN toP  

-- Works, but there are many fringe cases not dealt with.  
-- The method is far, far faster if you work out kinks though.
-- But the slow, brute-force way is simple and works in all cases =D...

-- Calls empty list. Above method seems better.
milP :: Int -> Int -> [Int] -> [Int]
milP _ _ (x:[])     = [x]
milP n prenum left
    | n <= prenum = left
    | otherwise   = [left !! nu] ++ milP n (prenum + last fl) (delete nu left)
    where d  = length left
          fl = takeWhile (\x -> x + prenum < n) (mult $ f (d-1))
          nu = length fl
        


{-
    So f 9 = 362880, so the millionth lexicographic permutation of [0..9] starts with 2
    And d1 (f 9) * 3 + d2 (f 8) * 7 + d3 (f 7) * 7 + d4 (f 6) * 3 + d5 (f 5) * 6 + d6 (f 4) * 2 + d7 (f 3) * 3
    is the first > million
    (And you revert one multiple when calculating the next!)
    
    2783905416

p = permutations "0123456789"
ps = sortBy compare p
answer = ps !! (1000000 -1)
answer = "2783915460"

-__- The problem with doing it by hand instead of coding it in: you mess up.
Well, I should code my "by hand" method =]

-}

