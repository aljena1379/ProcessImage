from bottle import route, run
from dotenv import load_dotenv
from tesseract import ocr
import os


load_dotenv()
SERVER_ADDRESS = os.getenv('SERVER_ADDRESS')
SERVER_PORT = os.getenv('SERVER_PORT')
TESSERACT_COMMAND = os.getenv('TESSERACT_COMMAND')

@route('/OCR')
def index():
    return "DONE!"
    # TODO: If needed, set RunTesseract to fill out lines in JSON.
    # jsonFile = {"pdf_name" : "pdf1", 
    #         "page" : [
    #             {"1" : {
    #                 "line" : [
    #                     {"1" : "test line 1"},
    #                     {"2" : "test line 2"}
    #                 ]
    #             }},
    #             {"2" : {
    #                 "line" : [
    #                     {"1" : "test line 3"},
    #                     {"2" : "test line 2"}
    #                 ]
    #             }}
    #         ]}
    # return jsonFile
def initialize():
    ocr.RunTesseractBatch()


if (__name__ == "__main__"):
    # TODO: Error in calling initialize function
    # initialize()
    run(host=SERVER_ADDRESS, port=SERVER_PORT)