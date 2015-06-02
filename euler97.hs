ten n = (reverse . take 10 . reverse . show) n
ans = ten $ 28433 * 2^7830457 + 1

-- I was expecting to have to do some weird trick to only calculate the last 10 digits...

--Hmm, 

ans = mod (28433 * 2^7830457 + 1) (10^10)

-- Is much faster -_-
-- I've got to stop using strings to manipulate numbers then... D'=


-- Can I assume Haskell's exponentiation is efficient?
