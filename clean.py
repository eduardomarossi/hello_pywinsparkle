import pathlib, os, shutil
[p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
[p.unlink() for p in pathlib.Path('installer').rglob('*.exe')]
[p.unlink() for p in pathlib.Path('.').rglob('*.spec')]
[p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]
if os.path.exists('dist'): shutil.rmtree('dist')
if os.path.exists('build'): shutil.rmtree('build')