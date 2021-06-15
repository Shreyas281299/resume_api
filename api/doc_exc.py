import docx2txt
import re

def get_info(filePath):
    try:
        all_text = docx2txt.process(filePath)
        email_pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
        email_matches = email_pattern.finditer(all_text)

        phone_pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
        phone_matches = phone_pattern.finditer(all_text)

        emails = []
        phone = []
        for match in email_matches:
            emails.append(match.group(0))            
        for match in phone_matches:
            phone.append(match.group(0))
        return [emails[0],phone[0]]
            
    except:
        return ['Error','Error']
