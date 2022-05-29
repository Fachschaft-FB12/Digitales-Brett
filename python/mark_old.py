from glob import glob
import re
import datetime

def markOld(file):
    with open(file, mode='r+', encoding='utf-8') as f:
        old = ''
        for line in f.readlines():
            if line[:6] == 'title:':
                if line[12] == '\"':
                    line = line[:13] + '- ALT - ' + line[13:]
                else:
                    line = line[:12] + '- ALT - ' + line[12:]
            old += line
        f.seek(0)
        f.write(old)

for file in glob('.././*/*.md'):
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            if line[:6] == 'until:':
                date = re.sub('\s+', '', line[6:])
                if len(date) == 10:
                    t = datetime.date(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:]))
                    if t < datetime.date.today():
                        markOld(file)
                        break