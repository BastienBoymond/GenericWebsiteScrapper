import sys
from scrapper import Scrapper

if (sys.argv[1]):
    scrapper = Scrapper(sys.argv[1])
    print(scrapper.getAllItemIntoSomethingByClass('footer-desc'));