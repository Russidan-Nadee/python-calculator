# Advanced Calculator

A modern calculator application built with Python Tkinter, featuring comprehensive mathematical functions and a sleek dark interface.

## Features

### Basic Operations
- Arithmetic operations: `+`, `-`, `×`, `÷`
- Exponentiation: `x²`, `x^y`
- Square root: `√`
- Reciprocal: `1/x`
- Percentage: `%`
- Parentheses support

### Scientific Functions
- Trigonometric: `sin`, `cos`, `tan`
- Logarithmic: `log` (base 10), `ln` (natural)
- Mathematical constant: `π`
- Angle modes: Degrees (`DEG`) / Radians (`RAD`)

### Memory Operations
- `MC` - Memory Clear
- `MR` - Memory Recall  
- `M+` - Memory Add
- `M-` - Memory Subtract

### User Interface
- Large, clear display (32pt font)
- Calculation history (last 5 operations)
- Dark theme with orange accents
- Responsive button layout

## Requirements

- **Python 3.6+** (tested with 3.13.5)
- **tkinter** (included with Python)
- **Windows/macOS/Linux**

## Installation & Usage

### Quick Start
```bash
# Clone or download the project
# Navigate to project directory
cd calculator_intern_test

# Run the application
py calculator.py          # Windows
python3 calculator.py     # macOS/Linux
```

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `0-9` | Numbers |
| `+` `-` `*` `/` | Operations |
| `Enter` `=` | Calculate |
| `Backspace` | Delete |
| `Delete` `C` | Clear |
| `Escape` | Clear entry |
| `P` | Insert π |

## Usage Examples

```
Basic: 15 + 25 = 40
Powers: 2^8 = 256
Trig: sin(30) = 0.5 (in DEG mode)
Mixed: 2π + sqrt(16) = 10.283
Complex: (8+5)×sin(45) = 9.192
```

## Advanced Features

### Implicit Multiplication
Automatically inserts multiplication operators:
- `2π` becomes `2 × π`
- `8sin(30)` becomes `8 × sin(30)`
- `(2+3)(4+5)` becomes `(2+3) × (4+5)`

### Error Handling
- Invalid expressions show "Error"
- Division by zero protection
- Automatic recovery from errors

### Smart Display
- Scientific notation for very large/small numbers
- Rounds near-zero values to zero
- Truncates long expressions with "..."

## File Structure

```
calculator.py    # Main application (400+ lines)
README.md       # Documentation
```

## Technical Details

### Architecture
- Single-class design (`AdvancedCalculator`)
- Event-driven GUI with tkinter
- Safe expression evaluation
- Comprehensive error handling

### Color Scheme
```python
colors = {
    'bg': '#1e1e1e',        # Dark background
    'accent': '#e97b47',    # Orange accent
    'text': '#ffffff',      # White text
    'button_bg': '#3d3d3d'  # Button background
}
```

## Troubleshooting

**Python not found**
```bash
# Check installation
py --version
python --version
python3 --version
```

**Import errors**
- tkinter is included with Python
- On Linux: `sudo apt-get install python3-tk`

**File issues**
- Ensure filename is `calculator.py` (not `caculator.py`)
- Check file permissions

## License

Open source project for educational and personal use.

## Developer

**Russidan Nadee**  

---
*Version 1.0 • July 2025*
