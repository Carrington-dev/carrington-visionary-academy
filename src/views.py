from datetime import datetime
from src import app
from flask import render_template

@app.context_processor
def inject_globals():
    company = "Carrington Visionary Academy"
    return {
        "company": company,
        "year": 2025,
        "phone": '+27 (0) 67 735 2242',
        "title": 'Independent Private Schools In South Africa!',
        "email": 'hello@cvacademy.co.za',
        "address": "395 Francis Baard Street</p><p>Pretoria Central, 0001</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/team")
def team():
    return render_template("team.html")

# Add More About Us Pages

@app.route("/academic-excellence")
def academic_excellence():
    return render_template("about/academic_excellence.html")

@app.route("/our-offering")
def our_offering():
    return render_template("about/our_offering.html")

@app.route("/our-principles")
def our_principles():
    return render_template("about/our_principles.html")