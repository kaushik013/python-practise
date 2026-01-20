
import re

# what is RegEx
#! Regex (Regular Expression) is a pattern used to search, match, extract, or replace text.


# ser = re.search('cat', 'i have cat')
# print(ser)


text = '''An extratropical Cyclone near Dyclone   Icelan Part Eyclone of a series on Weather Temperate and polar seasons Tropical seasons Storms Precipitation Topics Glossaries icon Weather portal vte In meteorology, a cyclone  is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure '''


pattern = r'[A-Z]+yclone'

matc = re.finditer(pattern, text)

# for i in matc:
#     print(i)


for i in matc:
    print(i.span())
