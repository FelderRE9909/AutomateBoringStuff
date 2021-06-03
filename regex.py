# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3.8.10 64-bit ('3.8.10')
#     name: python381064bit3810c8a5b6e912fa44d69267ddcb2af5cba8
# ---

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

emailregex = re.compile(r'(\w)+@(\w)+(\.com|\.net|\.org)')
mo2 = emailregex.search('emails%jh.net r@gmail.com n@email.com')
mo2.group()


