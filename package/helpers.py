from package.read_json import question_db


def ocr(exam_code, results, num_questions):
    """This function calculates the marks for the exam
    
    Arguments:
        exam_code {[str]} -- [The code of the exam to be marked]
        results {[dict]} -- [The answers of the questions answers by user]
        results {[int]} -- [The total number of the questions in an exam]

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
                        else:
                            continue  # continue to the next iteration

    print('Answers', answers)
    correct_answers = [1 for ans in answers if ans is True]

    total_marks = (len(correct_answers) / num_questions) * 100

    rounded_marks = round(total_marks, 2)

    return f'You had {rounded_marks} out of 100'
