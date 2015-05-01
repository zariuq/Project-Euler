# Euler -4

def is_palindrome ( num ):
    string = map(int, str(num))
    if string == string[::-1]:
        return True
    else:
        return False
    
print is_palindrome(121)
print is_palindrome(123)    

palindromes = []    

for i in range(97500,99999)[::-1]:
    for j in range(i,99999)[::-1]:
        mult = i * j
        if is_palindrome(mult):
            palindromes.append( (mult,i,j) )

palindromes.sort(reverse=True)


print palindromes














