from barcode import EAN13
from barcode.writer import ImageWriter


number="123458789487"
#b_code=EAN13(number)
b_code=EAN13(number, writer=ImageWriter()) 
b_code.save("new_code")