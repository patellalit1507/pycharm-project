import re
def EmailValidation(email):
    #regex_email=re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$',re.IGNORECASE)
    regex_email=re.compile(r"""
                            ([a-z0-9_\.-]+)
                            @
                            ([0-9a-z\.-]+)
                            \.
                            ([a-z\.]{2,6})$
                            """
                           ,re.VERBOSE|re.IGNORECASE)
    res=regex_email.fullmatch(email)
    if res:
        print('validate')
    else:
        print('Not valid')

EmailValidation("expectopatronum@gmail.com")
