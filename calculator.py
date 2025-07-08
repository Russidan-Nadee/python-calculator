import tkinter as tk
from tkinter import ttk, messagebox
import math
import re
from typing import List, Union
from fractions import Fraction
import operator

class AdvancedCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Calculator - Claude.AI Style")
        self.root.geometry("500x700")
        self.root.configure(bg='#1e1e1e')
        
        # Claude.AI Color Scheme
        self.colors = {
            'bg': '#1e1e1e',
            'secondary_bg': '#2d2d2d',
            'accent': '#e97b47',  # Claude orange
            'text': '#ffffff',
            'text_secondary': '#cccccc',
            'button_bg': '#3d3d3d',
            'button_hover': '#4d4d4d',
            'special_button': '#e97b47',
            'error': '#ff6b6b'
        }
        
        # Variables
        self.current_expression = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.history = []
        self.memory = 0
        self.angle_mode = "deg"  # deg or rad
        
        # Mathematical operations mapping
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod
        }
        
        self.setup_ui()
        self.setup_keyboard_bindings()
        
    def setup_ui(self):
        # Configure grid
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        
        # Display Frame
        display_frame = tk.Frame(self.root, bg=self.colors['bg'])
        display_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        
        # Main Display
        self.display_label = tk.Label(
            display_frame, 
            textvariable=self.display_var,
            font=("SF Pro Display", 32, "bold"),
            bg=self.colors['secondary_bg'],
            fg=self.colors['text'],
            anchor="e",
            padx=15,
            pady=10
        )
        self.display_label.pack(fill="both", expand=True)
        
        # History Frame
        history_frame = tk.Frame(self.root, bg=self.colors['bg'])
        history_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=(0, 10), sticky="nsew")
        
        # History Display
        self.history_label = tk.Label(
            history_frame,
            text="History: Empty",
            font=("SF Pro Display", 12),
            bg=self.colors['secondary_bg'],
            fg=self.colors['text_secondary'],
            anchor="w",
            padx=15,
            pady=5
        )
        self.history_label.pack(fill="both", expand=True)
        
        # Button Layout
        self.create_buttons()
        
        # Create large equals button separately
        self.create_large_equals_button()
        
    def create_buttons(self):
        # Button configurations: (text, row, col, colspan, style, command)
        buttons = [
            # Row 2 - Memory and Mode
            ("MC", 2, 0, 1, "memory", self.memory_clear),
            ("MR", 2, 1, 1, "memory", self.memory_recall),
            ("M+", 2, 2, 1, "memory", self.memory_add),
            ("M-", 2, 3, 1, "memory", self.memory_subtract),
            ("DEG", 2, 4, 1, "mode", self.toggle_angle_mode),
            
            # Row 3 - Advanced Functions
            ("sin", 3, 0, 1, "function", lambda: self.add_function("sin")),
            ("cos", 3, 1, 1, "function", lambda: self.add_function("cos")),
            ("tan", 3, 2, 1, "function", lambda: self.add_function("tan")),
            ("log", 3, 3, 1, "function", lambda: self.add_function("log")),
            ("ln", 3, 4, 1, "function", lambda: self.add_function("ln")),
            
            # Row 4 - More Functions
            ("√", 4, 0, 1, "function", lambda: self.add_function("sqrt")),
            ("x²", 4, 1, 1, "function", lambda: self.add_operator("**2")),
            ("x^y", 4, 2, 1, "function", lambda: self.add_operator("**")),
            ("1/x", 4, 3, 1, "function", self.reciprocal),
            ("π", 4, 4, 1, "function", lambda: self.add_number(str(math.pi))),
            
            # Row 5 - Clear and Backspace
            ("C", 5, 0, 1, "clear", self.clear_all),
            ("CE", 5, 1, 1, "clear", self.clear_entry),
            ("⌫", 5, 2, 1, "clear", self.backspace),
            ("%", 5, 3, 1, "operator", lambda: self.add_operator("%")),
            ("/", 5, 4, 1, "operator", lambda: self.add_operator("/")),
            
            # Row 6 - Numbers
            ("7", 6, 0, 1, "number", lambda: self.add_number("7")),
            ("8", 6, 1, 1, "number", lambda: self.add_number("8")),
            ("9", 6, 2, 1, "number", lambda: self.add_number("9")),
            ("×", 6, 3, 1, "operator", lambda: self.add_operator("*")),
            ("(", 6, 4, 1, "operator", lambda: self.add_operator("(")),
            
            # Row 7 - Numbers
            ("4", 7, 0, 1, "number", lambda: self.add_number("4")),
            ("5", 7, 1, 1, "number", lambda: self.add_number("5")),
            ("6", 7, 2, 1, "number", lambda: self.add_number("6")),
            ("-", 7, 3, 1, "operator", lambda: self.add_operator("-")),
            (")", 7, 4, 1, "operator", lambda: self.add_operator(")")),
            
            # Row 8 - Numbers and operators
            ("1", 8, 0, 1, "number", lambda: self.add_number("1")),
            ("2", 8, 1, 1, "number", lambda: self.add_number("2")),
            ("3", 8, 2, 1, "number", lambda: self.add_number("3")),
            ("+", 8, 3, 1, "operator", lambda: self.add_operator("+")),
            ("=", 8, 4, 1, "equals", self.calculate),
            
            # Row 9 - Zero and decimal with extended equals
            ("0", 9, 0, 2, "number", lambda: self.add_number("0")),
            (".", 9, 2, 1, "number", lambda: self.add_number(".")),
            ("±", 9, 3, 1, "operator", self.toggle_sign),
            ("=", 9, 4, 1, "equals", self.calculate),
        ]
        
        # Create buttons
        for button_config in buttons:
            text, row, col, colspan, style, command = button_config
            
            btn = tk.Button(
                self.root,
                text=text,
                command=command,
                font=("SF Pro Display", 16, "bold"),
                **self.get_button_style(style)
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=3, pady=3, sticky="nsew")
    
    def create_large_equals_button(self):
        """Create large equals button spanning 2 rows"""
        equals_btn = tk.Button(
            self.root,
            text="=",
            command=self.calculate,
            font=("SF Pro Display", 20, "bold"),
            **self.get_button_style("equals")
        )
        equals_btn.grid(row=8, column=4, rowspan=2, padx=3, pady=3, sticky="nsew")
            
    def get_button_style(self, style: str) -> dict:
        """Get button styling based on button type"""
        base_style = {
            'relief': 'flat',
            'borderwidth': 0,
            'cursor': 'hand2'
        }
        
        styles = {
            'number': {
                'bg': self.colors['button_bg'],
                'fg': self.colors['text'],
                'activebackground': self.colors['button_hover'],
                'activeforeground': self.colors['text']
            },
            'operator': {
                'bg': self.colors['accent'],
                'fg': 'white',
                'activebackground': '#d66b3c',
                'activeforeground': 'white'
            },
            'equals': {
                'bg': self.colors['accent'],
                'fg': 'white',
                'activebackground': '#d66b3c',
                'activeforeground': 'white'
            },
            'function': {
                'bg': self.colors['button_bg'],
                'fg': self.colors['accent'],
                'activebackground': self.colors['button_hover'],
                'activeforeground': self.colors['accent']
            },
            'clear': {
                'bg': '#ff6b6b',
                'fg': 'white',
                'activebackground': '#ff5252',
                'activeforeground': 'white'
            },
            'memory': {
                'bg': self.colors['button_bg'],
                'fg': self.colors['text_secondary'],
                'activebackground': self.colors['button_hover'],
                'activeforeground': self.colors['text_secondary']
            },
            'mode': {
                'bg': self.colors['button_bg'],
                'fg': self.colors['accent'],
                'activebackground': self.colors['button_hover'],
                'activeforeground': self.colors['accent']
            }
        }
        
        return {**base_style, **styles.get(style, styles['number'])}
    
    def add_number(self, number: str):
        """Add number to expression"""
        if self.current_expression == "0" or self.display_var.get() == "Error":
            self.current_expression = number
        else:
            self.current_expression += number
        self.update_display()
    
    def add_operator(self, operator: str):
        """Add operator to expression"""
        if self.current_expression and self.current_expression[-1] not in "+-*/()":
            self.current_expression += operator
        elif operator in "()":
            self.current_expression += operator
        self.update_display()
    
    def add_function(self, function: str):
        """Add mathematical function"""
        if self.current_expression == "0":
            self.current_expression = f"{function}("
        else:
            self.current_expression += f"{function}("
        self.update_display()
    
    def clear_all(self):
        """Clear everything"""
        self.current_expression = ""
        self.display_var.set("0")
    
    def clear_entry(self):
        """Clear current entry"""
        self.current_expression = ""
        self.display_var.set("0")
    
    def backspace(self):
        """Remove last character"""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            if not self.current_expression:
                self.display_var.set("0")
            else:
                self.update_display()
    
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        if self.current_expression:
            try:
                result = self.safe_eval(self.current_expression)
                self.current_expression = str(-result)
                self.update_display()
            except:
                pass
    
    def reciprocal(self):
        """Calculate reciprocal (1/x)"""
        if self.current_expression:
            try:
                result = self.safe_eval(self.current_expression)
                if result != 0:
                    self.current_expression = str(1 / result)
                    self.update_display()
                else:
                    self.display_var.set("Error")
            except:
                self.display_var.set("Error")
    
    def calculate(self):
        """Perform calculation"""
        if not self.current_expression:
            return
        
        try:
            # Replace display symbols with actual operators
            expression = self.current_expression.replace("×", "*").replace("÷", "/")
            
            # Handle mathematical functions
            result = self.safe_eval(expression)
            
            # Add to history
            self.history.append(f"{self.current_expression} = {result}")
            if len(self.history) > 5:
                self.history.pop(0)
            
            # Update display
            self.current_expression = str(result)
            self.update_display()
            self.update_history()
            
        except Exception as e:
            self.display_var.set("Error")
            self.current_expression = ""
    
    def safe_eval(self, expression: str) -> float:
        """Safely evaluate mathematical expression"""
        # Replace mathematical functions
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("sqrt", "math.sqrt")
        
        # Handle angle conversion for trigonometric functions
        if self.angle_mode == "deg":
            expression = re.sub(r'math\.(sin|cos|tan)\((.*?)\)', 
                              r'math.\1(math.radians(\2))', expression)
        
        # Safe evaluation with limited scope
        allowed_names = {
            "__builtins__": {},
            "math": math,
        }
        
        try:
            return eval(expression, allowed_names)
        except:
            raise ValueError("Invalid expression")
    
    def update_display(self):
        """Update main display"""
        if self.current_expression:
            self.display_var.set(self.current_expression)
        else:
            self.display_var.set("0")
    
    def update_history(self):
        """Update history display"""
        if self.history:
            self.history_label.config(text=f"History: {self.history[-1]}")
        else:
            self.history_label.config(text="History: Empty")
    
    def toggle_angle_mode(self):
        """Toggle between degrees and radians"""
        self.angle_mode = "rad" if self.angle_mode == "deg" else "deg"
        # Update button text
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget('text') in ['DEG', 'RAD']:
                widget.config(text=self.angle_mode.upper())
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
    
    def memory_recall(self):
        """Recall memory value"""
        self.current_expression = str(self.memory)
        self.update_display()
    
    def memory_add(self):
        """Add current value to memory"""
        if self.current_expression:
            try:
                value = self.safe_eval(self.current_expression)
                self.memory += value
            except:
                pass
    
    def memory_subtract(self):
        """Subtract current value from memory"""
        if self.current_expression:
            try:
                value = self.safe_eval(self.current_expression)
                self.memory -= value
            except:
                pass
    
    def setup_keyboard_bindings(self):
        """Setup keyboard shortcuts"""
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
    
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        
        # Numbers and operators
        if key.isdigit():
            self.add_number(key)
        elif key in '+-*/()':
            self.add_operator(key)
        elif key == '.':
            self.add_number('.')
        elif key == '=' or event.keysym == 'Return':
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Delete' or key.lower() == 'c':
            self.clear_all()
        elif event.keysym == 'Escape':
            self.clear_entry()
    
    def run(self):
        """Start the calculator"""
        self.root.mainloop()

# Create and run calculator
if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.run()