import cv2

__belgium_file = "CoreFlags/Flag_of_Belgium.png"
__france_file = "CoreFlags/Flag_of_France.png"
__germany_file = "CoreFlags/Flag_of_Germany.png"
__trans_pride_file = "CoreFlags/Transgender_Pride_flag.png"
__indian_file = "CoreFlags/Flag_of_India.png"
__serbian_file = "CoreFlags/Flag_of_Serbia.png"
__panama_file = "CoreFlags/Flag_of_Panama.png"

def __get_img(filename: str):
    return cv2.imread(filename, 1)

german_flag = __get_img(__germany_file)
french_flag = __get_img(__france_file)
belgian_flag = __get_img(__belgium_file)
trans_pride_flag = __get_img(__trans_pride_file)
indian_flag = __get_img(__indian_file)
serbian_flag = __get_img(__serbian_file)
panama_flag = __get_img(__panama_file)

__all__ = [german_flag, french_flag, belgian_flag, trans_pride_flag, indian_flag, serbian_flag, panama_flag]
