from bottle import route, run
import OCR
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
    OCR.RunTesseractBatch()
if (__name__ == "__main__"):
    # TODO: Error in calling initialize function
    # initialize()
    run(host='localhost', port=8080)