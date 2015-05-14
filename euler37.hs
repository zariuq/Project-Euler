
-- Trunctable Primes -- 

import System.IO
import qualified Data.Map.Strict as Map

type Pmap = Map.Map String String

main = do
    contents <- readFile "primes2.txt"
    let nono = ['0','4','6','8'] -- as before, we can't truncate into any even number!
    let primes = filter (\x -> length x > 1 && (not $ any (flip elem x) nono) ) $ words contents
    let pmap = Map.fromList $ map (\x -> (x,x)) primes
    let numTrunctablePrimes = Map.foldl (\ac el -> ac + if isTrunctable pmap el then (read el :: Int) else 0) 0 pmap
    print numTrunctablePrimes
    
isTrunctable :: Pmap -> String -> Bool
isTrunctable pm (ns:[]) = False
isTrunctable pm ns = rightTrunc pm ns && leftTrunc pm ns
          
rightTrunc :: Pmap -> String -> Bool
rightTrunc pm (ns:[]) = elem ns pr
    where pr = ['2','3','5','7']
rightTrunc pm      ns = Map.member ns pm && rightTrunc pm (init ns)

leftTrunc :: Pmap -> String -> Bool
leftTrunc pm (ns:[]) = elem ns pr
    where pr = ['2','3','5','7']
leftTrunc pm      ns = Map.member ns pm && leftTrunc pm (tail ns)
          
