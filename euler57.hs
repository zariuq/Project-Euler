import Data.Ratio

iter :: (Num a, Fractional a1, Eq a) => a -> a1
iter 0 = 1
iter n = 1 + 1 / (1 + iter (n-1))

digcompare :: (Show b, Num a, Integral b) => Ratio b -> a
digcompare r = if num > den then 1 else 0
    where num = (length . show . numerator) r
          den = (length . show . denominator) r

answer = sum [digcompare (iter n :: Rational) | n <- [1..1000]]

-- It's probably better to put the calc is iter... this has LOOOOTS of waste :p
