from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz Gráfica - First Package")
        self.setGeometry(100, 100, 600, 400)

        # Crear layout principal
        layout = QVBoxLayout()

        # Área de texto para mostrar la información
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Botón para Leptones
        lepton_button = QPushButton("Ver Leptones")
        lepton_button.clicked.connect(self.show_lepton_info)
        layout.addWidget(lepton_button)

        # Botón para Neutrinos
        neutrino_button = QPushButton("Ver Neutrinos")
        neutrino_button.clicked.connect(self.show_neutrino_info)
        layout.addWidget(neutrino_button)

        # Botón para Quarks
        quark_button = QPushButton("Ver Quarks")
        quark_button.clicked.connect(self.show_quark_info)
        layout.addWidget(quark_button)

        # Botón para Bosones
        boson_button = QPushButton("Ver Bosones")
        boson_button.clicked.connect(self.show_boson_info)
        layout.addWidget(boson_button)

        # Widget principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def format_particle_properties(self, particle):
        """Devuelve una cadena con todas las propiedades de la partícula."""
        properties = vars(particle)  # Obtiene todas las propiedades de la instancia
        info = f"Tipo: {particle.type}\n"
        for prop, value in properties.items():
            info += f"{prop}: {value}\n"
        return info

    def show_lepton_info(self):
        from First_Package.module1 import Electron, Muon, Tau
        info = "Información de Leptones:\n\n"
        info += "Electrón:\n" + self.format_particle_properties(Electron) + "\n"
        info += "Muón:\n" + self.format_particle_properties(Muon) + "\n"
        info += "Tau:\n" + self.format_particle_properties(Tau) + "\n"
        self.text_area.setText(info)

    def show_neutrino_info(self):
        from First_Package.module2 import Neutrino_Electron, Neutrino_Muon, Neutrino_Tau
        info = "Información de Neutrinos:\n\n"
        info += "Neutrino Electrónico:\n" + self.format_particle_properties(Neutrino_Electron) + "\n"
        info += "Neutrino Muónico:\n" + self.format_particle_properties(Neutrino_Muon) + "\n"
        info += "Neutrino Tauónico:\n" + self.format_particle_properties(Neutrino_Tau) + "\n"
        self.text_area.setText(info)

    def show_quark_info(self):
        from First_Package.module3 import Up, Down, Strange, Charm, Bottom, Top
        info = "Información de Quarks:\n\n"
        info += "Up:\n" + self.format_particle_properties(Up) + "\n"
        info += "Down:\n" + self.format_particle_properties(Down) + "\n"
        info += "Strange:\n" + self.format_particle_properties(Strange) + "\n"
        info += "Charm:\n" + self.format_particle_properties(Charm) + "\n"
        info += "Bottom:\n" + self.format_particle_properties(Bottom) + "\n"
        info += "Top:\n" + self.format_particle_properties(Top) + "\n"
        self.text_area.setText(info)

    def show_boson_info(self):
        from First_Package.module4 import Foton, Gluon, W, Z, Higgs
        info = "Información de Bosones:\n\n"
        info += "Fotón:\n" + self.format_particle_properties(Foton) + "\n"
        info += "Gluón:\n" + self.format_particle_properties(Gluon) + "\n"
        info += "Bosón W:\n" + self.format_particle_properties(W) + "\n"
        info += "Bosón Z:\n" + self.format_particle_properties(Z) + "\n"
        info += "Bosón de Higgs:\n" + self.format_particle_properties(Higgs) + "\n"
        self.text_area.setText(info)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
