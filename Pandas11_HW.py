# Problem 1 : Replace Employee ID with the Unique Identifier


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, on = ['id'], how ='left')
    return df[['unique_id','name']]




# Problem 2 : Students and Examination


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = subjects.merge(students, how ='cross')
    examinations = examinations.groupby(['subject_name','student_id']).agg(attended_exams= ('subject_name','count')).reset_index()
    df1 = df.merge(examinations, how= 'left', left_on = ['student_id','subject_name'], right_on = ['student_id','subject_name'])
    df1['attended_exams']= df1['attended_exams'].fillna(0)
    return df1.sort_values(['student_id','subject_name'])[['student_id','student_name','subject_name','attended_exams']]