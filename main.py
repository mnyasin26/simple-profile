from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def profile():
    name = "Muhamad Nur Yasin Amadudin"
    bio = "just a chill guy."
    age = 22
    phone = "+62895357831982"
    email = "forsvive22@gmail.com"
    job_title = "Software Engineer"
    style_url = url_for('static', filename='style.css')
    profile_img_url = "https://storage.googleapis.com/static_image_linearc/AGC_20230423_173943825.jpg"
    return render_template('index.html', name=name, bio=bio, age=age, phone=phone, email=email, job_title=job_title, style_url=style_url, profile_img_url=profile_img_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
