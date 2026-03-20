from flask import Flask, render_template, request, jsonify, send_file
from ai_logic import MCQS, evaluate_answers, analyze_score
from certificate import generate_certificate

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Skill-based MCQs API
@app.route("/mcqs/<skill>", methods=["GET"])
def get_mcqs(skill):
    questions = MCQS.get(skill, [])
    return jsonify([
        {
            "question": q["question"],
            "options": q["options"]
        } for q in questions
    ])

# Submit answers API
@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    skill = data.get("skill")
    name = data.get("name", "Participant")
    answers = data.get("answers", [])

    # Evaluate score & skill level
    score = evaluate_answers(skill, answers)
    level = analyze_score(score)

    # Generate certificate
    pdf_path = generate_certificate(name, skill)

    return jsonify({
        "score": score,
        "level": level,
        "recommendation": f"Your {skill} skill level is {level}",
        "certificate": pdf_path
    })

# Certificate download route
@app.route('/download/<path:filename>')
def download_certificate(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
