from flask import Blueprint, jsonify
from game.core.dungeon import Dungeon, DungeonClass

dungeon_bp = Blueprint('dungeon', __name__)

@dungeon_bp.route('/dungeons', methods=['GET'])
def get_dungeons():
    return jsonify([
        {'class': dc.name, 'level': dc.value} 
        for dc in DungeonClass
    ]), 200

@dungeon_bp.route('/enter/<dungeon_class>', methods=['POST'])
def enter_dungeon(dungeon_class):
    dungeon = Dungeon(DungeonClass[dungeon_class])
    # Add combat logic here
    return jsonify({'message': 'Dungeon entered'}), 200