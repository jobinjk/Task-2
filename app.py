from flask import Flask, jsonify, request, json, redirect, url_for, render_template

import random,string

app = Flask(__name__)   # creating app name
# app.config['DEBUG'] = True
@app.route('/') # setting app route for eg 127.0.0.1:5000/<something>

def api_root(): # creating a function api_root which returns some txt to url
    return render_template('intex.html')



@app.route('/messages', methods = ['POST']) # setting another route /messages methods as post

def api_message(): # creating a function api_message which gives a json data when a form is submitted in url
    data= request.get_json()
    # data.pop('ashjdja')
    print data

    data['new'] = "new data value"

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
    return render_template("redirc.html") # received data in c

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


@app.route('/secrets')
def api_hello():
    return render_template("secrt.html")

@app.route('/secrets/getSecrets', methods = ['GET'])
def get_secrets():
    li = [ gen_text() for x in xrange(50)]

    return jsonify(data=li)
def gen_text():
    return "".join( [random.choice(string.letters) for i in xrange(15)])

if __name__ == '__main__':
    app.run()