# Chapter 10 Examples

import shutil, os
from pathlib import Path

Desktop = Path('''C:\\Users\\Eric\\Desktop''')
shutil.copy(Desktop / 'eggs.txt', Desktop / 'test')

print(Path.home)