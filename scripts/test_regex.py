import re

content = r"""
Here are some links:
\[Ibis Paint](../catalog/apps/ibis-paint.md) ]
\[Kleki](../catalog/apps/kleki.md) ] 
[Normal Link](../normal.md)
[Another](url)   ]
"""

custom_link_pattern = re.compile(r'(\\?)\[(.*?)\]\((.*?)\)(\s*\]?)')

def replace_link(match):
    prefix = match.group(1)
    text = match.group(2)
    raw_link = match.group(3)
    suffix = match.group(4)

    title = text.upper() # simulate a title change
    
    is_malformed = (prefix == '\\') or (']' in suffix)
    
    if is_malformed or title != text:
        if ']' in suffix:
            clean_suffix = ""
        else:
            clean_suffix = suffix
        return f"[{title}]({raw_link}){clean_suffix}"
    
    return match.group(0)

print(custom_link_pattern.sub(replace_link, content))
