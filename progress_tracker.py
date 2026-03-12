student_progress = {}


def update_progress(student_id, concept, score):

    if student_id not in student_progress:
        student_progress[student_id] = []

    student_progress[student_id].append({
        "concept": concept,
        "score": score
    })

    return student_progress[student_id]


def learning_summary(student_id):

    if student_id not in student_progress:
        return {"message": "No learning data found"}

    records = student_progress[student_id]

    total_score = sum(r["score"] for r in records)
    average = total_score / len(records)

    weak_topics = [r["concept"] for r in records if r["score"] < 60]

    return {
        "concepts_learned": [r["concept"] for r in records],
        "average_score": average,
        "weak_topics": weak_topics
    }


def recommend_learning(student_id):

    if student_id not in student_progress:
        return {"message": "No learning data found"}

    weak_topics = []

    for record in student_progress[student_id]:
        if record["score"] < 60:
            weak_topics.append(record["concept"])

    if weak_topics:
        return {
            "recommendation": "Revise these topics",
            "topics": weak_topics
        }

    return {
        "recommendation": "Student performing well",
        "topics": []
    }