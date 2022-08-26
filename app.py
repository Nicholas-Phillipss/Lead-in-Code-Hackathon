from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # home page
    return render_template('base.html')

@app.route('/myreceipts')
    # receipt page
def receipts():
    return render_template('receipt.html')

@app.route('/mylessons')
    # lessons page
def lesson():
    return render_template('lessons.html')

