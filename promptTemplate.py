def prompt_format(resume_text,json_file):
  prompt = f"""Analyze this resume(key metrics-skill set,last qualification, current job(if appicable),last job(if appicable), projects, current qualification) and return ans  JSON format with:
    1. jobs: array of 5 job roles with match percentage sites with link (based on current job(if appicable) or last job(if appicable);current qualification or last qualification)
    2. mcqs: 10 technical MCQs with 4 options with moderate level standrad(based on project and skill)
    3. skill_gaps: 5 missing skills with resources (if any skill in trend recommend that type things)
    Resume: {resume_text}
    json format file type structure:{json_file}"""
  return prompt