

# ⁡⁢⁣⁣password validation

try:
    password = input('Enter your Password: ')
    
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    length = len(password) >= 8
    uppercase = any(ch.isupper() for ch in password)
    lowercase = any(ch.islower() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special = any(ch in "!@#$%^&*()_+-=<>?/{}[]|" for ch in password)

    if length and uppercase and lowercase and digit and special:
        print('✅ Password is Strong!')
    else:
        print('❌ Weak Password!')
        if(not length):
            print('- Length should be at least 8 characters')
        if(not uppercase):
            print('- Must include at least one uppercase letter')
        if(not lowercase):
            print('- Must include at least one lowercase letter')
        if(not digit):
            print('- Must include at least one number')
        if(not special):
            print('- Must include at least one special character')

except TypeError as te:
    print(f'⚠️ Type Error: {te}')

except ValueError as ve:
    print(f'⚠️ Value Error: {ve}')

except Exception as e:
    print(f'⚠️ Unexpected Error: {e}')

finally:
    print("✅ Password validation complete.")
