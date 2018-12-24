from flask import Flask,render_template,request
from flask_restful import Resource,Api

application = Flask(__name__)
api = Api(application)

#@application.route("/")
#def main():
   
#    return render_template('index.html')

class apipred(Resource):
     def post(self):
          data = request.get_json()
          name = data['name']
          name = name + "!!!"
          return name

api.add_resource(apipred,'/apipred/')

if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)

