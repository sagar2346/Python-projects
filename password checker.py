def check_password_strength(password):
    strength_score = 0
    
    # Check for length (at least 8 characters)
    if len(password) >= 8:
        strength_score += 1
        
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength_score += 1
        
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength_score += 1
        
    # Check for numbers
    if any(char.isdigit() for char in password):
        strength_score += 1
        
    # Check for special characters
    special_characters = "!@#$%^&*()-_+=<>?"
    if any(char in special_characters for char in password):
        strength_score += 1
        
    # Provide feedback based on the score
    if strength_score == 5:
        return "Strong password"
    elif strength_score >= 3:
        return "Moderate password"
    else:
        return "Weak password"

# Example use
user_password = input("Enter a password: ")
print(check_password_strength(user_password))
