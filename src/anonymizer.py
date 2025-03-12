import re
from .utils import generate_pseudonym  # Import the function from utils.py

def anonymize_message(message):
    """
    Anonymize PII (e.g., names) in the input message.
    Args:
        message (str): The input text containing PII.
    Returns:
        str: The anonymized text.
    """
    # Regex to detect names (capitalized words with at least 2 letters)
    name_pattern = r'\b[A-Z][a-z]+\b(?: [A-Z][a-z]+)*\b'

    # Find all matches of names in the message
    names = re.findall(name_pattern, message)

    # Replace each name with a pseudonym
    for name in names:
        # Skip common place names or non-name capitalized words
        if name.lower() in {"new york", "los angeles", "san francisco"}:  # Add more as needed
            continue
        pseudonym = generate_pseudonym()  # Use the imported function
        message = message.replace(name, pseudonym)

    return message