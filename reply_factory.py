
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id):

    if user_answer.strip():
        user_answers_list[current_question_index] = user_answer.strip().lower()
    else:

        raise ValueError("Invalid answer. Please provide a valid response.")
    '''
    Validates and stores the answer for the current question to session.
    '''
    


def get_next_question(current_question_id):

    if current_question_index < len(all_questions):
        return all_questions[current_question_index]
    else:
        # If the current_question_index exceeds the total number of questions,
        # return None to indicate that the quiz is finished.
        return None
    '''
    Fetches the next question from the PYTHON_QUESTION_LIST based on the current_question_id.
    '''

    


def generate_final_response(session):

    total_questions = len(all_questions)
    correct_answers = 0

    for i in range(total_questions):
        correct_answer = all_questions[i]['correct_answer'].strip().lower()
        user_answer = user_answers_list[i]

        if user_answer == correct_answer:
            correct_answers += 1

    score_percentage = (correct_answers / total_questions) * 100
    response = f"You've completed the quiz! Your score is {score_percentage:.2f}%."
    return response
    '''
    Creates a final result message including a score based on the answers
    by the user for questions in the PYTHON_QUESTION_LIST.
    '''

    
