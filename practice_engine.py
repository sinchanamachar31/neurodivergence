from tutor_brain import generate_lesson
from question_generator import generate_question
from interactive_tutor import tutor_interaction


def run_learning_cycle(concept, profile, student_answer):

    explanation = generate_lesson(concept, profile)

    question = generate_question(concept)

    evaluation = tutor_interaction(concept, student_answer)

    return {
        "explanation": explanation,
        "question": question,
        "evaluation": evaluation
    }