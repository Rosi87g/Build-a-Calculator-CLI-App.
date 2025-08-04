class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def register(self, event, handler):
        self.handlers[event] = handler

    def dispatch(self, event, *args):
        if event in self.handlers:
            return self.handlers[event](*args)
        return "Unknown operation"


def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero." if y == 0 else x / y


def print_menu():
    border = "=" * 32
    print(f"\n{border}")
    print("      CLI CALCULATOR")
    print(border)
    print(" 1 → Add")
    print(" 2 → Subtract")
    print(" 3 → Multiply")
    print(" 4 → Divide")
    print(" 5 → Exit")
    print(border)


def main():
    dispatcher = EventDispatcher()
    dispatcher.register("1", add)
    dispatcher.register("2", subtract)
    dispatcher.register("3", multiply)
    dispatcher.register("4", divide)

    while True:
        print_menu()
        choice = input(" Select operation (1–5): ")

        if choice == '5':
            print("\n Session ended. 🚀")
            break

        if choice in dispatcher.handlers:
            try:
                x = float(input(" Enter first number: "))
                y = float(input(" Enter second number: "))
            except ValueError:
                print(" Error: Please enter valid numbers.")
                continue

            result = dispatcher.dispatch(choice, x, y)
            print(" Result →", result)
        else:
            print(" Error: Invalid selection.")


if __name__ == "__main__":
    main()
