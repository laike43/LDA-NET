
import os

def em(dict):
    if ('@enron' in dict['From'])or ('@enron' in dict['To']):
        name =  dict['X-FileName'].split()[0].split('.')[0] +'.'+ dict['X-Origin'].split('-')[0]
        lastname = dict['X-Origin'].split('-')[0].lower().strip()
        firstname =  dict['X-FileName'].split()[0].split('.')[0].lower().strip()
        print(name,firstname,lastname)
        
        if lastname in dict['From']:
            if '@enron' in dict['From']:
                emailaddress =  dict['From']
            return name.lower(), firstname, lastname, emailaddress
        
        elif (lastname in dict['To']):
            tmp = dict['To'].split(',')
            for i in tmp:
                if lastname in i:
                    if '@enron' in i:
                        emailaddress = i.strip()

                    return name.lower(),firstname,lastname,emailaddress
        else:
            return 0
    else:
        return 0
def ernorneibu(dict):
    if '@enron' in dict['From']:
        if '@enron' in dict['To']:
            return 1
        else:
            return 0
    else:
        return 0


if __name__=="__main__":
    pass