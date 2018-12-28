from flask import Flask,render_template,request
from flask_restful import Resource,Api
import os

application = Flask(__name__)
api = Api(application)

#@application.route("/")
#def main():
   
#    return render_template('index.html')

class apipred(Resource):
     def post(self):
          data = request.get_json()
          print(data)
          name = data['name']
          name = name + "!!!"
          f = open('log.txt','a')          
          print("Worker ID:" + str(os.getpid()),file=f)         
          print(data,file=f)
          print(name,file=f)
          return name

api.add_resource(apipred,'/apipred/')

if __name__ == "__main__":
    application.run(host='0.0.0.0',port=80,debug=True)

