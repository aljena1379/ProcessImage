# TODO: Remove if RunTesseractBatch works.
# import pytesseract
# from PIL import Image
# def ProcessImage():
    # img = Image.open("testImg.jpg")
    # result = pytesseract.image_to_string(img)
    # print(result)
def RunTesseractBatch():
    import subprocess
    subprocess.run([r"\RunTesseract.bat"])