import streamlit as st
import os
import json
from resume_processor import analyze_resume

if 'results' not in st.session_state:
    st.session_state.results=None

uploaded_file=st.file_uploader("Upload Resume",type=['pdf','docx'])

if uploaded_file:
    uploaded_path= os.path.join('data/uploads',uploaded_file.name)
    with open(uploaded_path,'wb') as f:
        f.write(uploaded_file.getbuffer())
    if st.button('Analyze'):
        results=analyze_resume(uploaded_path)
        st.session_state.results=results
        with open(f'data/results/{uploaded_file.name}_analysis.json','w') as f:
            json.dump(results,f)


#Dispaly Results
if st.session_state.results:
    st.header("Analysis Results")
 
    #Job recommendations Tab
    with st.expander("Job Recommendation"):
        for job in st.session_state.results['jobs']:
            st.markdown(f"**{job['role']}** ({job['match']}%) ({job['link']})")

    # MCQ Exam Tab
    with st.expander("Skill Assesment Questions"):
        selected_options=[]
        for i,mcq in enumerate(st.session_state.results['mcqs']):
           selected= st.radio(
                f"{i+1}. {mcq['question']}",
                options=mcq['options'],
                key=f"mcq_{i}"
                  )
           if selected:
                   selected_options.append(selected)
           else:
                   selected_options.append("Not Selected")  

        if st.button("Submit Exam"):
            marks=0
            right=0
            for i,j in zip(selected_options,st.session_state.results['mcqs']):
                if i==j['correct']:
                    marks=marks+1
                    right=right+1
            st.markdown(f"**Assesment Results:** Marks={marks}, Right={right}")

    # Skill Gap Analysis
    with st.expander("Skill Developement"):
        for gap in st.session_state.results["skill_gaps"]:
            st.markdown(f"**{gap['skill']}**")
            st.caption(f"Resources: {','.join(gap['resources'])}")