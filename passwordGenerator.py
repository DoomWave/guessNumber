import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        

        return False
    

    def contains_symbols(password: str) -> bool:
        for char in password:
            if char in string.punctuation:
                return True
        
        return False
    
print(string.punctuation)
