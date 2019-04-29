from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import win32com.client
import time
import pythoncom

# Initialize the Flask application
app = Flask( __name__ )
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'images/'+time.strftime( "%d%m%y" )
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit( '.', 1 )[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route( "/upload", methods=["POST", "GET"] )
def upload():
    if request.method == "POST":
        # print(request.)
        pythoncom.CoInitialize()
        if "file" not in request.files:
            return jsonify( "Please upload a file" )
        save_file = request.files["file"]
        if save_file.filename == "":
            return jsonify( "Select proper file" )
        if save_file and allowed_file( save_file.filename ):
            save_file_name = secure_filename( save_file.filename )
            if not os.path.exists( "images/" + time.strftime( "%d%m%y" ) ):
                os.makedirs( "images/" + time.strftime( "%d%m%y" ) )
            save_file.save( os.path.join( app.config['UPLOAD_FOLDER'], save_file_name ) )
            msginfo = win32com.client.Dispatch( "MSMQ.MSMQQueueInfo" )

            computer_name = os.getenv( 'COMPUTERNAME' )

            msginfo.FormatName = "direct=os:" + computer_name + "\\PRIVATE$\\idg"
            msgqueue = msginfo.Open( 2, 0 )  # Open a ref to queue

            msg = win32com.client.Dispatch( "MSMQ.MSMQMessage" )

            msg.Label = time.strftime( "%d%m%y%H%M%S" )
            msg.Body = "dfdfd"
            msg.Send( msgqueue )

            msgqueue.Close()

            return jsonify( "file save to queue" ), 200
    else:
        return jsonify( "Request method error" ), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="9001")
