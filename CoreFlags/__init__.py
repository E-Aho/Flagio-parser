import cv2

__belgium_file = "Flag_of_Belgium.svg"
__france_file = "Flag_of_France.svg"
__germany_file = "Flag_of_Germany.svg"
__trans_pride_file = "Transgender_Pride_flag.png"

def __get_img(filename: str):
    return cv2.imread(filename)


german_flag = __get_img(__germany_file)
french_flag = __get_img(__france_file)
belgian_flag = __get_img(__belgium_file)
trans_pride_flag = __get_img(__trans_pride_file)

__all__ = [german_flag, french_flag, belgian_flag, trans_pride_flag]
