import cv2

__belgium_file = "Flag_of_Belgium.png"
__france_file = "Flag_of_France.png"
__germany_file = "CoreFlags/Flag_of_Germany.png"
__trans_pride_file = "CoreFlags/Transgender_Pride_flag.png"

def __get_img(filename: str):
    return cv2.imread(filename, 1)


german_flag = __get_img(__germany_file)
french_flag = __get_img(__france_file)
belgian_flag = __get_img(__belgium_file)
trans_pride_flag = __get_img(__trans_pride_file)

__all__ = [german_flag, french_flag, belgian_flag, trans_pride_flag]
