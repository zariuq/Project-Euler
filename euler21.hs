import System.IO
import Data.Char
import Data.List
import Control.Monad
import qualified Data.Map.Strict as Map

type IntMap = Map.Map Int Int 

dCalc :: Int -> Int
--dCalc :: (RealFrac a, Integral a, Floating a) => a -> a
dCalc i = if filter (\x -> x^2 == i) bnd /= [] then sum ((init x) ++ (tail $ map (div i) x)) else sum (x ++ (tail $ map (div i) x))
    where x   = filter (\x -> mod i x == 0) bnd
          bnd = takeWhile (\x -> x^2 <= i) [1..i]

dSums :: IntMap
dSums = Map.fromList [(1,0)]

getSum :: Int -> IntMap -> Int
getSum i ds = case Map.lookup i ds of
               Just n -> n
               Nothing -> 0
               
addTo :: Int -> IntMap -> IntMap
addTo i ds = Map.insert i (dCalc i) ds    

getSums :: Int -> IntMap -> IntMap
getSums i ds = foldl (\s i -> addTo i s) dSums [1..i]

sumTo = 10000 - 1
sums = getSums sumTo dSums

answer = foldl (\s i -> let t = getSum i sums in if i < t && i == getSum t sums && i /= t then s+i+t else s ) 0 [1..sumTo]

-- I forgot to make sure i/=t !!

