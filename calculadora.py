import tkinter as tk
import re

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("520x460")
        self.root.resizable(0, 0)
        
        self.expresion = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        input_frame = tk.Frame(
            self.root, 
            width=300, 
            height=150, 
            bd=0, 
            highlightbackground="black", 
            highlightcolor="black", 
            highlightthickness=1
        )
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(
            input_frame,
            font=('arial', 18, 'bold'), 
            textvariable=self.input_text, 
            width=150, 
            bg="#eee", 
            bd=0, 
            justify=tk.RIGHT
        )
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()
        
        self.create_buttons(btns_frame)
        
    def create_buttons(self, frame):
        # Define los colores para cada grupo de botones
        color_operadores = "#45EA6E"   # Verde claro
        color_especiales = "#BA0000"   # Rojo
        color_numericos  = "#AAB7B8"   # Gris
        
        # Grupos de botones
        operadores = {'+', '-', '*', '/', '=', '%'}
        especiales = {'EXIT', 'C', '←'}
        
        buttons = [
            ('←',    1, 0, 1),
            ('%',    1, 1, 1),
            ('EXIT', 1, 2, 1),
            ('C',    1, 3, 1),
            ('7',    2, 0, 1),
            ('8',    2, 1, 1),
            ('9',    2, 2, 1),
            ('*',    2, 3, 1),
            ('4',    3, 0, 1),
            ('5',    3, 1, 1),
            ('6',    3, 2, 1),
            ('-',    3, 3, 1),
            ('1',    4, 0, 1),
            ('2',    4, 1, 1),
            ('3',    4, 2, 1),
            ('+',    4, 3, 1),
            ('0',    5, 0, 1),
            ('.',    5, 1, 1),
            ('=',    5, 2, 1),
            ('/',    5, 3, 1)
        ]
        
        for text, row, col, colspan in buttons:
            if text in operadores:
                btn_color = color_operadores
            elif text in especiales:
                btn_color = color_especiales
            else:
                btn_color = color_numericos
            
            button = tk.Button(
                frame,
                text=text,
                fg="black",
                width=10,
                height=3,
                bd=0,
                bg=btn_color,
                cursor="hand2",
                font=('arial', 14, 'bold'),
                command=lambda t=text: self.exit_app() if t == 'EXIT' else self.on_button_click(t)
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1)

    def exit_app(self):
        self.root.destroy()
    
    def calculate_percentage(self, expression: str) -> str:
        """
        1) Reemplaza todas las secuencias de la forma:
             X [+,-,*,/] Y%
           según las reglas:
             - +, - => X op (X*(Y/100))
             - *, / => X op (Y/100)

        2) Luego, convierte cualquier número con % suelto (sin operador a la izquierda),
           por ej. "20%", en "(20/100)".
        
        De este modo se obtienen resultados como:
          40-20%   =>  40-(40*(20/100)) = 32
          100+10%  =>  100+(100*(10/100)) = 110
          90*6%    =>  90*(6/100) = 5.4
          90/9%    =>  90/(9/100) = 1000
          20%+30   =>  (20/100)+30 = 30.2
        """

        # 1) Manejo de "X op Y%"
        pattern_op = re.compile(r'(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)(%)')

        def replace_op_percent(m):
            x = m.group(1)    # número antes del operador
            op = m.group(2)   # operador: + - * /
            y = m.group(3)    # número antes del %
            # m.group(4) es '%'

            if op in ['+', '-']:
                # X +/- Y% => X op (X*(Y/100))
                return f"{x}{op}({x}*({y}/100))"
            else:
                # X */ Y% => X op (Y/100)
                return f"{x}{op}({y}/100)"

        new_expr = expression
        while True:
            transformed = pattern_op.sub(replace_op_percent, new_expr)
            if transformed == new_expr:
                break
            new_expr = transformed

        # 2) Manejo de porcentajes "sueltos"
        pattern_suelto = re.compile(r'(\d+(?:\.\d+)?)%')
        def replace_suelto(m):
            num = m.group(1)
            return f"({num}/100)"

        new_expr = pattern_suelto.sub(replace_suelto, new_expr)
        
        return new_expr

    def on_button_click(self, char):
        if char == 'C':
            # Limpia la expresión
            self.expresion = ""
            self.input_text.set("")
        elif char == '←':
            # Borra el último caracter
            self.expresion = self.expresion[:-1]
            self.input_text.set(self.expresion)
        elif char == '=':
            try:
                transformed_expr = self.calculate_percentage(self.expresion)
                result = str(eval(transformed_expr))
                self.input_text.set(result)
                self.expresion = result
            except:
                self.input_text.set("Error")
                self.expresion = ""
        else:
            self.expresion += str(char)
            self.input_text.set(self.expresion)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
