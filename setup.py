from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='toto',
      version='0.3.0',
      description="say hi to the world!",
      packages=find_packages(),
      install_requires=requirements,
      scripts=['scripts/toto-say-hi'])