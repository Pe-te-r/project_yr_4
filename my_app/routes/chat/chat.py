from flask import Blueprint,render_template

chatp_bp = Blueprint('chat', __name__, template_folder='templates')

@chatp_bp.route("/chat")
def chat():
    team = [
        {"name": "John Doe", "role": "Project Lead", "image": "john.jpg", "bio": "John has 10+ years in healthcare tech and leads SHA development."},
        {"name": "Jane Smith", "role": "Backend Engineer", "image": "jane.jpg", "bio": "Jane is an expert in Flask and security, ensuring SHA remains robust."},
        {"name": "David Kim", "role": "Frontend Developer", "image": "david.jpg", "bio": "David crafts engaging user experiences using React and Bootstrap."},
    ]

    testimonials = [
        {"author": "John Doe", "message": "Leading SHA has been a transformative experience."},
        {"author": "Jane Smith", "message": "Building a secure, scalable system for SHA is my passion."},
        {"author": "David Kim", "message": "Bringing the SHA vision to life with design and frontend magic!"}
    ]

    return render_template("chat.html", team=team, testimonials=testimonials)