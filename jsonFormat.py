def json_format():
  json_file={
   "jobs": [
    {"role": "Frontend Developer", "match": 85, "link": "naukri.com"},
    {"role": "UI Engineer", "match": 78, "link": "naukri.com"}
  ],
   "mcqs": [
    {
      "question": "What does CSS stand for?",
      "options": ["A) Computer Style Sheets", "B)..","C)..","D).."],
      "correct": "C) Cascading Style Sheets"
    }
  ],
  "skill_gaps": [
    {
      "skill": "React State Management",
      "resources": ["Official Docs", "Redux Tutorial"]
    }
     ]
   }
  return json_file