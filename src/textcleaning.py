
import re

'''
text_clean_last_spaces: this function deletes las word spaces in case there is some
'''
def text_clean_last_spaces(text):
    x = re.search(r'\s+\Z', text)
    if x:
        return text[:x.start()]
    else:
        return text


def coma_clean(text):
    if "," in text:
        return text.replace(",","")
    elif "s" in text:
        return text.replace("s","")
    else:
        return text


def fatal(row):
    if len(row) == 2:
        if row[0] == "Y" or row[0] == "N" or row[0] == "y" or row[0] == "n":
            return row[0]
        elif row [0] == None and row[1] == None :
            return 'Nan'
        else:
            if row[0] == "" and row[1].lower().find("fatal"):
                return "Y"
            else:
                return "N"
    else:
        return 'Nan'

def month(month):
    if month != None:
        if len(month) == 3:
            return month
        elif len(month) > 3:
            return month[:3]
    else:
        return 0

def country(country):
    country = str(country)
    if re.findall(r"(.*)SRI LANKA(.*)" , country):
        return "SRY LANKA"
    elif re.findall(r"(.*)UNITED ARAB EMIRATES(.*)", country):
        return "UNITED ARAB EMIRATES"
    elif re.findall(r"(.*)Fiji(.*)" , country):
        return "FIJI"
    elif re.findall(r"(.*)British(.*)" , country):
        return "UNITED KINGDOM"
    elif re.findall(r"(.*)BRITISH(.*)" , country):
        return "UNITED KINGDOM"
    elif re.findall(r"(.*)BRITAIN(.*)" , country):
        return "UNITED KINGDOM"
    elif re.findall(r"(.*)MEXICO(.*)" , country):
        return "MEXICO"
    elif re.findall(r"(.*)Sierra Leone(.*)" , country):
        return "SIERRA LEONE"
    elif re.findall(r"(.*)Seychelles(.*)" , country):
        return "SEYCHELLES"
    else:
        return country