# flask-file-upload

Flask application that allows you to upload files to your domain and access them using its generated endpoint. The supported files are: PDF, Docx and Xlsx

Example:
response = requests.post('https:Your_Domain/upload', files={'file': open('example.html', 'rb')})

The response will be your domain followed by the generated endpoint.
Example response:
https://Your_Domain/Generated_Endpoint.html

You can now open the url in your brower and view your upload.
