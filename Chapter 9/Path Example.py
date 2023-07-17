# Path Example 

from pathlib import Path
import os

p = Path('C:/Users/Eric/Desktop')
p.glob('*')
print(list(p.glob('*')))

