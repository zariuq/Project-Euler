import System.IO
import qualified Data.Map.Strict as Map

type Pmap = Map.Map String String

main = do
    contents <- readFile "primes2.txt"
    let nono = ['0','2','4','6','8']
    let primes = filter (\x -> length x < 7 && (not $ any (flip elem x) nono) ) $ words contents
    let pmap = Map.fromList $ map (\x -> (x,x)) primes
    let numCircularPrimes = Map.foldl (\ac el -> ac + (snd $ isCircular pmap el)) 0 pmap
    print (numCircularPrimes + 1) -- 2 is removed...

isCircular :: Pmap -> String -> (Pmap, Int)
isCircular pm xs = (pm,if tv then 1 else 0)
    where rs = rotate xs
          tv = and $ map (flip Map.member pm) rs

rotate :: String -> [String]
rotate xs = rotations xs (length xs)

rotations :: String -> Int -> [String] 
rotations xs 1 = [xs]
rotations xs n = [xs] ++ (rotations r (n-1))
    where r = (tail xs) ++ [head xs]
