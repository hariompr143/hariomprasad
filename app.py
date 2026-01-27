#!/usr/bin/env python3
"""
Contact Form Handler for Portfolio Website
This script handles form submissions and can send emails or store data
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Configuration (use environment variables in production)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your-email@example.com')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', 'your-app-password')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'hariom.prasad@example.com')

# Data storage file
DATA_FILE = 'contact_submissions.json'


def load_submissions():
    """Load existing submissions from file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_submission(data):
    """Save submission to file"""
    submissions = load_submissions()
    submission = {
        'timestamp': datetime.now().isoformat(),
        'name': data.get('name'),
        'email': data.get('email'),
        'subject': data.get('subject'),
        'message': data.get('message')
    }
    submissions.append(submission)
    
    with open(DATA_FILE, 'w') as f:
        json.dump(submissions, f, indent=2)


def send_email(name, email, subject, message):
    """Send email notification"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f'Portfolio Contact: {subject}'
        
        # Email body
        body = f"""
        New contact form submission from your portfolio website:
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        
        ---
        Sent: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'message': 'Missing required fields'
            }), 400
        
        # Save submission
        save_submission(data)
        
        # Send email notification
        email_sent = send_email(
            data['name'],
            data['email'],
            data['subject'],
            data['message']
        )
        
        return jsonify({
            'success': True,
            'message': 'Message received successfully!',
            'email_sent': email_sent
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing request: {str(e)}'
        }), 500


@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    """Get all contact form submissions (admin only - add authentication)"""
    try:
        submissions = load_submissions()
        return jsonify({
            'success': True,
            'count': len(submissions),
            'submissions': submissions
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving submissions: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200


if __name__ == '__main__':
    print("Starting Portfolio Contact Form API...")
    print(f"Server running on http://localhost:5000")
    print(f"Contact endpoint: POST http://localhost:5000/api/contact")
    app.run(debug=True, host='0.0.0.0', port=5000)
