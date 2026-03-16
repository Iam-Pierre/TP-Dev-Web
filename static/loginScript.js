 async function handleLogin() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (data.ok) {
                window.location.href = "/";  
            } else {
                document.getElementById('error').style.display = 'block';
                document.getElementById('error').textContent = data.error;
            }
        }