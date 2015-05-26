
lychrel :: Int -> Integer -> Bool
lychrel i v 
    | i >= 50   = s /= rs
    | i == 1    = lychrel (i+1) ((sum.map read) [s,rs]) 
    | otherwise = if s == rs
                    then False
                    else lychrel (i+1) ((sum.map read) [s,rs]) 
    where s  = show v
          rs = reverse s

answer = foldl (\c v -> if lychrel 1 v then c+1 else c) 0 [1..10000]
-- Or I could filter and add the sum.. same?

-- numbers should be removed after being checked in a chain... we're double checking a lot!
