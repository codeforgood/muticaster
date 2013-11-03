from api import app
from api.schemavalidator import sendhub_schema, is_valid
from flask import make_response, request, jsonify, abort

from api.multicastservice import get_routing, get_recipients_assigned_for_routing

@app.route('/')
def hello():
    return 'Welcome to SendHub Message Routing API Home. Please POST to /api/sendhub/v1.0/routes for routing request.'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/api/sendhub/v1.0/routes', methods=['POST'])
def multi_cast():
    data = request.json
    if not data or not is_valid(data, sendhub_schema):
        abort(400)
    recipients = data['recipients']
    routing_table = get_routing(recipients)
    recipients_routing = get_recipients_assigned_for_routing(routing_table, recipients)
    return jsonify({"routes": recipients_routing})
