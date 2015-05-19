import Sieve

-- Damn, this version of the Sieve is so elegant, and provides you with a list of all primes and nonprimes!

twicesquare = [2*(n^2) | n <- [1..]]

belem :: [Integer] -> Integer -> Bool
belem xs e = elem e (takeWhile (<e+1) xs)

goldbach :: Integer -> Bool
goldbach n = any (belem twicesquare) (map (n-) $ takeWhile (<n) primes)

main :: IO ()
main = do
  print $ head $ filter (not.goldbach) nonprimes
  
  
