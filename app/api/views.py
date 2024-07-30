from flask import Blueprint, render_template, jsonify, request
from app.models import Flight
from app.notification_service.sms_service import send_sms_notification

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/flight_status', methods=['GET'])
def get_flight_status():
    flights = Flight.get_all_flights()
    return jsonify(flights)

@bp.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    flight = Flight.get_flight_by_id(flight_id)
    if flight:
        return jsonify(flight)
    else:
        return jsonify({'error': 'Flight not found'}), 404

@bp.route('/notify', methods=['POST'])
def notify():
    data = request.json
    to = data.get('to')
    message = data.get('message')
    notification_type = data.get('type', 'sms')

    if notification_type == 'sms' and to and message:
        try:
            send_sms_notification(to, message)
            return jsonify({'status': 'Notification sent'}), 200
        except Exception as e:
            return jsonify({'error': f'Failed to send SMS notification: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Invalid data or notification type'}), 400

@bp.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    email = data.get('email')
    phone = data.get('phone')

    if not email or not phone:
        return jsonify({'error': 'Email and phone are required'}), 400

    # Here you would typically add the subscriber to your database
    # For this example, we'll just return a success message
    return jsonify({'message': 'Subscription successful'}), 200