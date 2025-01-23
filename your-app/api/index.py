import json
from http.server import BaseHTTPRequestHandler
import os

# Load student marks from the JSON file
def load_student_marks():
    with open("students_marks.json", "r") as f:
        return json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load the student marks from the JSON file
        students_marks = load_student_marks()
        
        # Parse the query parameters from the URL
        query_params = self.parse_query_params()

        # Extract names and get the corresponding marks
        marks = [students_marks.get(name, "Not Found") for name in query_params]

        # Create response payload
        response = {"marks": marks}

        # Send response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Write the response as JSON
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def parse_query_params(self):
        # Parse query parameters from the URL
        query = self.path.split('?')[-1]
        if query:
            params = query.split('&')
            return [param.split('=')[-1] for param in params if param.startswith('name=')]
        return []
