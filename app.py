"""Flask entry point for the Frutiger Aero image interface."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Show the image-based desktop interface."""
    return render_template('index.html')


@app.route('/network', endpoint='network')
@app.route('/documents', endpoint='documents')
@app.route('/music', endpoint='music')
@app.route('/pictures', endpoint='pictures')
@app.route('/settings', endpoint='settings')
def desktop_shortcut():
    """Keep every image shortcut on the same exact desktop interface."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)