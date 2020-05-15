# -*- coding: utf-8 -*-
"""
Date: May 15, 2020

@author: Rajiv Ram

"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/courses")
def coursepage():
    return render_template('courseinfo.html')

@app.route("/assignments")
def assignmentspage():
    return render_template('assignments.html')

#start the server
if __name__ == "__main__":
    app.run()
    
    