from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from vehicle_monitoring import predict

app = Flask(__name__)

@app.route('/')
def index():
    table_html, csv_exists = display_output()
    return render_template('index.html', table_html=table_html, csv_exists=csv_exists)


@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return redirect(url_for('index'))

    video = request.files['video']
    if video.filename == '':
        return redirect(url_for('index'))

    video.save("my_video.mp4")
    upload_message = "Upload Successful!"
    table_html, csv_exists = display_output()
    return render_template('index.html', upload_message=upload_message, table_html=table_html, csv_exists=csv_exists)


@app.route('/process')
def process_video():
    predict()
    message = "Video Processed Successfully!"
    table_html, csv_exists = display_output()
    return render_template('index.html', message=message, table_html=table_html, csv_exists=csv_exists)


@app.route('/download', methods=['GET'])
def download_result():
    file_name = "output.csv"
    try:
        return send_file(file_name, as_attachment=True)
    except Exception as e:
        return str(e)


@app.route('/reset', methods=['POST'])
def reset_output():
    """Delete CSV, logs and reset state (keep video)"""
    # Paths
    output_file_path = os.path.join(os.getcwd(), 'output.csv')
    log_file_path = os.path.join(os.getcwd(), 'vehicle_monitoring.log')

    # Remove CSV if exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Remove log file if exists
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    # Return app to fresh state
    message = "Application has been reset! CSV and logs cleared."
    return render_template('index.html', message=message, table_html="", csv_exists=False, upload_message="")


def display_output():
    output_file_path = os.path.join(os.getcwd(), 'output.csv')
    if os.path.exists(output_file_path):
        df = pd.read_csv(output_file_path)
        table_html = df.to_html(classes='table table-bordered table-striped')
        return table_html, True
    else:
        return "", False 


if __name__ == '__main__':
    app.run(debug=True)
