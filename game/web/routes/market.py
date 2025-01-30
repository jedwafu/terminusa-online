from flask import Blueprint, request, jsonify
from game.core.marketplace import Marketplace

market_bp = Blueprint('market', __name__)
marketplace = Marketplace()

@market_bp.route('/listings', methods=['GET'])
def get_listings():
    return jsonify([
        {
            'item_id': l.item_id,
            'price': l.price,
            'currency': l.currency
        } for l in marketplace.listings
    ]), 200

@market_bp.route('/purchase', methods=['POST'])
def purchase_item():
    data = request.json
    success = marketplace.buy_item(
        request.current_user,
        data['item_id']
    )
    return jsonify({'success': success}), 200 if success else 400