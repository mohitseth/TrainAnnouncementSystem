from flask import Flask, session, render_template, request,flash , redirect, g, url_for
from playsound import playsound
from preprocessing import generateAnnouncement
import os
app = Flask(__name__)


@app.route('/')
def index():
	return render_template("form.html")


@app.route('/formfun',methods=['GET', 'POST'])
def formfun():
	fcity = request.form.get('fcity')
	via = request.form.get('via')
	to = request.form.get('to')
	train_no = request.form.get('train_no')
	train_name = request.form.get('train_name')
	platform = request.form.get('platform')

	dict1 = {'fcity': fcity, 'via': via, 'to':to ,'train_no':train_no, 'train_name':train_name,'platform': platform}
	generateAnnouncement(**dict1)
	playsound(f"announcement_{train_no}.mp3")
	os.remove(f"announcement_{train_no}.mp3")
	return render_template("form.html")
    

if __name__ == '__main__':
    app.run(debug=True)