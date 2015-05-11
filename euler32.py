import qualified Data.Set as Set
import Data.Char
import Data.List

digits = map intToDigit [1..9]

panDigital :: String -> Bool
panDigital xs = digits == (sort xs) --and [foldl (\b a -> if a == x || b then True else False) False xs | x <- digits]
-- Wow, sorting is an order of magnitidue faster. I knew there had to be a less wasteful way!


toString :: (Int,Int,Int) -> String
toString (a,b,c) = (show a)++(show b)++(show c)

products = [(a,b,a*b) | a <- [10..99], b <- [100..999], a*b < 10000] ++
           [(a,b,a*b) | a <- [1..9], b <- [1000..9999], a*b < 10000]

pandigprods = filter (\x -> (panDigital . toString) x) products
uniqueprods = Set.elems (Set.fromList (map (\(a,b,c) -> c) pandigprods))
answer = sum uniqueprods
