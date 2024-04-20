"""
Validator module for serial write commands
"""


class Validators:
    """
    Validate color string
    Generally in the form of 'x;y;z' where 0 < x,y,z < 256
    """

    @staticmethod
    def validate_color(c_str) -> bool:
        if c_str.count(';') != 2:
            return False
        for n_str in c_str.split(';'):
            try:
                if 0 <= int(n_str) < 256:
                    pass
                else:
                    return False
            except ValueError:
                return False
        return True
