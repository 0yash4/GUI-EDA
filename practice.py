def get_requirements(file_path):
  with open(file_path) as file:
      req=file.readlines()
      req=[req.replace('\n','') for req in req]

      return req

if __name__=="__main__":
  print(get_requirements("requirements.txt"))