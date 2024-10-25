from flask import Flask, render_template
from google.cloud import storage

client = storage.Client()

BUCKET_NAME = "ccws-cw01-bucket01"
STORAGE_API_PATH = "https://storage.googleapis.com"
BUDDY_LISTING = {
    1: {'name': "Ayana Anjuman .", 'campus': "Glasgow Campus", 'photo': "ayana.jpg", 'connection': "Beauty with brains. Always the first to respond to my queries during lecture sessions (even more on Slack). Hope we get to meet in person. Perhaps, we can chat a litte more about the dot."},
    2: {'name': "Yosra Bouassida", 'campus': "London Campus", 'photo': "yosra.jpg", 'connection': "Dedicated and hardworking. One of the best in the London campus. These days we're always next to one another solving problems in the lab."},
    3: {'name': "Terence Nigel Francis", 'campus': 'Glasgow Campus', 'photo': "terence.jpg", 'connection': "Buddy from afar. There seem to be a connection between us, 'cos we're both not shy at ask questions during lecture sessions."}
   }
  
        

app = Flask(__name__)

@app.route("/")
def root():
    # Placeholder(s) to inflate static content in the template
    id = "S2229758"
    name = "Emmanuel Akama"

    return render_template("index.html", my_id=id, my_name=name)
    

@app.route('/buddies')
def buddy_listing():
    # Placeholder(s) to inflate static content in the template
    buddies = BUDDY_LISTING
    
    return render_template("buddies.html", buddy_listing=buddies)


@app.route('/buddy/<int:position>')
def buddy_details(position):
    # Placeholder(s) to inflate static content in the template 
    name = BUDDY_LISTING[position]['name']
    campus = BUDDY_LISTING[position]['campus']
    photo_url = STORAGE_API_PATH + '/' + BUCKET_NAME + '/' + BUDDY_LISTING[position]['photo']
    connection = BUDDY_LISTING[position]['connection']
    
    return render_template("/buddy.html", student_position=position, student_photo_url=photo_url, student_name=name, student_campus=campus, student_connection=connection)
    

@app.route('/buddy/photo/<int:position>')
def photo_details(position):
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.get_blob(BUDDY_LISTING[position]['photo'])
    
    # Placeholder(s) to inflate static content in the template          
    photo_name = blob.name
    photo_size = blob.size
    photo_url = blob.media_link
    photo_type = blob.content_type
    photo_created_on = blob.timeCreated.strftime("%B %d, %Y; %H:%M:%S")
    
    return render_template("/photo.html", student_photo_name=photo_name, student_photo_size=photo_size, student_photo_url=photo_url, student_photo_type=photo_type, student_photo_created_on=photo_created_on)

    


if __name__ == "__main__":
    # Flask's development server to serve content locally    
    app.run(host="127.0.0.1", port=8080, debug=True)

