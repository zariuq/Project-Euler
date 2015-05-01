import System.IO
import Control.Exception -- for exception raising or error handling
import Data.Char
import Data.List
import Control.Monad
import qualified Data.Map.Strict as Map

--numdic :: Map Int String
numDic = Map.fromList [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five"),(6,"six"),(7,"seven"),(8,"eight")
                      ,(9,"nine"),(10,"ten"),(11,"eleven"),(12,"twelve"),(13,"thirteen"),(14,"fourteen")
                      ,(15,"fifteen"),(16,"sixteen"),(17,"seventeen"),(18,"eighteen"),(19,"nineteen"),(20,"twenty")
                      ,(30,"thirty"),(40,"forty"),(50,"fifty"),(60,"sixty"),(70,"seventy"),(80,"eighty")
                      ,(90,"ninety"),(100,"hundred"),(1000,"onethousand")]

-- Map.lookup 5 numDic

getNum :: Int -> String
getNum i = case Map.lookup i numDic of
               Just n -> n
               Nothing -> "Fuck you, too!"

makeString :: Int -> String
makeString i 
    | i < 20    = getNum i
    | i < 100   = let tens = (div i 10)*10 
                  in (getNum tens) ++ if tens == i 
                      then "" 
                      else getNum (i - tens)
    | i < 1000  = let hundreds = (div i 100) in
                  let remainder = i - hundreds*100
                  in (getNum hundreds) ++ (getNum 100) ++ if remainder == 0
                      then ""
                      else "and" ++ makeString remainder
    | i == 1000 = getNum i
    | otherwise = "Fuck You!"

count :: Int -> Int
count n = sum $ map length (map makeString [1..n])

