"""
--------------------------------------------------
Initial Setup
--------------------------------------------------
"""
#import necessary libraries
from flask import Flask, render_template
import requests
import platform
import json
from bs4 import BeautifulSoup

#Instance of Flask to create the app
app = Flask(__name__)

#Route to homepage of Web Service
@app.route('/')
def get_homepage():
    return render_template('homepage.html')

"""
--------------------------------------------------
Task 1: GET /ping request should return “pong”.
--------------------------------------------------
"""

#Route to /ping
@app.route('/ping')
def get_ping():
    return '<h3>Pong</h3>'

"""
----------------------------------------------------------------------------------------------------
Task 2: GET /system request should return JSON object with service version and system information.
----------------------------------------------------------------------------------------------------
"""

#Route to /system
@app.route('/system')
def get_systeminfo():
    #Dictionary to store system information
    service_info = {
        "Web Service Version":"1.0.0",
        "Platform Version":platform.version(),
        "OS":platform.system(),
        "Processor":platform.processor()
    }

    #convert dictionary to JSON
    service_info_json = json.dumps(service_info)
    
    return render_template('system.html',sys_info=service_info_json)


"""
---------------------------------------------------------------------------------
Task3: GET /mediainfo/<id> should return a JSON object with image filename, size,
dimensions and image title.
---------------------------------------------------------------------------------
"""

#Route to /mediainfo/<id>
@app.route('/mediainfo/<id>')
def get_mediainfo(id):
    #URL generation for scaping the image
    url = 'https://www.pond5.com/photo/'+id
    response = requests.get(url)

    #Parse the html file 
    soup = BeautifulSoup(response.text, 'html.parser')

    #search the tag that has the image description
    element = soup.find("meta",attrs={"name":"description"})["content"]
    element_str = str(element)

    #dictionary to store image information 
    image_info = {}
    
    #get title of the image
    img_title = element_str.split('.')[0]
    image_info["Title"]=img_title

    #get filename of the image
    filename = soup.find_all('a',
                            class_="Button Button--bare ItemDetailV4-downloadPreviewBtn u-textUpperCase variant u-weightSemibold u-text12px u-isHidden:0-40em js-downloadPreview js-previewDownloadButton")

    filename_str = str(filename)

    img_filename = filename_str.split('%')[3].split('&')[0]

    image_info["Filename"]=img_filename

    #get dimensions of the image
    dimensions = element_str.split('x')
    dim1 = dimensions[0].rstrip().split()[-1]
    dim2 = dimensions[1].lstrip().split()[0].split('.')[0]
    img_dimensions = dim1+" x "+dim2
    image_info["Dimensions"]=img_dimensions
    
    #convert dictionary to JSON
    image_info_json = json.dumps(image_info)
    
    return render_template('img.html',img_info=image_info_json)
    
"""
--------------------------------------------------
Run the application
--------------------------------------------------
"""

if(__name__=='__main__'):
    app.run()