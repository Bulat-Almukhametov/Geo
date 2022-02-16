import colorsys

import variables

H_MAX = 360

def get(spei: float):
    H_coefficient = (variables.H_TO - variables.H_FROM) / H_MAX - variables.H_FROM
    H = H_coefficient * (variables.SPEI_TO + spei) / (variables.SPEI_TO - variables.SPEI_FROM)
    R, G, B = colorsys.hls_to_rgb(H, variables.L, variables.S)
    return (int(255 * R), int(255 * G), int(255 * B), variables.RECT_OPACITY)
