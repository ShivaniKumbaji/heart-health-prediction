document.getElementById("heartForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fields = document.querySelectorAll("input, select");
    for (let field of fields) {
        if (!field.value) {
            alert("Please fill all fields correctly.");
            return;
        }
    }

    const data = {
        age: Number(age.value),
        sex: Number(sex.value),
        cp: Number(cp.value),
        trestbps: Number(trestbps.value),
        chol: Number(chol.value),
        fbs: Number(fbs.value),
        restecg: Number(restecg.value),
        thalach: Number(thalach.value),
        exang: Number(exang.value),
        oldpeak: Number(oldpeak.value),
        slope: Number(slope.value),
        ca: Number(ca.value),
        thal: Number(thal.value)
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();

const box = document.getElementById("resultBox");
const text = document.getElementById("resultText");
const percent = document.getElementById("riskPercent");

box.classList.remove("hidden");

if (result.prediction === "High Risk") {
    box.className = "high";
    text.innerText = "⚠️ High Risk of Heart Disease";
} else {
    box.className = "low";
    text.innerText = "✅ Low Risk of Heart Disease";
}

percent.innerText = `Risk Probability: ${result.risk_percentage}%`;

});
