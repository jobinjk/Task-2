from flask import Flask, jsonify, request, json, redirect, url_for

app = Flask(__name__)   # creating app name
# app.config['DEBUG'] = True
@app.route('/') # setting app route for eg 127.0.0.1:5000/<something>

def api_root(): # creating a function api_root which returns some txt to url
    return 'Welcome to RESTfull FLASK'



@app.route('/messages', methods = ['POST']) # setting another route /messages methods as post

def api_message(): # creating a function api_message which gives a json data when a form is submitted in url
    data= request.get_json()
    # data.pop('ashjdja')
    print data

    return jsonify(data) # returns the data as json format

# this is to show HTTP 302 response

@app.route('/redirectA') # setting another route /redirectA which redirect data to b
def redir_a():
    print "Now in A"
    return redirect(url_for('redir_b'))

@app.route('/redirectB') #setting another route /redirectA which redirect data to c
def redir_b():
    print "Now in B"
    return redirect(url_for('redir_c'))

@app.route('/redirectC')
def redir_c():
    print "Now in C"
    return jsonify({'Final destination':'C'}) # received data in c

# error handling 404

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

# error handling 500

@app.errorhandler(500)
def site_block(error=None):
    message = {
            'status': 500,
            'message': 'site blocked: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}
    
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()


@app.route('/secrets')
def api_hello():
    return "Shhh this is top secret spy stuff!"


if __name__ == '__main__':
    app.run()