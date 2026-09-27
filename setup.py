from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'
def get_requirenments(file_path:str)->List[str]:
  requirenments = []
  with open(file_path) as f :
    requirenments = f.readlines()
    requirenments = [r.replace("\n","") for r in requirenments]

    if hypen_e_dot in requirenments:
      requirenments.remove(hypen_e_dot)
  return requirenments


setup(
  name='ML_Project',
  version='0.0.1',
  author='Balaji',
  author_email='balajipalani707@gmail.com',
  packages=find_packages(),
  install_requires=get_requirenments('requirenments.txt')
)
