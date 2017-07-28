import json
import base64
import sqlite3
import logging
import cStringIO
import subprocess
import tornado.web
import tornado.ioloop

from PIL import Image
from tornado import gen

logging.basicConfig(
    filename="error_log.log",
    format='%(levelname)-8s - %(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.INFO)


class main_handler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, to you!')


class upload_file(tornado.web.RequestHandler):
    def get(self):
        self.write("You are at the upload_file page.")

    @gen.coroutine
    def post(self):

        print ('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        print ("Server got the request")

        f = json.loads(self.request.body)
        image_string = cStringIO.StringIO(base64.b64decode(f.get("image.jpg")))
        image = Image.open(image_string)
        print (image.size[0], image.size[1])
        image = image.resize((image.size[0]//3, image.size[1]//3), Image.ANTIALIAS)
        image.save('test.jpg')

        print ('Server save image')

        self.write(object_recognition())


# recognize object and prepare json file
def object_recognition():

    print ('Server start recognition')

    bashCommand = "./darknet detect cfg/yolo.cfg yolo.weights test.jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print ('Server recognized: {}'.format(output))

    targets = ['bag', 'watch', 'spectacles', 'smartphone']

    for target in targets:
        if target in output:
            return json.dumps(get_data_from_database(target))

    print ('Server return 500 error')


# get data from database using recognized objects
def get_data_from_database(type):

    print ('Server find goods into database')

    connection = sqlite3.connect("goods.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM goods WHERE type=?', (type,))

    final = {'result': list()}

    for data in cursor.fetchall():
        with open(data[3], "rb") as imageFile:
            str = base64.b64encode(imageFile.read())

        data = {'name': data[1], 'price': data[4], 'image': str}
        final["result"].append(data)

    print ('Server find this goods: {}'.format(final))

    return final


def make_app():
    return tornado.web.Application([
        (r"/", main_handler),
        (r"/upload_file", upload_file),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()