import wikipediaapi
from pydantic import BaseModel
from typing import List, Optional

class Institution_Details(BaseModel):
  founder : Optional[str] = None
  founded : Optional[str] = None
  branches : Optional[List[str]] = None
  no_of_employees : Optional[int] = None
  summary : Optional[str] = None

def fetch_institution_details(name):
  wiki = wikipediaapi.Wikipedia(
    user_agent = "MyApp/1.0",
    language = "en"
  )
  page = wiki.page(name)
  if not page.exists():
    raise ValueError("Page not found")
  text = page.text
  founder = None
  founded = None
  branches = None
  employees = None
  summary = page.summary[:500]
  for line in text.split("\n"):
    line_lower = line.lower()
    if "founder" in line_lower and founder is None:
      founder = line.split(":")[-1].strip()
    elif "founded" in line_lower and founded is None:
      founded = line.split(":")[-1].strip()
    elif "branch" in line_lower and branches is None:
      branches = [b.strip() for b in line.split(":")[-1].split(",")]
    elif "employees" in line_lower and employees is None:
      try:
        employees = int(line.split(":")[-1].strip().replace(",",""))
      except:
        pass
    return Institution_Details[
      founder = founder,
      founded = founded,
      branches = branches,
      no_of_employess = employees,
      summary = summary
    ]

name = input("Enter institution Name: ")
details = fetch_institution_details(name)
try:
  print("Founder: ", details.founder or "N/A")
  print("Founded: ", details.founded or "N/A")
  print("Branches: ", ",".join(details.branches) or "N/A")
  print("Number of employees: ", details.no_of_employees if details.no_of_employees else "N/A")
  print("Summary: ", details.summary or "N/A")
except Exception as e:
  print("Error : ", e)

