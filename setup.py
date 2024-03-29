from setuptools import setup, find_packages

HYPEN_DOT="-e ."
def get_requirements(file_path):
  with open(file_path) as file:
      req=file.readlines()
      req=[req.replace('\n','') for req in req]
	  
      if HYPEN_DOT in req:
          req.remove(HYPEN_DOT)
      return req


setup( 
	name='GUI EDA', 
	version='0.1', 
	description='Interactive website to do EDA and Train ML models', 
	author='Yash Choudhary', 
	author_email='4yashchoudhary@gmail.com', 
	packages=find_packages(), 
	install_requires=get_requirements("requirements.txt")
) 
