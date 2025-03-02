from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import numpy as np

class EquationSolver(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Título de la aplicación
        self.title_label = Label(text="Espoachan Calculator 2.0 Deluxe Special Edition", font_size=24, size_hint=(1, 0.1))
        self.add_widget(self.title_label)
        
        # Instrucciones
        self.instructions_label = Label(text="Ingresa los coeficientes de las ecuaciones lineales.", font_size=18, size_hint=(1, 0.1))
        self.add_widget(self.instructions_label)

        # Crear los campos de entrada para dos ecuaciones lineales con dos variables
        self.inputs = []
        labels = [
            ("A1 (Coeficiente de X en la 1ª ecuación):", "Coeficiente de X en la primera ecuación"),
            ("B1 (Coeficiente de Y en la 1ª ecuación):", "Coeficiente de Y en la primera ecuación"),
            ("C1 (Constante de la 1ª ecuación):", "Constante de la primera ecuación"),
            ("A2 (Coeficiente de X en la 2ª ecuación):", "Coeficiente de X en la segunda ecuación"),
            ("B2 (Coeficiente de Y en la 2ª ecuación):", "Coeficiente de Y en la segunda ecuación"),
            ("C2 (Constante de la 2ª ecuación):", "Constante de la segunda ecuación")
        ]
        
        for lbl, hint in labels:
            row = BoxLayout()
            row.add_widget(Label(text=lbl, size_hint=(0.5, 1)))
            input_field = TextInput(multiline=False, input_filter='float', hint_text=hint)
            row.add_widget(input_field)
            self.inputs.append(input_field)
            self.add_widget(row)
        
        # Botón para resolver
        self.solve_button = Button(text='Resolver Sistema', size_hint=(1, 0.2))
        self.solve_button.bind(on_press=self.solve_equations)
        self.add_widget(self.solve_button)
        
        # Etiqueta para mostrar el resultado
        self.result_label = Label(text='', size_hint=(1, 0.2))
        self.add_widget(self.result_label)
    
    def solve_equations(self, instance):
        try:
            # Obtener los valores de los campos
            a1, b1, c1, a2, b2, c2 = [float(i.text) for i in self.inputs]
            A = np.array([[a1, b1], [a2, b2]])  # Matriz de coeficientes
            B = np.array([c1, c2])  # Matriz de constantes
            solution = np.linalg.solve(A, B)  # Resolver el sistema de ecuaciones
            # Mostrar los resultados
            self.result_label.text = f"X = {solution[0]:.2f}, Y = {solution[1]:.2f}"
        except Exception as e:
            # Si ocurre un error, mostrar mensaje
            self.result_label.text = "Error: Verifica los valores y las ecuaciones"

class EquationApp(App):
    def build(self):
        return EquationSolver()

if __name__ == '__main__':
    EquationApp().run()
