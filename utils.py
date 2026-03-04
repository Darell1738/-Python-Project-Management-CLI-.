import uuid
from datetime import datetime

def generate_id():
    return str(uuid.uuid4())[:8]

def format_date(date_string):
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%Y-%m-%d %H:%M")
    except:
        return "Unknown date"

def validate_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required. Please enter a value.")

def print_header(text):
    print("\n" + "="*50)
    print(f" {text}")
    print("="*50)

def print_success(text):
    print(f"✓ {text}")

def print_error(text):
    print(f"✗ {text}")