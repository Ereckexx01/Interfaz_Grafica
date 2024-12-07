from First_Package.module1 import Lepton, Electron, Muon, Tau

# Prueba para las propiedades del electrón
def test_electron_properties():
    assert Electron.c == -1, "La carga eléctrica del electrón es incorrecta"
    assert "0.5109989500" in Electron.m, "La masa del electrón es incorrecta"
    assert Electron.mma == "(1159.65218062 ± 0.00000012) × 10^-6", "El momento magnético anómalo del electrón es incorrecto"
    assert Electron.vm == "> 6.6 × 10^28 años", "La vida media del electrón es incorrecta"
    assert Electron.ld == "---", "La longitud de desintegración del electrón es incorrecta"
    assert Electron.de == "< 0.041 × 10^-28", "El dipolo eléctrico del electrón es incorrecto"
    assert Electron.dd == "---", "El dipolo débil del electrón es incorrecto"
    assert Electron.ntn == 3, "El número de tipos de neutrinos del electrón es incorrecto"
    assert Electron.amg == "---", "La anomalía magnética débil del electrón es incorrecta"
    assert Electron.vnfl == "---", "La violación del número de familia leptónica del electrón es incorrecta"

# Prueba para las propiedades del muón
def test_muon_properties():
    assert Muon.c == -1, "La carga eléctrica del muón es incorrecta"
    assert "105.6583755" in Muon.m, "La masa del muón es incorrecta"
    assert Muon.mma == "(11659205.9 ± 2.2) × 10^-10", "El momento magnético anómalo del muón es incorrecto"
    assert Muon.vm == "(2.1969811 ± 0.0000022) × 10^-6 s", "La vida media del muón es incorrecta"
    assert Muon.ld == "658.6384 m", "La longitud de desintegración del muón es incorrecta"
    assert Muon.de == "< 1.8 × 10^-19", "El dipolo eléctrico del muón es incorrecto"
    assert Muon.dd == "---", "El dipolo débil del muón es incorrecto"
    assert Muon.ntn == 3, "El número de tipos de neutrinos del muón es incorrecto"
    assert Muon.amg == "---", "La anomalía magnética débil del muón es incorrecta"
    assert Muon.vnfl == "μ-->eγ < 4.2 × 10^-8", "La violación del número de familia leptónica del muón es incorrecta"

# Prueba para las propiedades del tau
def test_tau_properties():
    assert Tau.c == -1, "La carga eléctrica del tau es incorrecta"
    assert "1776.93" in Tau.m, "La masa del tau es incorrecta"
    assert Tau.mma == "-0.057 a 0.024", "El momento magnético anómalo del tau es incorrecto"
    assert Tau.vm == "(290.3 ± 0.5) × 10^-15 s", "La vida media del tau es incorrecta"
    assert Tau.ld == "87.03 μm", "La longitud de desintegración del tau es incorrecta"
    assert Tau.de == "R(dτ)=-0.185 a 0.061 × 10^-16", "El dipolo eléctrico del tau es incorrecto"
    assert Tau.dd == "R(dωτ) < 0.50 × 10^-17", "El dipolo débil del tau es incorrecto"
    assert Tau.ntn == 3, "El número de tipos de neutrinos del tau es incorrecto"
    assert Tau.amg == "R(α_{ω}^{τ}) < 1.1 × 10^-3", "La anomalía magnética débil del tau es incorrecta"
    assert Tau.vnfl == "τ-->μγ < 4.2 × 10^-8", "La violación del número de familia leptónica del tau es incorrecta"

# Prueba opcional para la creación de un leptón personalizado
def test_lepton_creation():
    custom_lepton = Lepton(
        Carga_Electrica=1,
        Masa="10 MeV",
        MMA="0.002",
        Vida_Media="100 s",
        Longitud_Desintegracion="10 m",
        Dipolo_Electrico="0.01 e⋅cm",
        Dipolo_Debil="0.02 e⋅cm",
        Numero_Tipo_Neutrino=2,
        Anomalia_Magnetica_Debil="0.001",
        Violacion_Numero_Familia_Leptonica="No"
    )
    assert custom_lepton.c == 1, "La carga eléctrica del leptón personalizado es incorrecta"
    assert custom_lepton.m == "10 MeV", "La masa del leptón personalizado es incorrecta"
    assert custom_lepton.mma == "0.002", "El momento magnético anómalo del leptón personalizado es incorrecto"
    assert custom_lepton.vm == "100 s", "La vida media del leptón personalizado es incorrecta"
    assert custom_lepton.ld == "10 m", "La longitud de desintegración del leptón personalizado es incorrecta"
    assert custom_lepton.de == "0.01 e⋅cm", "El dipolo eléctrico del leptón personalizado es incorrecto"
    assert custom_lepton.dd == "0.02 e⋅cm", "El dipolo débil del leptón personalizado es incorrecto"
    assert custom_lepton.ntn == 2, "El número de tipos de neutrinos del leptón personalizado es incorrecto"
    assert custom_lepton.amg == "0.001", "La anomalía magnética débil del leptón personalizado es incorrecta"
    assert custom_lepton.vnfl == "No", "La violación del número de familia leptónica del leptón personalizado es incorrecta"
