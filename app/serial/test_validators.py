from app.serial.validators import Validators


def test_color_validator_normal_case():
    assert Validators.validate_color("255;255;255") is True
    assert Validators.validate_color("000;000;000") is True
    assert Validators.validate_color("0;0;0") is True
    assert Validators.validate_color("64;128;128") is True
    assert Validators.validate_color("255;0;0") is True


def test_color_validator_missing_semicolon():
    assert Validators.validate_color("255;255255") is False
    assert Validators.validate_color("") is False
    assert Validators.validate_color(";") is False
    assert Validators.validate_color("00;0") is False


def test_color_validator_non_integer():
    assert Validators.validate_color("255;hello;255") is False
    assert Validators.validate_color("hello;world'255") is False
    assert Validators.validate_color("0;0;hello") is False


def test_color_validator_missing_numbers():
    assert Validators.validate_color("0;;0") is False
    assert Validators.validate_color("0; ;0") is False
    assert Validators.validate_color(" ; ; ") is False
    assert Validators.validate_color(";;") is False
