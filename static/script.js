const form = document.getElementById("formulaire");
const show = document.getElementById("show");
form.addEventListener("submit", (e) => {
e.preventDefault();
    form.style.display = 'none';
    show.style.display = 'inline-block'
    const data = Object.fromEntries(new FormData(form))
    fetch("/api/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((result) => {
        let prob = result.probability;
        alert(`Probabilité d'être diabétique: ${prob}`);
        if (isNaN(prob)) prob=0;
        prob = (prob * 100).toFixed(2);
        document.getElementById("result").textContent = `Probabilité d'être diabétique: ${prob}%`;
    })
});


async function handleLogout() { 
    console.log("Logout clicked");
    const response = await fetch('/api/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    if (data.ok) {
        window.location.href = "/";  
    }
}
document.getElementById("logout").addEventListener("click", handleLogout);

// const progressbar = document.getElementById("prediction").style.width = data['prediction']*100 + "%";
// progressbar.style






