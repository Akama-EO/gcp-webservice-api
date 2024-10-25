from flask import Flask, render_template
        

app = Flask(__name__)

@app.route("/")
def root():
    # Placeholder(s) to inflate static content in the template
    id = "S2229758"
    name = "Emmanuel Akama"

    return render_template("index.html", my_id=id, my_name=name)   
    


if __name__ == "__main__":
    # Flask's development server to serve content locally    
    app.run(host="127.0.0.1", port=8080, debug=True)

