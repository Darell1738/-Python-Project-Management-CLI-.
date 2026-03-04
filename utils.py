import uuid
from datetime import datetime

def generate_id():
    """Generate a unique ID"""
    return str(uuid.uuid4())[:8]

def format_date(date_string):
    """Format ISO date string to readable format"""
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%Y-%m-%d %H:%M")
    except:
        return "Unknown date"

def validate_input(prompt, required=True):
    """Validate user input"""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required. Please enter a value.")

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*50)
    print(f" {text}")
    print("="*50)

def print_success(text):
    """Print success message"""
    print(f"✓ {text}")

def print_error(text):
    """Print error message"""
    print(f"✗ {text}")