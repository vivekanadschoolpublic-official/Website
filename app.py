from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Making variables to use the modularity and asset saving.
index_title = "Vivekanand Public School"
enquiry_title = "Enquiry"


# This is for making the index page
@app.route("/")
def test_page():
    return render_template("index.html", title=index_title)


@app.route("/enquiry")
def enquiry():
    return render_template("enquiry.html", title=enquiry_title)


# This block allows you to run the application directly
if __name__ == "__main__":
    app.run(debug=True)
