"""Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name.
For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo"."""

def generate_signature(name, title, company):

    first_letter = name[0].upper()

    if 'A' <= first_letter <= 'I':
        prefix = ">>"
    elif 'J' <= first_letter <= 'R':
        prefix = "--"
    elif 'S' <= first_letter <= 'Z':
        prefix = "::"

    signature = f"{prefix}{name}, {title} at {company}"
    print(signature)

    return signature

signature = generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") # "--Quinn Waverly, Founder and CEO at TechCo".
generate_signature("Alice Reed", "Engineer", "TechCo") # ">>Alice Reed, Engineer at TechCo".
generate_signature("Tina Vaughn", "Developer", "example.com") # "::Tina Vaughn, Developer at example.com".
generate_signature("B. B.", "Product Tester", "AcmeCorp") # ">>B. B., Product Tester at AcmeCorp".
generate_signature("windstorm", "Cloud Architect", "Atmospheronics") # "::windstorm, Cloud Architect at Atmospheronics".