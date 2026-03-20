let currentSkill = "";
let currentQuestions = [];
let currentIndex = 0;
let answers = [];
let participantName = "";

// Login
function login() {
    participantName = document.getElementById('name').value;
    if (participantName.trim() === "") {
        alert("Please enter your name");
        return;
    }
    document.getElementById('login').classList.add('hidden');
    document.getElementById('skill').classList.remove('hidden');
}

// Start Test
function startTest(skill) {
    currentSkill = skill;
    currentIndex = 0;
    answers = [];
    fetch(`/mcqs/${skill}`)
        .then(res => res.json())
        .then(data => {
            currentQuestions = data;
            document.getElementById('skill').classList.add('hidden');
            document.getElementById('quiz').classList.remove('hidden');
            showQuestion();
        });
}

// Show Question
function showQuestion() {
    const q = currentQuestions[currentIndex];
    document.getElementById('skillTitle').innerText = currentSkill + " Test";
    document.getElementById('question').innerText = q.question;
    q.options.forEach((opt, i) => {
        document.getElementById('opt' + i).innerText = opt;
    });
    document.getElementById('progressFill').style.width = ((currentIndex / currentQuestions.length) * 100) + "%";
}

// Check Answer
function checkAnswer(ans) {
    answers.push(ans);
    currentIndex++;
    if (currentIndex < currentQuestions.length) {
        showQuestion();
    } else {
        submitAnswers();
    }
}

// Submit Answers to backend
function submitAnswers() {
    fetch("/submit", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: participantName,
            skill: currentSkill,
            answers: answers
        })
    })
    .then(res => res.json())
    .then(response => {
        document.getElementById('quiz').classList.add('hidden');
        document.getElementById('result').classList.remove('hidden');
        document.getElementById('score').innerText = "Score: " + response.score;
        document.getElementById('level').innerText = "Level: " + response.level;
        document.getElementById('recommendation').innerText = response.recommendation;

        // Show certificate download
        const downloadBtn = document.getElementById('downloadBtn');
        downloadBtn.href = "/download/" + response.certificate;
        downloadBtn.classList.remove('hidden');
    });
}
