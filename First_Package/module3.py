#Definicion de 'Clase' de tipo Quarks
class Quarks():
    type = 'Quarks'
    '''
    Propiedades
    ----------------------------------------------------
    c: Carga en unidades de [e]
    m: Masa en unidades de [MeV/c^2]
    i: Isospin
    se: Sabor Extraño
    see: Sabor Encantado
    si: Sabor Inferior 
    sp: Sabor Superior
    rm: Relacion Masa
    a: Ancho de Desintegracion en unidades de [Γ]
    d: Decaimientos
    '''

    def __init__(self, Carga_Electrica, Masa, Isospin, Sabor_Extraño, Sabor_Encantado, Sabor_Inferior, Sabor_Superior, Relacion_Masa, Ancho_Desintegracion, Decaimientos):
      self.c = Carga_Electrica
      self.m = Masa
      self.i = Isospin  
      self.se = Sabor_Extraño
      self.see = Sabor_Encantado
      self.si = Sabor_Inferior
      self.sp = Sabor_Superior
      self.rm = Relacion_Masa
      self.a = Ancho_Desintegracion
      self.d = Decaimientos
        
    def properties(self):
      str_properties = f'Tipo: {self.type}\n' + (
          f'Carga Electrica: {str(self.c)}\n' +
          f'Masa: {str(self.m)}\n' +
          f'Isospin: {str(self.i)}\n' +
          f'Sabor Extraño: {str(self.se)}\n' +
          f'Sabor Encantado: {str(self.see)}\n' +
          f'Sabor Inferior: {str(self.si)}\n' +
          f'Sabor Superior: {str(self.sp)}\n' +
          f'Relacion Masa: {str(self.rm)}\n'  +
          f'Ancho de Desintegracion: {str(self.a)}\n'  +
          f'Decaimientos: {str(self.d)}\n'  
    )
      print(str_properties)


#Definicion de Particulas Quarks
Up = Quarks(
    Carga_Electrica = "+ 2/3",
    Masa = "2.16 ± 0.07",
    Isospin = "I = 1/2, I_z = + 1/2", 
    Sabor_Extraño = 0,
    Sabor_Encantado = 0,
    Sabor_Inferior = 0,
    Sabor_Superior = 0,
    Relacion_Masa = "m_u / m_d = 0.462 ± 0.020",
    Ancho_Desintegracion = "---",
    Decaimientos = "---",
)

Down = Quarks(
    Carga_Electrica = "- 1/3",
    Masa = "4.70 ± 0.07",
    Isospin = "I = 1/2, I_z = - 1/2", 
    Sabor_Extraño = 0,
    Sabor_Encantado = 0,
    Sabor_Inferior = 0,
    Sabor_Superior = 0,
    Relacion_Masa = "---",
    Ancho_Desintegracion = "---",
    Decaimientos = "---",
)

Strange = Quarks(
    Carga_Electrica = "- 1/3",
    Masa = "93.5 ± 0.8",
    Isospin = "I = 0", 
    Sabor_Extraño = -1,
    Sabor_Encantado = 0,
    Sabor_Inferior = 0,
    Sabor_Superior = 0,
    Relacion_Masa = "m_s / m_d = 17 a 22",
    Ancho_Desintegracion = "---",
    Decaimientos = "---",
)

Charm = Quarks(
    Carga_Electrica = "+ 2/3",
    Masa = "1273 ± 4.6",
    Isospin = "I = 0", 
    Sabor_Extraño = 0,
    Sabor_Encantado = 1,
    Sabor_Inferior = 0,
    Sabor_Superior = 0,
    Relacion_Masa = "m_c - m_b = 3.45 ± 0.05 GeV",
    Ancho_Desintegracion = "---",
    Decaimientos = "---",
)

Bottom = Quarks(
    Carga_Electrica = "- 1/3",
    Masa = "4183 ± 7",
    Isospin = "I = 0", 
    Sabor_Extraño = 0,
    Sabor_Encantado = 0,
    Sabor_Inferior = -1,
    Sabor_Superior = 0,
    Relacion_Masa = "---",
    Ancho_Desintegracion = "---",
    Decaimientos = "---",
)

Top = Quarks(
    Carga_Electrica = "+ 2/3",
    Masa = "172.57 ± 0.29 GeV",
    Isospin = "I = 0", 
    Sabor_Extraño = 0,
    Sabor_Encantado = 0,
    Sabor_Inferior = 0,
    Sabor_Superior = 1,
    Relacion_Masa = "---",
    Ancho_Desintegracion = "1.42_{-0.15}^{+0.19} GeV",
    Decaimientos = "Wq(q=b,s,d) 66.5%",
)