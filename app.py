from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Sample data for services
SERVICES = [
    {
        "name": "Web Development", 
        "icon": "fas fa-code", 
        "description": "Custom web applications and responsive websites"
    },
    {
        "name": "Mobile Apps", 
        "icon": "fas fa-mobile-alt", 
        "description": "iOS and Android native & cross-platform applications"
    },
    {
        "name": "UI/UX Design", 
        "icon": "fas fa-palette", 
        "description": "User-centered design with modern interfaces"
    },
    {
        "name": "Cloud Solutions", 
        "icon": "fas fa-cloud", 
        "description": "Scalable cloud infrastructure and deployment"
    },
    {
        "name": "Digital Marketing", 
        "icon": "fas fa-chart-line", 
        "description": "SEO, social media, and online presence management"
    },
    {
        "name": "Software Consulting", 
        "icon": "fas fa-laptop-code", 
        "description": "Technical guidance and digital transformation"
    }
]

# Sample gallery images
GALLERY_IMAGES = [
    {"src": "/static/images/gym1.jpg", "alt": "Modern Gym Equipment"},
    {"src": "/static/images/gym2.jpg", "alt": "Group Training Session"},
    {"src": "/static/images/gym3.jpg", "alt": "Personal Training"},
    {"src": "/static/images/gym4.jpg", "alt": "Cardio Zone"},
    {"src": "/static/images/gym5.jpg", "alt": "Yoga Class"},
    {"src": "/static/images/gym6.jpg", "alt": "Strength Area"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images=GALLERY_IMAGES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash('Please fill in all fields', 'error')
        else:
            # Here you would typically save to database or send email
            flash('Message sent successfully! We\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Basic validation
        if not username or not password:
            flash('Please fill in all fields', 'error')
        else:
            # Here you would typically check against database
            if username == 'demo' and password == 'password':
                session['user'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Basic validation
        if not all([fullname, email, username, password]):
            flash('Please fill in all fields', 'error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
        else:
            # Here you would typically save to database
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)