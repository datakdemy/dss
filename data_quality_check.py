# import de librairie
import re

# fonction de validation d'emails
def validate_emails(data):
    """
    Cette fonction validate_emails prend une liste de chaînes (les adresses e-mail)
    comme entrée, puis utilise une expression régulière (email_pattern) pour valider des adresse e-mail
    Les adresses e-mail valides sont stockées dans la liste valid_emails, tandis que les adresses e-mail 
    invalides sont stockées dans la liste invalid_emails"""
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid_emails = []
    invalid_emails = []

    for email in data:
        if re.match(email_pattern, email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    return valid_emails, invalid_emails