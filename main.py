from flask import Flask, request,render_template,send_file,send_from_directory
import os
import passgen
from random import sample

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './endpoints'
@app.route('/upload', methods = ["POST", "GET"])  
def upload():
    
  if request.method == 'POST':
    f = request.files['file']
    n=passgen.passgen()
    file=f.filename.split('.')
    if file[-1]=="docx":
      file[-1]="pdf"
    if file[-1]=="xls":
      file[-1]="xlsx"
    f.filename=f"{n}.{file[-1]}"

    
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))

      
    return f'https://Your_Domain/{n}.{file[-1]}'


  
@app.route('/<string:name>')
def got(name):  
  f=name
  file=f.split('.')[-1]
  if file=="pdf" or file=="docx" or file=="xlsx":
    #return send_file(f'./endpoints/{f}', 'application/pdf',as_attachment=True,attachment_filename="answer.pdf")
     return send_from_directory(app.config['UPLOAD_FOLDER'], f)
  else:
    print(f)
    with open(f"./endpoints/{f}","r") as f:
      data=f.read()
      return render_template("index.html",tags=data)
    
if __name__ == "__main__":
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)
