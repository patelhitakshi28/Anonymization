from src.anonymizer import anonymize_message

def main():
    # Example user message
    user_message = "Hello, my name is John Doe and I live in New York."
    print("Original Message:", user_message)

    # Anonymize the message
    anonymized_message = anonymize_message(user_message)
    print("Anonymized Message:", anonymized_message)

if __name__ == "__main__":
    main()