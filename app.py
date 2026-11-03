module 3 chapter 2
----------------------
module.exports = async function (context, req) {

    try {

        // Get current date and time
        const now = new Date();

        // Get current date in IST
        const currentDate = now.toLocaleDateString("en-IN", {
            timeZone: "Asia/Kolkata",
            day: "2-digit",
            month: "2-digit",
            year: "numeric"
        });

        // Get current time in IST
        const currentTime = now.toLocaleTimeString("en-IN", {
            timeZone: "Asia/Kolkata",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
        });

        // Get complete date and time
        const currentDateTime = now.toLocaleString("en-IN", {
            timeZone: "Asia/Kolkata",
            day: "2-digit",
            month: "2-digit",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
            hour12: true
        });

        // Prepare JSON response
        const result = {
            status: "Success",
            message: "Current date and time fetched successfully",
            currentDate: currentDate,
            currentTime: currentTime,
            currentDateTime: currentDateTime,
            timeZone: "Asia/Kolkata",
            utcTimestamp: now.toISOString()
        };

        // Log output
        context.log("Date and Time:", currentDateTime);

        // Return HTTP response
        context.res = {
            status: 200,
            headers: {
                "Content-Type": "application/json"
            },
            body: result
        };

    } catch (error) {

        context.log("Error:", error);

        context.res = {
            status: 500,
            headers: {
                "Content-Type": "application/json"
            },
            body: {
                status: "Error",
                message: error.message
            }
        };
    }
};
-----------------------
module 3 chapter 3
-----------------
app.py
from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask Azure App</title>
        </head>
        <body>
            <h1>Welcome to Python Flask on Azure App Service!</h1>
            <p>Application deployed successfully.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Flask application is running"
    })

@app.route("/api")
def api():
    return jsonify({
        "application": "Flask on Azure App Service",
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
------------------------------
req.txt
Flask
gunicorn
