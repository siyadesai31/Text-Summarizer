from flask import Flask, render_template,request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    print("Hello")
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyse():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        # print(rawtext)
        summary, original_txt, len_orig_text, len_summary = summarizer(rawtext)

        return render_template('summary.html',summary=summary, original_txt= original_txt, len_orig_text=len_orig_text,len_summary=len_summary )
    # return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)