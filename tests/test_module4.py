import pytest
from First_Package.module4 import Bosones, Foton, Gluon, W, Z, Higgs

# Prueba para las propiedades del fotón
def test_foton_properties():
    assert Foton.c == 0, "La carga eléctrica del fotón es incorrecta"
    assert "< 1 × 10^-18 eV" in Foton.m, "La masa del fotón es incorrecta"
    assert Foton.s == 1, "El spin del fotón es incorrecto"
    assert Foton.a == "Estable", "El ancho de desintegración del fotón es incorrecto"
    assert Foton.md == "Estable", "El modo de desintegración del fotón es incorrecto"
    assert Foton.vd == "Estable", "La vida media del fotón es incorrecta"
    assert Foton.ac == "---", "El acoplamiento con fermiones del fotón es incorrecto"
    assert Foton.ab == "---", "El acoplamiento con bosones del fotón es incorrecto"

# Prueba para las propiedades del gluón
def test_gluon_properties():
    assert Gluon.c == 0, "La carga eléctrica del gluón es incorrecta"
    assert "0 Teorico" in Gluon.m, "La masa del gluón es incorrecta"
    assert Gluon.s == 1, "El spin del gluón es incorrecto"
    assert Gluon.a == "---", "El ancho de desintegración del gluón es incorrecto"
    assert Gluon.md == "---", "El modo de desintegración del gluón es incorrecto"
    assert Gluon.vd == "Estable", "La vida media del gluón es incorrecta"
    assert Gluon.ac == "---", "El acoplamiento con fermiones del gluón es incorrecto"
    assert Gluon.ab == "---", "El acoplamiento con bosones del gluón es incorrecto"

# Prueba para las propiedades del bosón W
def test_w_properties():
    assert W.c == "± 1", "La carga eléctrica del bosón W es incorrecta"
    assert "80.3692 ± 0.0133" in W.m, "La masa del bosón W es incorrecta"
    assert W.s == 1, "El spin del bosón W es incorrecto"
    assert W.a == "2.085 ± 0.042 GeV", "El ancho de desintegración del bosón W es incorrecto"
    assert "l^+ ν (10.86 %), hadrones (67.41 %)" in W.md, "El modo de desintegración del bosón W es incorrecto"
    assert "3 × 10^-25 s" in W.vd, "La vida media del bosón W es incorrecta"
    assert W.ac == "---", "El acoplamiento con fermiones del bosón W es incorrecto"
    assert W.ab == "---", "El acoplamiento con bosones del bosón W es incorrecto"

# Prueba para las propiedades del bosón Z
def test_z_properties():
    assert Z.c == 0, "La carga eléctrica del bosón Z es incorrecta"
    assert "91.1880 ± 0.0020" in Z.m, "La masa del bosón Z es incorrecta"
    assert Z.s == 1, "El spin del bosón Z es incorrecto"
    assert Z.a == "2.4955 ± 0.0023 GeV", "El ancho de desintegración del bosón Z es incorrecto"
    assert "l^+ l^- (3.36 %), hadrones (69.91 %)" in Z.md, "El modo de desintegración del bosón Z es incorrecto"
    assert "3 × 10^-25 s" in Z.vd, "La vida media del bosón Z es incorrecta"
    assert Z.ac == "g_{lV} = -0.03783 ± 0.00041", "El acoplamiento con fermiones del bosón Z es incorrecto"
    assert Z.ab == "---", "El acoplamiento con bosones del bosón Z es incorrecto"

# Prueba para las propiedades del bosón de Higgs
def test_higgs_properties():
    assert Higgs.c == 0, "La carga eléctrica del bosón de Higgs es incorrecta"
    assert "125.20 ± 0.11" in Higgs.m, "La masa del bosón de Higgs es incorrecta"
    assert Higgs.s == 0, "El spin del bosón de Higgs es incorrecto"
    assert "3.7" in Higgs.a, "El ancho de desintegración del bosón de Higgs es incorrecto"
    assert "bb (53 %), WW* (25.7 %)" in Higgs.md, "El modo de desintegración del bosón de Higgs es incorrecto"
    assert Higgs.vd == "---", "La vida media del bosón de Higgs es incorrecta"
    assert Higgs.ac == "κ_F = 0.94 ± 0.05", "El acoplamiento con fermiones del bosón de Higgs es incorrecto"
    assert Higgs.ab == "κ_V = 1.023 ± 0.026", "El acoplamiento con bosones del bosón de Higgs es incorrecto"

# Prueba opcional para la creación de un bosón personalizado
def test_boson_creation():
    custom_boson = Bosones(
        Carga_Electrica="± 2",
        Masa="500 GeV",
        Spin=2,
        Ancho_Desintegracion="10 GeV",
        Modo_Desintegracion="Custom decay",
        Vida_Media="10^-20 s",
        Acoplamiento_Fermiones="g_custom = 0.5",
        Acoplamiento_Bosones="κ_custom = 1.2"
    )
    assert custom_boson.c == "± 2", "La carga eléctrica del bosón personalizado es incorrecta"
    assert custom_boson.m == "500 GeV", "La masa del bosón personalizado es incorrecta"
    assert custom_boson.s == 2, "El spin del bosón personalizado es incorrecto"
    assert custom_boson.a == "10 GeV", "El ancho de desintegración del bosón personalizado es incorrecto"
    assert custom_boson.md == "Custom decay", "El modo de desintegración del bosón personalizado es incorrecto"
    assert custom_boson.vd == "10^-20 s", "La vida media del bosón personalizado es incorrecta"
    assert custom_boson.ac == "g_custom = 0.5", "El acoplamiento con fermiones del bosón personalizado es incorrecto"
    assert custom_boson.ab == "κ_custom = 1.2", "El acoplamiento con bosones del bosón personalizado es incorrecto"

