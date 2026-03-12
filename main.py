from fastapi import FastAPI, UploadFile, File, Form, Body
from tutor_brain import generate_lesson
from pdf_reader import extract_text_from_pdf
import tempfile
from behavior_analyzer import detect_learning_mode
from image_reader import extract_text_from_image
from interactive_tutor import tutor_interaction
from question_generator import generate_question
from practice_engine import run_learning_cycle
from diagram_generator import generate_diagram
from flashcard_generator import generate_flashcards
from worksheet_generator import generate_worksheet
from progress_tracker import update_progress,learning_summary,recommend_learning
from study_plan_generator import generate_study_plan
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/adaptive-explain-mode")

async def adaptive_explain_mode(data: dict = Body(...)):

    concept = data.get("concept")
    profile = data.get("profile")

    difficulty = "medium"

    if profile == "ADHD":
        difficulty = "easy"

    elif profile == "Dyslexia":
        difficulty = "easy"

    elif profile == "Exam":
        difficulty = "hard"

    elif profile == "Visual":
        difficulty = "medium"

    explanation = await adaptive_explain(concept, difficulty)

    return {
        "concept": concept,
        "mode": profile,
        "explanation": explanation
    }


@app.post("/study-plan")
async def study_plan(topics: str):

    plan = generate_study_plan(topics)

    return {"plan": plan}


@app.get("/learning-summary")
async def get_learning_summary(student_id: str):

    summary = learning_summary(student_id)

    return summary

@app.get("/learning-recommendation")
async def get_recommendation(student_id: str):

    recommendation = recommend_learning(student_id)

    return recommendation

@app.post("/update-progress")
async def update_student_progress(
    student_id: str,
    concept: str,
    score: int
):

    progress = update_progress(student_id, concept, score)

    return {
        "progress": progress
    }

@app.post("/generate-worksheet")
async def worksheet_api(concept: str):

    sheet = generate_worksheet(concept)

    return {
        "worksheet": sheet
    }

@app.post("/generate-flashcards")
async def flashcards_api(concept: str):

    cards = generate_flashcards(concept)

    return {
        "flashcards": cards
    }

@app.post("/generate-diagram")
async def generate_diagram_api(concept: str):

    diagram = generate_diagram(concept)

    return {
        "diagram": diagram
    }

@app.post("/learning-cycle")
async def learning_cycle(concept: str, profile: str, student_answer: str):

    result = run_learning_cycle(concept, profile, student_answer)

    return result


@app.post("/teach-pdf")
async def teach_pdf(
    file: UploadFile = File(...),
    read_time: int = Form(10),
    repeats: int = Form(0),
    scroll_speed: int = Form(50)
):

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_location)

    profile = detect_learning_mode(read_time, repeats, scroll_speed)

    lesson = generate_lesson(text, profile)
    return {
    "lesson": lesson,
    "detected_profile": profile
     }

@app.post("/adaptive-explain")
async def adaptive_explain(
    text: str,
    difficulty: str
):

    if difficulty == "confused":
        profile = "Visual"

    elif difficulty == "distracted":
        profile = "ADHD"

    elif difficulty == "exam":
        profile = "Exam"

    else:
        profile = "Dyslexia"

    lesson = generate_lesson(text, profile)

    return lesson
    from fastapi import UploadFile, File
import shutil
import os


@app.post("/teach-image")
async def teach_image(file: UploadFile = File(...), profile: str = "Visual"):

    # save uploaded image
    file_location = f"uploads/{file.filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR extraction
    extracted_text = extract_text_from_image(file_location)

    # send text to AI tutor
    lesson = generate_lesson(extracted_text, profile)

    return lesson

@app.post("/tutor-step")
async def tutor_step(concept: str, student_answer: str):

    result = tutor_interaction(concept, student_answer)

    return {
        "tutor_response": result
    }

@app.post("/generate-question")
async def generate_checkpoint_question(concept: str):

    question = generate_question(concept)

    return {
        "checkpoint_question": question
    }