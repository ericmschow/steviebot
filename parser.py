from bs4 import BeautifulSoup, SoupStrainer, NavigableString
import io, os

onlyLyricsDiv = SoupStrainer(class_='lyrics')

def tagFilter(tag):
    return tag != 'a' and tag != 'i'

def classFilter(class_):
    return class_ != 'thanks' and class_ != 'note'

for filename in os.listdir('lyrics'):
    with open('./lyrics/' + filename) as fh:
        soup = BeautifulSoup(fh, 'html.parser', parse_only=onlyLyricsDiv)

    lines = soup.find_all(attrs={"class": classFilter, "tag": tagFilter})

    content = []
    for line in lines:
        content = ''.join(child for child in line.parent.children
                        if isinstance(child, NavigableString)
                    ).strip()

    splitLines = filter(lambda x: x != '', content.split('\n'))
    delimitedLines = []
    for line in splitLines:
        delimitedLines.append(line + '\n')

    f = open('parsedlyrics.csv', 'a', encoding='utf-8')
    f.writelines(delimitedLines)
    f.close()

    cache = open('cache.txt', 'w', encoding='utf-8')
    cache.write(str(len(delimitedLines)))
    cache.close()