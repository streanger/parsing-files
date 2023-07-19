from pathlib import Path
import pandas as pd

"""
useful:
    https://stackoverflow.com/questions/73632326/how-to-convert-this-time-format-fri-apr-01-2022-000100-gmt0100-to-utc-gmt

example date formats:
    Fri Apr 01 2022 00:01:00 GMT+0100
    "%a %b %d %Y %H:%M:%S %Z%z"

    Tue, 18 Jul 2023 00:00:00 GMT
    "%a, %d %b %Y %H:%M:%S %Z"
"""

lines = Path('stats.txt').read_text().splitlines()
parsed = []
for line in lines[1:]:
    (first, *middle, last) = line.split()
    parsed.append((first, ' '.join(middle), last))
    
header = ['first', 'middle', 'last']
df = pd.DataFrame(parsed)
df.columns = header
df['middle'] = pd.to_datetime(df['middle'], format="%a, %d %b %Y %H:%M:%S %Z")
df.index += 1
df.to_csv('stats.csv')
