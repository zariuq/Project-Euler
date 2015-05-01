import System.IO
import Control.Exception -- for exception raising or error handling
import Data.Char
import Data.List
import Control.Monad

evenOp :: Int -> Int
evenOp n = div n 2

oddOp :: Int -> Int
oddOp n = 3*n + 1

appOp :: Int -> Int
appOp n
    | even n    = evenOp n
    | otherwise = oddOp n

collatz :: [Int] -> Int -> [Int]
collatz xs 1 = reverse (1:xs)
collatz xs n = collatz (n:xs) (appOp n)

maxCollatz :: Int -> (Int,Int)
maxCollatz n
    | n > 1 = foldl (\m c -> let cl = length (collatz [] c) in if cl > snd m  then (c,cl) else m) (0,0) [1..n]
    | otherwise = (1,1)

-- Faster would be to store the length of [all numbers < n], and use those as soon as we reach it...
-- Space makes for shorter time! >:D
-- Yes, I should memoize it... using Maps (dictionaries...)
