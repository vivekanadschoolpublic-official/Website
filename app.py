from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Faculty details
@app.context_processor
def inject_faculty_details():
    faculties = {
        "Principal": "Mrs. Preeti Singh",
        "Incharge": "Mrs. Shuchi Patel",
        "Manager": "Ms. Sanskriti Singh",
        "Academic_incharge": "Mrs. Mamta Chauhan",
        "Primary_incharge": "Mrs. Bharti Singh",
    }
    return dict(faculty=faculties)


# Personal details that are unanimous along all the pages
@app.context_processor
def inject_site_details():
    details = {
        "address": "J.P. Vihar Colony, Mangla, Bilaspur(C.G.)",
        "email": "vivekanand.school.public@gmail.com",
        "contact": "(+91) 83052-27722",
        "secondary_contact": "(+91) 88392-05805",
        "index_title": "Vivekanand Public School",
        "enquiry_title": "Enquiry",
        "faqs_title": "Frequently Asked Questions",
    }
    return dict(details=details)


# This is for making the index page
@app.route("/")
def test_page():
    return render_template("index.html")


@app.route("/enquiry")
def enquiry():
    return render_template("enquiry.html")


@app.route("/faqs")
def faq():
    return render_template("faqs.html")


# This block allows you to run the application directly
if __name__ == "__main__":
    app.run(debug=True)
