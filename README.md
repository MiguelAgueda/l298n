# l298n Module
This module is designed to be used with two GPIO pins on the Raspberry Pi.

## Usage
First, create an instance of l298n using 2 pin numbers from the board as 
attributes. Use the GPIO number as opposed to the board number.

```python
from l298n import l298n
motor = l298n(2, 3)
```

Then, using methods from l298n, a motor can be activated in the desired direction.
```python
motor.forwards()
motor.backwards()
motor.stop()
```

## Contributions
If you see areas for improvement in this module, please submit an issue or 
feel free to email me. All contributions are welcome.
