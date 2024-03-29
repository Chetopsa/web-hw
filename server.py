from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote_plus

new_entries =""
def get_body_params(body):
    if not body:
        return {}
    parameters = body.split("&")

    # split each parameter into a (key, value) pair, and escape both
    def split_parameter(parameter):
        k, v = parameter.split("=", 1)
        k_escaped = unquote_plus(k)
        v_escaped = unquote_plus(v)
        return k_escaped, v_escaped

    body_dict = dict(map(split_parameter, parameters))
    print(f"Parsed parameters as: {body_dict}")
    # return a dictionary of the parameters
    return body_dict


def submission_to_table(item):
    """TODO: Takes a dictionary of form parameters and returns an HTML table row

    An example input dictionary might look like: 
    {
     'event': 'Sleep',
     'day': 'Sun',
     'start': '01:00',
     'end': '11:00', 
     'phone': '1234567890', 
     'location': 'Home',
     'extra': 'Have a nice dream', 
     'url': 'https://example.com'
    }
    
    """
    global new_entries
    table_row = "<tr><td>"
    table_row += item.get("event") + "</td>"
    table_row += "<td>"+item.get("days") + "</td>"
    table_row += "<td>"+item.get("start") + "</td>"
    table_row += "<td>"+item.get("end") + "</td>"
    table_row += "<td>"+item.get("phone") + "</td>"
    table_row += "<td>"+item.get("location") + "</td>"
    table_row += "<td>"+item.get("info") + "</td>"
    table_row += "<td>"+ "<a href='"+item.get("url")+"'target='_blank'>"+item.get("url")+"</a></td>"
    table_row += "</tr>"
    new_entries += table_row
    return new_entries


# NOTE: Please read the updated function carefully, as it has changed from the
# version in the previous homework. It has important information in comments
# which will help you complete this assignment.
def handle_req(url, body=None):
    """
    The url parameter is a *PARTIAL* URL of type string that contains the path
    name and query string.

    If you enter the following URL in your browser's address bar:
    `http://localhost:4131/MyForm.html?name=joe` then the `url` parameter will have
    the value "/MyForm.html?name=joe"

    This function should return two strings in a list or tuple. The first is the
    content to return, and the second is the content-type.
    """

    # Get rid of any query string parameters
    url, *_ = url.split("?", 1)
    # Parse any form parameters submitted via POST
    global new_entries
    parameters = get_body_params(body)

    if url == "/MySchedule.html":
        return open("static/html/MySchedule.html").read(), "text/html"
    if url == "/MyForm.html":
        return open("static/html/MyForm.html").read(), "text/html"
    elif url == "/AboutMe.html":
        return open("static/html/AboutMe.html").read(), "text/html"
    elif url == "/img/gophers-mascot.png":
        return open("static/img/gophers-mascot.png", "br").read(), "image/png"
    # NOTE: These files may be different for your server, but we include them to
    # show you examples of how yours may look. You may need to change the paths
    # to match the files you want to serve. Before you do that, make sure you
    # understand what the code is doing, specifically with the MIME types and
    # opening some files in binary mode, i.e. `open(..., "br")`.
    elif url == "/css/style.css":
        return open("static/css/style.css").read(), "text/css"
    elif url == "/js/schedule.js":
        return open("static/js/schedule.js").read(), "text/javascript"
    
    elif url == "/js/profile.js":
        return open("static/js/profile.js").read(), "text/javascript"
    elif url == "/img/Dan1.jpeg":
        return open("static/img/Dan1.jpeg", "br").read(), "image/jpeg"
    elif url == "/img/Lind.jpg":
        return open("static/img/Lind.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Tate.png":
        return open("static/img/Tate.png", "br").read(), "image/png"
    elif url == "/img/zoom.jpg":
        return open("static/img/zoom.jpg", "br").read(), "image/jpeg"
    elif url == "/img/vanCleve.jpg":
        return open("static/img/vanCleve.jpg", "br").read(), "image/jpeg"
    elif url == "/img/breakfast.jpg":
        return open("static/img/breakfast.jpg", "br").read(), "image/jpeg"
    elif url == "/img/track.jpg":
        return open("static/img/track.jpg", "br").read(), "image/jpeg"

    elif url == "/img/Nicholson.jpg":
        return open("static/img/Nicholson.jpg", "br").read(), "image/jpeg"

    elif url == "/img/Wiley.jpg":
        return open("static/img/Wiley.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Akerman.jpg":
        return open("static/img/Akerman.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Civil_Engineering.jpg":
        return open("static/img/Civil_Engineering.jpg", "br").read(), "image/jpeg"
    elif url == "/img/Molecular_Biology.jpg":
        return open("static/img/Molecular_Biology.jpg", "br").read(), "image/jpeg"
    elif url == "/img/walter.jpg":
        return open("static/img/walter.jpg", "br").read(), "image/jpeg"
    elif url == "/img/anderson.jpg":
        return open("static/img/anderson.jpg", "br").read(), "image/jpeg"
    
    
    # TODO: Add update the HTML below to match your other pages and
    # implement the `submission_to_table`.
    
    elif url == "/EventLog.html":
        if new_entries == "" and len(parameters) == 0:
            return open("static/html/EventLog.html").read(), "text/html"
        elif len(parameters) != 0:
            submission_to_table(parameters)
        return (
            """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title> Event Submission </title>
                <link href="css/style.css" type="text/css" rel="stylesheet">
            </head>
            <body>
                <header>
                  <nav>
                    <!-- TODO: Update to appear like the navigation in your other
                    pages if needed -->
                      <a href="/MySchedule.html">My Schedule</a>
                      <a href="/AboutMe.html">About Me</a>
                      <a href="/MyForm.html">Form Input</a>
                      <a href="/EventLog.html">My New Events</a>
                  </nav>
                </header>
                <h1> My New Events </h1>
                <div>
                    <table id="table2">
                        <thead>
                            <tr>
                                <th>Event</th>
                                <th>Day</th>
                                <th>Start</th>
                                <th>End</th>
                                <th>Phone</th>
                                <th>Location</th>
                                <th>Extra Info</th>
                                <th>URL</th>
                            </tr>
                        </thead>
                        <tbody>
                        """
            + new_entries
            + """
                        </tbody>
                    </table>
                </div>
            </body>
            </html>""",
            "text/html; charset=utf-8",
        )
    else:
        return open("static/html/404.html").read(), "text/html; charset=utf-8"


# You shouldn't change content below this. It would be best if you just left it alone.


class RequestHandler(BaseHTTPRequestHandler):
    def __c_read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        body = str(body, encoding="utf-8")
        return body

    def __c_send_response(self, message, response_code, headers):
        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        # Send the first line of response.
        self.protocol_version = "HTTP/1.1"
        self.send_response(response_code)

        # Send headers (plus a few we'll handle for you)
        for key, value in headers.items():
            self.send_header(key, value)
        self.send_header("Content-Length", len(message))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()

        # Send the file.
        self.wfile.write(message)

    def do_GET(self):
        # Call the student-edited server code.
        message, content_type = handle_req(self.path)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )

    def do_POST(self):
        body = self.__c_read_body()
        message, content_type = handle_req(self.path, body)

        # Convert the return value into a byte string for network transmission
        if type(message) == str:
            message = bytes(message, "utf8")

        self.__c_send_response(
            message,
            200,
            {
                "Content-Type": content_type,
                "Content-Length": len(message),
                "X-Content-Type-Options": "nosniff",
            },
        )


def run():
    PORT = 4131
    print(f"Starting server http://localhost:{PORT}/")
    server = ("", PORT)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


run()
