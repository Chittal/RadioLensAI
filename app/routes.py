from flask import Blueprint, render_template, request, session, jsonify
from app.chat import get_response

# Create a blueprint for the app routes
main_routes = Blueprint('main', __name__)

# Define the route for the home page
@main_routes.route('/')
def home():
    return render_template('home.html')

# Define the route for the profile page
@main_routes.route('/profile')
def profile():
    return render_template('profile.html')

# Define the route for the generate report page
@main_routes.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    # Initialize chat history in session if not already done
    if 'chat_history' not in session:
        session['chat_history'] = []
    # Simulate a conversation
    if request.method == 'POST':
        print('I')
        user_input = request.json['input']
        print(user_input)
        if user_input.lower() in ['exit', 'quit', 'bye']:
            output = "Goodbye! Have a great day!"
        else:
            output = get_response(user_input)
        session['chat_history'].append({'type': 'user', 'text': user_input})
        session['chat_history'].append({'type': 'ai', 'text': output})
        session.modified = True
        return jsonify({'response': output})
    print(session['chat_history'])
    return render_template('generate_report.html', chat_history=session['chat_history'])

# Define the route for the reports page
@main_routes.route('/view_reports')
def view_reports():
    return render_template('view_reports.html')

# Define the route for the contact us page
@main_routes.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
