from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
# I am currently using this for debugging purposes, this can eventually be deleted
def get_users():

    query = '''
       SELECT * FROM INFORMATION_SCHEMA.TABLES;
    '''
    
    # Same process as handler above
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
 
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get rank of a specific user in the system
@users.route('/user/<userId>/rank', methods=['GET'])
def get_user_rank(userId):
    
    cursor = db.get_db().cursor()
    cursor.execute('SELECT Title FROM User WHERE UserId = {0}'.format(userId))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get events a specific user is attending in the system
@users.route('/user/<userId>/events', methods=['GET'])
def get_user_events(userId):

    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT DISTINCT p.Title, e.StartTime, e.EndTime
        FROM Post p JOIN Event e ON p.EventId = e.EventId
                    JOIN GroupChat gc ON p.GroupChatId = gc.GroupChatId
                    JOIN GroupChatMembers gcm ON gc.GroupChatId = gcm.GroupChatId
        WHERE gcm.UserId = {0}'''.format(userId))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get posts a specific user has made in the system
@users.route('/user/<userId>/posts', methods=['GET'])
def get_user_posts(userId):

    cursor = db.get_db().cursor()
    cursor.execute('SELECT Title FROM Post WHERE CreatedBy = {0}'.format(userId))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response