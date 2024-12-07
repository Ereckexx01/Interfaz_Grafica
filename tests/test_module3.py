from First_Package.module3 import Quarks, Up, Down, Strange, Charm, Bottom, Top

# Prueba para las propiedades del quark Up
def test_up_properties():
    assert Up.c == "+ 2/3", "La carga eléctrica del quark Up es incorrecta"
    assert "2.16 ± 0.07" in Up.m, "La masa del quark Up es incorrecta"
    assert Up.i == "I = 1/2, I_z = + 1/2", "El isospin del quark Up es incorrecto"
    assert Up.se == 0, "El sabor extraño del quark Up es incorrecto"
    assert Up.see == 0, "El sabor encantado del quark Up es incorrecto"
    assert Up.si == 0, "El sabor inferior del quark Up es incorrecto"
    assert Up.sp == 0, "El sabor superior del quark Up es incorrecto"
    assert "m_u / m_d = 0.462 ± 0.020" in Up.rm, "La relación de masa del quark Up es incorrecta"
    assert Up.a == "---", "El ancho de desintegración del quark Up es incorrecto"
    assert Up.d == "---", "Los decaimientos del quark Up son incorrectos"

# Prueba para las propiedades del quark Down
def test_down_properties():
    assert Down.c == "- 1/3", "La carga eléctrica del quark Down es incorrecta"
    assert "4.70 ± 0.07" in Down.m, "La masa del quark Down es incorrecta"
    assert Down.i == "I = 1/2, I_z = - 1/2", "El isospin del quark Down es incorrecto"
    assert Down.se == 0, "El sabor extraño del quark Down es incorrecto"
    assert Down.see == 0, "El sabor encantado del quark Down es incorrecto"
    assert Down.si == 0, "El sabor inferior del quark Down es incorrecto"
    assert Down.sp == 0, "El sabor superior del quark Down es incorrecto"
    assert Down.rm == "---", "La relación de masa del quark Down es incorrecta"
    assert Down.a == "---", "El ancho de desintegración del quark Down es incorrecto"
    assert Down.d == "---", "Los decaimientos del quark Down son incorrectos"

# Prueba para las propiedades del quark Strange
def test_strange_properties():
    assert Strange.c == "- 1/3", "La carga eléctrica del quark Strange es incorrecta"
    assert "93.5 ± 0.8" in Strange.m, "La masa del quark Strange es incorrecta"
    assert Strange.i == "I = 0", "El isospin del quark Strange es incorrecto"
    assert Strange.se == -1, "El sabor extraño del quark Strange es incorrecto"
    assert Strange.see == 0, "El sabor encantado del quark Strange es incorrecto"
    assert Strange.si == 0, "El sabor inferior del quark Strange es incorrecto"
    assert Strange.sp == 0, "El sabor superior del quark Strange es incorrecto"
    assert "m_s / m_d = 17 a 22" in Strange.rm, "La relación de masa del quark Strange es incorrecta"
    assert Strange.a == "---", "El ancho de desintegración del quark Strange es incorrecto"
    assert Strange.d == "---", "Los decaimientos del quark Strange son incorrectos"

# Prueba para las propiedades del quark Charm
def test_charm_properties():
    assert Charm.c == "+ 2/3", "La carga eléctrica del quark Charm es incorrecta"
    assert "1273 ± 4.6" in Charm.m, "La masa del quark Charm es incorrecta"
    assert Charm.i == "I = 0", "El isospin del quark Charm es incorrecto"
    assert Charm.se == 0, "El sabor extraño del quark Charm es incorrecto"
    assert Charm.see == 1, "El sabor encantado del quark Charm es incorrecto"
    assert Charm.si == 0, "El sabor inferior del quark Charm es incorrecto"
    assert Charm.sp == 0, "El sabor superior del quark Charm es incorrecto"
    assert "m_c - m_b = 3.45 ± 0.05 GeV" in Charm.rm, "La relación de masa del quark Charm es incorrecta"
    assert Charm.a == "---", "El ancho de desintegración del quark Charm es incorrecto"
    assert Charm.d == "---", "Los decaimientos del quark Charm son incorrectos"

# Prueba opcional para la creación de un quark personalizado
def test_quark_creation():
    custom_quark = Quarks(
        Carga_Electrica="± 2",
        Masa="500 GeV",
        Isospin="I = 0",
        Sabor_Extraño=0,
        Sabor_Encantado=0,
        Sabor_Inferior=1,
        Sabor_Superior=0,
        Relacion_Masa="m_custom / m_b = 0.5",
        Ancho_Desintegracion="0.01 GeV",
        Decaimientos="Custom decay"
    )
    assert custom_quark.c == "± 2", "La carga eléctrica del quark personalizado es incorrecta"
    assert custom_quark.m == "500 GeV", "La masa del quark personalizado es incorrecta"
    assert custom_quark.i == "I = 0", "El isospin del quark personalizado es incorrecto"
    assert custom_quark.rm == "m_custom / m_b = 0.5", "La relación de masa del quark personalizado es incorrecta"

