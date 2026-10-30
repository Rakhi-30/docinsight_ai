import re

def extract_info(text):

    dates = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text)

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    phones = re.findall(
        r'\b\d{10}\b',
        text
    )

    return {
        "Dates": dates,
        "Emails": emails,
        "Phone Numbers": phones
    }