from api import app
from api.schemavalidator import sendhub_schema, is_valid
from flask import make_response, request, jsonify, abort

from api.multicastservice import get_routing, get_recipients_assigned_for_routing

@app.route('/')
def hello():
    """
    Home URL welcome request handler
    """
    msg = 'Welcome to SendHub Message Routing API Home. Please POST to /api/sendhub/v1.0/routes for routing request.'
    return jsonify({"message": msg})


@app.errorhandler(404)
def not_found(error):
    """
    404 Error handler
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_found(error):
    """
    400 Error handler
    """
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(500)
def not_found(error):
    """
    500 Error handler
    """
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@app.route('/api/sendhub/v1.0/routes', methods=['POST'])
def multi_cast():
    # parse the post json body
    data = request.json
    # verify for post body presence and structure verification using jsonschema
    if not data or not is_valid(data, sendhub_schema):
        abort(400)
    recipients = data['recipients']
    # generate routing table
    routing_table = get_routing(recipients)
    # generate actual routing details based on above routing table and recipients
    recipients_routing = get_recipients_assigned_for_routing(routing_table, recipients)
    # return the above routes as json and 200 ok
    return jsonify({"routes": recipients_routing})
