# pycld3
# https://pypi.org/project/pycld3/

import cld3



def get_lange_cld(text, get_prob=False):
    output = cld3.get_language(text)
    lang=output.language
    
    if get_prob == False:
        return lang
    else:
        return lang, output.probability
    
if __name__ == "__main__":
    text = input("Text to be classified.")
    print(f"Estimated Lanugage: {get_lange_cld(text)}")

