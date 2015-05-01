import System.IO
import Control.Exception -- for exception raising or error handling
import Data.Char
import Data.List
import Control.Monad -- Note: Control, not Data

-- slist = map (\x -> read [x]::Int) series
    -- not Int, Integer.  Int is too small

-- Okay, I need to look at how to read in from another file

main = do
    contents <- readFile "euler13sum.txt"
    let t = lines contents
    let g = map (\x -> read x :: Integer) t
    let sumOf = sum g
    
    print sumOf
    --let nums = fmap (liftM (\x -> read x :: Integer)) (lines contents)
    --let sum = liftM sum nums 
    -- .____. Two liftMs and an fmap to get my IO [Integer].  Can't touch the actual IO content -.-;
    -- O_O WTF!!!  When testing, contents was IO String, not String!  
    --O.o  Oh well, at least I got some odd practice...
