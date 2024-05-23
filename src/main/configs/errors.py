from flask import jsonify

def handle_500(e):
    return jsonify({"data":{"error": {"status": 500, "message":"Internal Server Error"}}})
    
def handle_400(e):
    return jsonify({"data":{"error": {"status": 400, "message":"Bad Request"}}})
    
def handle_405(e):
    return jsonify({"data":{"error": {"status": 405, "message":"Method Not Allowed"}}})

def handle_404(e):
    return jsonify({"data":{"error": {"status": 404, "message":"Not Found"}}})