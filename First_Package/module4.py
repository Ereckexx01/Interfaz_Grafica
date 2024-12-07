#Definicion de 'Clase' de tipo Bosones
class Bosones():
    type = 'Bosones'
    '''
    Propiedades
    ----------------------------------------------------
    c: Carga en unidades de [e]
    m: Masa en unidades de [MeV/c^2]
    s: Spin en unidades de [J]
    a: Ancho de Desintegracion en unidades de [Γ]
    md: Modos de Desintegracion 
    vd: Vida Media
    ac: Acoplamiento con Fermiones
    ab: Acoplamiento con Bosones
    '''

    def __init__(self, Carga_Electrica, Masa, Spin, Ancho_Desintegracion, Modo_Desintegracion, Vida_Media, Acoplamiento_Fermiones, Acoplamiento_Bosones):
      self.c = Carga_Electrica
      self.m = Masa
      self.s = Spin  
      self.a = Ancho_Desintegracion
      self.md = Modo_Desintegracion
      self.vd = Vida_Media
      self.ac = Acoplamiento_Fermiones
      self.ab = Acoplamiento_Bosones 
        
    def properties(self):
      str_properties = f'Tipo: {self.type}\n' + (
          f'Carga Electrica: {str(self.c)}\n' +
          f'Masa: {str(self.m)}\n' +
          f'Spin: {str(self.s)}\n' +
          f'Ancho de Desintegracion: {str(self.a)}\n'  +
          f'Modos de Desintegracion: {str(self.md)}\n' +
          f'Vida Media: {str(self.vd)}\n' +
          f'Acoplamiento con Fermiones: {str(self.ac)}\n' +
          f'Acoplamiento con Bosones: {str(self.ab)}\n' 
    )
      print(str_properties)


#Definicion de Particulas Bosones
Foton = Bosones(
    Carga_Electrica = 0,
    Masa = "< 1 × 10^-18 eV",
    Spin = 1,
    Ancho_Desintegracion = "Estable",
    Modo_Desintegracion = "Estable",
    Vida_Media = "Estable",
    Acoplamiento_Fermiones = "---",
    Acoplamiento_Bosones = "---"
)

Gluon = Bosones(
    Carga_Electrica = 0,
    Masa = "0 Teorico",
    Spin = 1,
    Ancho_Desintegracion = "---",
    Modo_Desintegracion = "---",
    Vida_Media = "Estable",
    Acoplamiento_Fermiones = "---",
    Acoplamiento_Bosones = "---"
)

W = Bosones(
    Carga_Electrica = "± 1",
    Masa = "80.3692 ± 0.0133",
    Spin = 1,
    Ancho_Desintegracion = "2.085 ± 0.042 GeV",
    Modo_Desintegracion = "l^+ ν (10.86 %), hadrones (67.41 %)",
    Vida_Media = "3 × 10^-25 s",
    Acoplamiento_Fermiones = "---",
    Acoplamiento_Bosones = "---"
)

Z = Bosones(
    Carga_Electrica = 0,
    Masa = "91.1880 ± 0.0020",
    Spin = 1,
    Ancho_Desintegracion = "2.4955 ± 0.0023 GeV",
    Modo_Desintegracion = "l^+ l^- (3.36 %), hadrones (69.91 %)",
    Vida_Media = "3 × 10^-25 s",
    Acoplamiento_Fermiones = "g_{lV} = -0.03783 ± 0.00041",
    Acoplamiento_Bosones = "---"
)

Higgs = Bosones(
    Carga_Electrica = 0,
    Masa = "125.20 ± 0.11",
    Spin = 0,
    Ancho_Desintegracion = "3.7_{1.4}^{1.9} MeV",
    Modo_Desintegracion = "bb (53 %), WW* (25.7 %)",
    Vida_Media = "---",
    Acoplamiento_Fermiones = "κ_F = 0.94 ± 0.05",
    Acoplamiento_Bosones = "κ_V = 1.023 ± 0.026"
)