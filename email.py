def extract_name_from_email(email):
    # Split the email using "@" as the delimiter
    parts = email.split("@")
    
    # If the email has the correct format, extract the name part
    if len(parts) == 2:
        name_part = parts[0]
        return name_part
    else:
        return None

# Get email input from the user
user_email = input("Enter your email: ")

# Extract and print the name part of the email
name_part = extract_name_from_email(user_email)

if name_part:
    print("Name part of the email:", name_part)
else:
    print("Invalid email format. Please enter a valid email.")      