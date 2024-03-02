from bottle import route, run
@route('/OCR')
def index():
    #TODO:
    return {"pdf_name" : "pdf1", 
            "page" : [
                {"1" : {
                    "line" : [
                        {"1" : "test line 1"},
                        {"2" : "test line 2"}
                    ]
                }},
                {"2" : {
                    "line" : [
                        {"1" : "test line 3"},
                        {"2" : "test line 2"}
                    ]
                }}
            ]}
run(host='localhost', port=8080)