from read_json import question_db


def ocr(exam_code, results):
    """This function calculates the marks for the exam
    
    Arguments:
        exam_code {[str]} -- [The code of the exam to be marked]
        results {[dict]} -- [The answers of the questions answere by user]
    
    Returns:
        [str] -- [The marks the user had in the exam]
    """
    questionDB = question_db()

    answers = []

    for exam in questionDB:
        if exam['examCode'] == exam_code:
            for results_keys, question in zip(results.keys(), exam['questions']):
                if question['_id'] == results_keys:
                    for option in question['alternatives']:
                        if option['_id'] == results[str(results_keys)]:
                            answers.append(option['isCorrect'])

    correct_answers = [1 for ans in answers if ans == True]

    total_marks = len(correct_answers) / len(answers) * 100

    rounded_marks = round(total_marks, 2)

    return f'You had {rounded_marks} out of 100.'


exam_code = "5e7bf109e8554c0de33bce2d"

results = {
    "Q1":"5e7bf109e8554c0de33bcf2d", "Q2":"5e7bf109e8554c0de33bcf2b", "Q3":"5e7bf109e8554c0de33bcf2d",
    "Q4":"5e7bf109e8554c0de33bcf2d", "Q5":"5e7bf109e8554c0de33bcf2c", "Q6":"5e7bf109e8554c0de33bcf2d",
    "Q7":"5e7bf109e8554c0de33bcf2d", "Q8":"5e7bf109e8554c0de33bcf2d", "Q9":"5e7bf109e8554c0de33bcf2d", 
    "Q10":"5e7bf109e8554c0de33bcf2d","Q11":"5e7bf109e8554c0de33bcf2b", "Q12":"5e7bf109e8554c0de33bcf2d", 
    "Q13":"5e7bf109e8554c0de33bcf2d","Q14":"5e7bf109e8554c0de33bcf2d", "Q15":"5e7bf109e8554c0de33bcf2d",
    "Q16":"5e7bf109e8554c0de33bcf2d","Q17":"5e7bf109e8554c0de33bcf2d", "Q18":"5e7bf109e8554c0de33bcf2d",
    "Q19":"5e7bf109e8554c0de33bcf2d","Q20":"5e7bf109e8554c0de33bcf2d", "Q21":"5e7bf109e8554c0de33bcf2d"
}
#print(ocr(exam_code=exam_code, results=results))

#for item in questionDB:
    #if item['examCode'] == exam_code:
       #total_questions = len(item['questions'])      

#question_in_range = list(range(1, total_questions+1))
