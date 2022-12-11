# use this to import repo's data to your local mongo db
import json
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
  
f = open('./data/mitosis/db.json')

data = json.load(f)

for i in data:
    print(i)