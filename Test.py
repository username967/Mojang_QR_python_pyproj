from typing import List
from qrcodegen import QrCode, QrSegment,print_qr


def main():
	"""The main application program."""
	do_basic_demo()
	return

def do_basic_demo() -> None:
	text = "Hello, QR and pyproj!"      # User-supplied Unicode text
	errcorlvl = QrCode.Ecc.LOW  # Error correction level
	
	# Make and print the QR Code symbol
	qr = QrCode.encode_text(text, errcorlvl)
	print_qr(qr)
if __name__ == "__main__":
	main()