from First_Package.module2 import Neutrino, Neutrino_Electron, Neutrino_Muon, Neutrino_Tau

# Prueba para las propiedades del neutrino del electrón
def test_neutrino_electron_properties():
    assert Neutrino_Electron.c == 0, "La carga eléctrica del neutrino del electrón es incorrecta"
    assert "< 0.8" in Neutrino_Electron.m, "La masa del neutrino del electrón es incorrecta"
    assert Neutrino_Electron.mm == "< 0.064 × 10^-10", "El momento magnético del neutrino del electrón es incorrecto"
    assert Neutrino_Electron.ntn == "3", "El número de tipos de neutrinos es incorrecto"
    assert Neutrino_Electron.vmm == "> 300", "La vida media/masica del neutrino del electrón es incorrecta"
    assert Neutrino_Electron.am12 == "0.307 ± 0.013", "El ángulo de mezcla θ_12 del neutrino del electrón es incorrecto"
    assert Neutrino_Electron.am23 == "0.553 ± 0.016", "El ángulo de mezcla θ_23 del neutrino del electrón es incorrecto"
    assert Neutrino_Electron.am13 == "0.0219 ± 0.0007", "El ángulo de mezcla θ_13 del neutrino del electrón es incorrecto"

# Prueba para las propiedades del neutrino del muón
def test_neutrino_muon_properties():
    assert Neutrino_Muon.c == 0, "La carga eléctrica del neutrino del muón es incorrecta"
    assert "< 0.8" in Neutrino_Muon.m, "La masa del neutrino del muón es incorrecta"
    assert Neutrino_Muon.mm == "< 0.064 × 10^-10", "El momento magnético del neutrino del muón es incorrecto"
    assert Neutrino_Muon.ntn == "3", "El número de tipos de neutrinos es incorrecto"
    assert Neutrino_Muon.vmm == "> 7 × 10^9", "La vida media/masica del neutrino del muón es incorrecta"
    assert Neutrino_Muon.am12 == "0.307 ± 0.013", "El ángulo de mezcla θ_12 del neutrino del muón es incorrecto"
    assert Neutrino_Muon.am23 == "0.553 ± 0.016", "El ángulo de mezcla θ_23 del neutrino del muón es incorrecto"
    assert Neutrino_Muon.am13 == "0.0219 ± 0.0007", "El ángulo de mezcla θ_13 del neutrino del muón es incorrecto"

# Prueba para las propiedades del neutrino del tau
def test_neutrino_tau_properties():
    assert Neutrino_Tau.c == 0, "La carga eléctrica del neutrino del tau es incorrecta"
    assert "< 0.8" in Neutrino_Tau.m, "La masa del neutrino del tau es incorrecta"
    assert Neutrino_Tau.mm == "< 0.064 × 10^-10", "El momento magnético del neutrino del tau es incorrecto"
    assert Neutrino_Tau.ntn == "3", "El número de tipos de neutrinos es incorrecto"
    assert Neutrino_Tau.vmm == "> 15.4", "La vida media/masica del neutrino del tau es incorrecta"
    assert Neutrino_Tau.am12 == "0.307 ± 0.013", "El ángulo de mezcla θ_12 del neutrino del tau es incorrecto"
    assert Neutrino_Tau.am23 == "0.553 ± 0.016", "El ángulo de mezcla θ_23 del neutrino del tau es incorrecto"
    assert Neutrino_Tau.am13 == "0.0219 ± 0.0007", "El ángulo de mezcla θ_13 del neutrino del tau es incorrecto"

# Prueba opcional para la creación de un neutrino personalizado
def test_neutrino_creation():
    custom_neutrino = Neutrino(
        Carga_Electrica=0,
        Masa="1.2 MeV",
        Momento_Magnetico="0.03 × 10^-10",
        Numero_Tipo_Neutrino="2",
        Vida_Media_Masica="500 s/eV",
        Angulo_Mezcla_12="0.2",
        Angulo_Mezcla_23="0.3",
        Angulo_Mezcla_13="0.1"
    )
    assert custom_neutrino.c == 0, "La carga eléctrica del neutrino personalizado es incorrecta"
    assert custom_neutrino.m == "1.2 MeV", "La masa del neutrino personalizado es incorrecta"
    assert custom_neutrino.mm == "0.03 × 10^-10", "El momento magnético del neutrino personalizado es incorrecto"
    assert custom_neutrino.ntn == "2", "El número de tipos de neutrinos del neutrino personalizado es incorrecto"
    assert custom_neutrino.vmm == "500 s/eV", "La vida media/masica del neutrino personalizado es incorrecta"
    assert custom_neutrino.am12 == "0.2", "El ángulo de mezcla θ_12 del neutrino personalizado es incorrecto"
    assert custom_neutrino.am23 == "0.3", "El ángulo de mezcla θ_23 del neutrino personalizado es incorrecto"
    assert custom_neutrino.am13 == "0.1", "El ángulo de mezcla θ_13 del neutrino personalizado es incorrecto"
