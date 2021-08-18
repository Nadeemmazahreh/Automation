import re 

def extract_emails(file):
    with open(file,'r') as file:
        text = file.read()
        result = re.findall("([a-zA-z-0-9+.-_]+@[a-zA-z-1-9+.-_]+\.[a-zA-z-0-9]+)", text)
    
    with open('emails.txt', 'w') as emailsFile:
        for email in result:
            emailsFile.write('%s\n' % email)

def extract_phone_numbers(file):
    with open(file,'r') as file:
        numbers = file.read()
        result = re.findall("([0-9]+-[0-9]+-[0-9]+)", numbers)
    
    with open('phone_numbers.txt', 'w') as PhoneNumbers:
        for number in result:
            PhoneNumbers.write('%s\n' % number)

if __name__ == '__main__':
    extract_emails('./automation/potential_contacts.txt')
    extract_phone_numbers('./automation/potential_contacts.txt')