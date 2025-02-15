// Function to get CSRF token from Django cookies
function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            cookieValue = cookie.substring("csrftoken=".length, cookie.length);
            break;
        }
    }
    return cookieValue;
}

async function shortenURL () {

    const longURL = document.getElementById("long-url").value;
    const response = await fetch("http://127.0.0.1:8000/api/shorten/", {
        method: "POST",
        headers: {"content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() 
        },
        body: JSON.stringify({long_url: longURL}),
    });

    const data = await response.json ();

    if (response.ok) {

        document.getElementById("short-url").innerHTML = 
       `Shortened URL: <a href="http://127.0.0.1:8000/api/${data.short_url}" target="_blank">/api/${data.short_url}</a>`;
    } else {

        document.getElementById("short-url").innerHTML = `Error: ${data.error}`;

    }
    
    
}

async function getOriginalURL() {
    const shortCode = document.getElementById("short-url-input").value;

    const response = await fetch(`http://127.0.0.1:8000/api/${shortCode}/`, { method: "GET" });

    if (response.ok) {
        const data = await response.json();
        window.location.href = data.long_url; // Redirect to original URL
    } else {
        const data = await response.json();
        document.getElementById("original-url").innerText = `Error: ${data.error}`;
    }
}