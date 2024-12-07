#Definicion de 'Clase' de tipo Lepton Cargado
class Lepton():
    type = 'Lepton'
    '''
    Propiedades
    ----------------------------------------------------
    c: Carga en unidades de [e]
    m: Masa en unidades de [MeV/c^2]
    mma: Momento magnetico anomalo en unidades de [g-2]
    vm: Vida media en unidades de [τ]
    ld: Longitud de desintegracion en unidades de [cτ]
    de: Dipolo electrico en unidades de [e⋅cm]
    dd: Dipolo debil en unidades de [e⋅cm]
    ntn: Numero de tipos de neutrinos
    amg: Anomalia magnetica debil
    vnfl: Violacion de numero de familia leptonica
    '''

    def __init__(self, Carga_Electrica, Masa, MMA, Vida_Media, Longitud_Desintegracion, Dipolo_Electrico, Dipolo_Debil, Numero_Tipo_Neutrino, Anomalia_Magnetica_Debil, Violacion_Numero_Familia_Leptonica):
      self.c = Carga_Electrica
      self.m = Masa
      self.mma = MMA
      self.vm = Vida_Media
      self.ld = Longitud_Desintegracion
      self.de = Dipolo_Electrico
      self.dd = Dipolo_Debil
      self.ntn = Numero_Tipo_Neutrino
      self.amg = Anomalia_Magnetica_Debil
      self.vnfl = Violacion_Numero_Familia_Leptonica
  
    def properties(self):
      str_properties = f'Tipo: {self.type}\n' + (
          f'Carga Electrica: {str(self.c)}\n' +
          f'Masa: {str(self.m)}\n' +
          f'Momento Magentico Anomalo: {str(self.mma)}\n' +
          f'Vida Media: {str(self.vm)}\n' +
          f'Longitud de Desintegracion: {str(self.ld)}\n' +
          f'Dipolo Electrico: {str(self.de)}\n' +
          f'Dipolo Debil: {str(self.dd)}\n' +
          f'Numero de Tipos de Neutrinos: {str(self.ntn)}\n' +
          f'Anomalia Magnetica Debil: {str(self.amg)}\n' +
          f'Violacion de Numero de Familia Leptonica: {str(self.vnfl)}\n' 
    )
      print(str_properties)


#Definicion de Particulas Leptones
Electron = Lepton(
    Carga_Electrica = -1,
    Masa = "0.5109989500 ± 0.00000000015",
    MMA = "(1159.65218062 ± 0.00000012) × 10^-6",
    Vida_Media = "> 6.6 × 10^28 años",
    Longitud_Desintegracion = "---",
    Dipolo_Electrico = "< 0.041 × 10^-28",
    Dipolo_Debil = "---",
    Numero_Tipo_Neutrino = 3,
    Anomalia_Magnetica_Debil = "---",
    Violacion_Numero_Familia_Leptonica = "---"
)

Muon = Lepton(
    Carga_Electrica = -1,
    Masa = "105.6583755 ± 0.0000023",
    MMA = "(11659205.9 ± 2.2) × 10^-10",
    Vida_Media = "(2.1969811 ± 0.0000022) × 10^-6 s",
    Longitud_Desintegracion = "658.6384 m",
    Dipolo_Electrico = "< 1.8 × 10^-19",
    Dipolo_Debil = "---",
    Numero_Tipo_Neutrino = 3,
    Anomalia_Magnetica_Debil = "---",
    Violacion_Numero_Familia_Leptonica = "μ-->eγ < 4.2 × 10^-8"  
)

Tau = Lepton(
    Carga_Electrica = -1,
    Masa = "1776.93 ± 0.09",
    MMA = "-0.057 a 0.024",
    Vida_Media = "(290.3 ± 0.5) × 10^-15 s",
    Longitud_Desintegracion = "87.03 μm",
    Dipolo_Electrico = "R(dτ)=-0.185 a 0.061 × 10^-16",
    Dipolo_Debil = "R(dωτ) < 0.50 × 10^-17",
    Numero_Tipo_Neutrino = 3,
    Anomalia_Magnetica_Debil = "R(α_{ω}^{τ}) < 1.1 × 10^-3",
    Violacion_Numero_Familia_Leptonica = "τ-->μγ < 4.2 × 10^-8"  
)