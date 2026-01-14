from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Personal details that are unanimous along all the pages
@app.context_processor
def inject_site_details():
    details = {
        "address": "J.P. Vihar Colony, Mangla, Bilaspur(C.G.)",
        "email": "vivekanand.school.public@gmail.com",
        "contact": "(+91) 83052-27722",
        "index_title": "Vivekanand Public School",
        "enquiry_title": "Enquiry",
    }
    return dict(details=details)


# This is for making the index page
@app.route("/")
def test_page():
    return render_template("index.html")


@app.route("/enquiry")
def enquiry():
    return render_template("enquiry.html")


# This block allows you to run the application directly
if __name__ == "__main__":
    app.run(debug=True)
