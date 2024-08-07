# pynput

- pynput.mouse
    - Contains classes for controlling and monitoring a mouse or trackpad.
- pynput.keyboard
    - Contains classes for controlling and monitoring the keyboard.

```python
from pynput import mouse, keyboard
```

## Handling the mouse

### Controlling the mouse

```python
from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
```

### Monitoring the mouse

```python
from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

# Collect events until released
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()
```
