import serial

serialPort = serial.Serial(
    port="COM4",
    baudrate=9600,
    bytesize=8,
    timeout=2,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_EVEN
)

def print_colored_text(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    reset_color = '\033[0m'
    colored_text = colors[color] + text + reset_color
    return colored_text

def print_menu():
    menu = "\033[2J\033[HMenu:\r\n"
    menu += print_colored_text("1. Option 1", "red") + "\r\n"
    menu += print_colored_text("2. Option 2", "green") + "\r\n"
    menu += print_colored_text("3. Option 3", "yellow") + "\r\n"
    menu += print_colored_text("4. Exit", "blue") + "\r\n"
    serialPort.write(menu.encode('ISO-8859-1'))

def handle_input(serialString):
    print(f"Received: {serialString}")
    if serialString == "1":
        serialPort.write("You selected option 1\n".encode('ascii', 'ignore'))
    elif serialString == "2":
        serialPort.write("You selected option 2\n".encode('ascii', 'ignore'))
    elif serialString == "3":
        serialPort.write("You selected option 3\n".encode('ascii', 'ignore'))
    elif serialString == "4":
        serialPort.write("Exiting...\n".encode('ascii', 'ignore'))
        return False
    else:
        serialPort.write("Invalid input. Please try again.\n".encode('ascii', 'ignore'))
    return True

print_menu()
while 1:
    if serialPort.in_waiting > 0:
        serialString = serialPort.readline().decode('ascii', 'ignore').strip()
        if not handle_input(serialString):
            break
        print_menu()