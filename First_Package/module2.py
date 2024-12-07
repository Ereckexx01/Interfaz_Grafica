#Definicion de 'Clase' de tipo Lepton Neutrino
class Neutrino():
    type = 'Neutrino'
    '''
    Propiedades
    ----------------------------------------------------
    c: Carga en unidades de [e]
    m: Masa en unidades de [MeV/c^2]
    mm: Momento magnetico en unidades de [e⋅cm]
    ntn: Numero de tipos de neutrinos
    vmm: Vida media/masica en unidades de [τ/m] [s/eV]
    am12: Angulo de mezcla θ_12 
    am23: Angulo de mezcla θ_23 
    am13: Angulo de mezcla θ_13
    '''

    def __init__(self, Carga_Electrica, Masa, Momento_Magnetico, Numero_Tipo_Neutrino , Vida_Media_Masica, Angulo_Mezcla_12, Angulo_Mezcla_23, Angulo_Mezcla_13):
      self.c = Carga_Electrica
      self.m = Masa
      self.mm = Momento_Magnetico
      self.ntn = Numero_Tipo_Neutrino  
      self.vmm = Vida_Media_Masica
      self.am12 = Angulo_Mezcla_12
      self.am23 = Angulo_Mezcla_23
      self.am13 = Angulo_Mezcla_13

    def properties(self):
      str_properties = f'Tipo: {self.type}\n' + (
          f'Carga Electrica: {str(self.c)}\n' +
          f'Masa: {str(self.m)}\n' +
          f'Momento Magnetico: {str(self.mm)}\n' +
          f'Numero de Tipos de Neutrinos: {str(self.ntn)}\n' +
          f'Vida Media/Masica: {str(self.vmm)}\n' +
          f'Angulo de mezcla θ_12: {str(self.am12)}\n' +
          f'Angulo de mezcla θ_23: {str(self.am23)}\n' +
          f'Angulo de mezcla θ_13: {str(self.am13)}\n'
    )
      print(str_properties)


#Definicion de Particulas Neutrinos
Neutrino_Electron = Neutrino(
    Carga_Electrica = 0,
    Masa = "< 0.8",
    Momento_Magnetico = "< 0.064 × 10^-10",
    Numero_Tipo_Neutrino = "3", 
    Vida_Media_Masica = "> 300",
    Angulo_Mezcla_12 = "0.307 ± 0.013",
    Angulo_Mezcla_23 = "0.553 ± 0.016",
    Angulo_Mezcla_13 = "0.0219 ± 0.0007"
)

Neutrino_Muon = Neutrino(
    Carga_Electrica = 0,
    Masa = "< 0.8",
    Momento_Magnetico = "< 0.064 × 10^-10",
    Numero_Tipo_Neutrino = "3", 
    Vida_Media_Masica = "> 7 × 10^9",
    Angulo_Mezcla_12 = "0.307 ± 0.013",
    Angulo_Mezcla_23 = "0.553 ± 0.016",
    Angulo_Mezcla_13 = "0.0219 ± 0.0007"
)

Neutrino_Tau = Neutrino(
    Carga_Electrica = 0,
    Masa = "< 0.8",
    Momento_Magnetico = "< 0.064 × 10^-10",
    Numero_Tipo_Neutrino = "3", 
    Vida_Media_Masica = "> 15.4",
    Angulo_Mezcla_12 = "0.307 ± 0.013",
    Angulo_Mezcla_23 = "0.553 ± 0.016",
    Angulo_Mezcla_13 = "0.0219 ± 0.0007"
)

