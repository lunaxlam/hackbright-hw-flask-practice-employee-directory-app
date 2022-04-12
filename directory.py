from flask import Flask, request, render_template, redirect, flash
from model import employee_directory

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


@app.route("/")
def home():
    """Show the employee directory home page, which has a search form."""

    return render_template("home.html")


@app.route("/search")
def get_employee_details():
    """Process search and return the employee details page."""

    # Get employee name from search form (passed in the request object)
    name = request.args.get("employee_name")

    # If the user didn't type anything, ask them to.
    if not name:
        flash("Please type in a first name.")

    # If the name isn't in our directory, flash a message to the user.
    elif name.lower() not in employee_directory:
        flash(f"{name} not found.")

    # We have a name, and it's in our directory. Return that info.
    else:
        employee_info = employee_directory.get(name.lower())
        return render_template("employee_details.html", details=employee_info)

    # If we didn't return the employee details page, send the user back to the
    # page they were on before.
    return(redirect(request.referrer))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
