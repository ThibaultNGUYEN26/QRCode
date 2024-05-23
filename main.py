import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path, final_size):
    qr_version = 5
    qr_box_size = 10

    qr = qrcode.QRCode(
        version=qr_version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=qr_box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    qr_img = qr_img.resize(final_size, Image.LANCZOS)

    logo = Image.open(logo_path)
    logo_size = min(final_size) // 5
    logo.thumbnail((logo_size, logo_size), Image.LANCZOS)

    pos = ((final_size[0] - logo.size[0]) // 2, (final_size[1] - logo.size[1]) // 2)

    qr_img.paste(logo, pos, logo)

    qr_img.save(output_path)
    print(f"The QR code with logo has been saved to {output_path}")

# Usage
if __name__ == "__main__":
    generate_qr_with_logo("{link}", "{logo_inside_QRcode}", "{QRcode_name}", (900, 900))
