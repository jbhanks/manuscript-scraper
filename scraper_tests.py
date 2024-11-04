from sqlalchemy import create_engine
import os

from utils import *
from models import *


# ####



def get_cambridge_sitemap():
    import requests
    import xml.etree.ElementTree as ET

    sitemap_url = 'https://cudl.lib.cam.ac.uk/sitemap.xml'
    response = requests.get(sitemap_url)
    root = ET.fromstring(response.content)

    manuscripts = []
    printed = []
    photos = []
    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        if '/view/MS-' in url.text:
            manuscripts.append(url.text)
        if '/view/PR-' in url.text:
            printed.append(url.text)
        if '/view/PH-' in url.text:
            photos.append(url.text)
    return manuscripts, printed, photos

# Compare with previous list to detect new URLs

'''
>>> len(manuscripts)
40899
'>>> len(printed)
6040
>>> len(photos)
2213
'''

path = '/home/jam/Documents/'
current_os = os.name
if not path:
    path = os.getcwd()
if current_os == 'posix':
    engine = create_engine(f"sqlite:////{path}/foo.db")
elif current_os == 'nt':
    engine = create_engine(f"sqlite:///{path}\foo.db")
