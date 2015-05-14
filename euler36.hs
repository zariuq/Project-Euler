answer = for (10^6-1) 0

for :: Int -> Int -> Int
for n s
    | n < 0     = s
    | otherwise = if isPalindrome n then for (n-2) (s+n) else for (n-2) s
-- only doing odds makes it much faster :D
-- I probably should've constructed the palindromes though >__>;

isPalindrome :: Int -> Bool
isPalindrome i = dec == reverse dec && bin == reverse bin
    where bin = concat $ map show (toBin i)
          dec = show i

-- From stackexchange... as usual >___>;
-- Like, man, I can do it myself, but what if there's a better way or a built in functionality?!
-- removed the "reverse" from toBin, as we don't need that here :>
toBin 0 = [0]
toBin n = helper n

helper 0 = []
helper n = let (q,r) = n `divMod` 2 in r : helper q
