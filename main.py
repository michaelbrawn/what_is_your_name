# What is Your Name

import cgi
import webapp2


form = """
<form method="post">
    What is your Name?
    <br>
    <label> Name:
        <!-- # Put your text input here -->
    </label>
    <br>
    <br>
    <!-- # Put your submit input button here -->
    <p>%(error)s</p>
</form>
"""


def escape_html(s):
    if s == "":
        return "''"
    s = s.replace("&", "&amp;")  # Must be done first!
    return cgi.escape(s, quote=True)


def valid_name(name):
    # Check if the name is a string
    # Check that it's more than one character long
    # Check that it doesn't have any numbers in it
    # If all of these are true, return true
    return False


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", name=""):
        self.response.out.write(form % {
            "error": error,
            "name": name
        })

    def get(self):
        self.write_form()

    def post(self):
        name = self.request.get("name")

        valid_name_check = valid_name(name)

        if not (valid_name_check):
            self.write_form(
                "That doesn't look valid to me. Please enter a valid name",
                name
            )
        else:
            self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's an awesome name!")


app = webapp2.WSGIApplication(
    [("/", MainPage), ("/thanks", ThanksHandler)], debug=True)
