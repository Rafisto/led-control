"""
Class to convert color from one format to another
"""

class ColorConverter():
    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """
        Convert a color from hex to RGB format
        :param hex_color: str
        :return: tuple
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def hex_to_rgb_str_semicolon(hex_color: str) -> str:
        """
        Convert a color from hex to RGB format with semicolon separator
        :param hex_color: str
        :return: str
        """
        return ';'.join(map(str, ColorConverter.hex_to_rgb(hex_color)))
    
    @staticmethod
    def rgb_to_hex(rgb_color: tuple) -> str:
        """
        Convert a color from RGB to hex format
        :param rgb_color: tuple
        :return: str
        """
        return '#{:02x}{:02x}{:02x}'.format(*rgb_color)
    