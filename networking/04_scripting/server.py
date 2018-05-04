from flask import Flask, render_template
import requests
import time
app = Flask(__name__)
# We use current time to name our search result
# This way we can save our history of searches
current_milli_time = int(round(time.time() * 1000))
file_name = str(current_milli_time)
extension = ".html"


@app.route('/')
def index():
    """Index page of our application."""
    return render_template('index.html')


@app.route('/my-link/')
def my_link():
    """Create the new search result and redirect to it."""
    data = {
            "OfficeId": 675,
            "MobilityCategoryId": 17,
            "Type": 2
           }
    r = requests.post('http://licytacje.komornik.pl/Notice/Search', data=data)
    path_file = "templates/" + file_name + extension
    path_render = file_name + extension
    days_file = open(path_file, 'w')
    days_file.write(r.text)
    return render_template(path_render)

if __name__ == '__main__':
    app.run(debug=True)
