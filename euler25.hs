import Data.List
import Control.Monad

-- Gosh, an infinite list of all Fibonacci numbers is cool =D
fib :: Integer -> Integer -> [Integer]
fib pre pen = [cur]++(fib cur pre) 
    where cur = pre + pen

answer = liftM (+1) (findIndex (\x -> (length $ show x) > 999) ([1,1]++(fib 1 1))) 

-- Surprisingly fast >_>;
-- I did freeze my computer by using ints, which can't go to 1000 digits... -ore baka-




