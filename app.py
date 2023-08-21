from flask import *
from werkzeug.utils import secure_filename
import os,sys
import pandas as pd
import logging

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = 'weather'
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        # upload file flask
        f = request.files.get('file')
        app.logger.info(f)
        # Extracting uploaded file name
        data_filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)

        return render_template('index2.html')
    return render_template("index.html")


@app.route('/show_json_data')
def showdata():
    # Uploaded File Path is obtained
    data_file_path = session.get('uploaded_data_file_path', None)
    app.logger.info(data_file_path)
    response = get_json_content(data_file_path)
    # Save to disk
    save_json_to_disk(data_file_path)
    return response


# Return Json response when csv file is provided
def get_json_content(data_file_path):
    df = pd.read_csv(data_file_path)
    # Return json version of the csv file
    return Response(df.to_json(orient="records"), mimetype='application/json')


def save_json_to_disk(data_file_path):
    df = pd.read_csv(data_file_path)
    file_name = data_file_path + '.json'
    app.logger.info(file_name)
    app.logger.info("Saving to disk for verification")
    df.to_json(file_name)


@app.route('/query', methods=['GET'])
def search():
    args = request.args
    limit = args.get('limit')
    date = args.get('date')
    weather = args.get('weather')
    app.logger.info(args)
    data_file_path = session.get('uploaded_data_file_path', None)
    df_filter = pd.read_csv(data_file_path)

    if date is not None:
        app.logger.info("Checking date")
        df_filter = df_filter.loc[df_filter['date'] == date]
    if weather is not None:
        app.logger.info("Checking weather")
        df_filter = df_filter.loc[df_filter['weather'] == weather]
    if limit is not None:
        app.logger.info("Requesting the limit of {} records".format(limit))
        df_filter = df_filter.head(int(limit))

    return Response(df_filter.to_json(orient="records"), mimetype='application/json')


