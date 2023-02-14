current_version = '1.0.4'
new_version = '1.0.5'

files = [r'README.md', r'setup.py', r'build.bat', r'deploy.bat']

for file in files:
    script_str = open(file).read()
    script_str = script_str.replace(current_version, new_version)
    open(file, 'w').write(script_str)
