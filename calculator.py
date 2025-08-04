class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def register(self, event, handler):
        self.handlers[event] = handler

    def dispatch(self, event, *args):
        return self.handlers.get(event, lambda *_: "Unknown operation")(*args)


def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero." if y == 0 else x / y


def print_menu():
    bar = "=" * 40
    print(f"\n{bar}")
    print("           CLI CALCULATOR")
    print(bar)
    print(" 1 ➤ Add\n 2 ➤ Subtract\n 3 ➤ Multiply\n 4 ➤ Divide\n 5 ➤ Exit")
    print(bar)


def main():
    dispatcher = EventDispatcher()
    dispatcher.register("1", add)
    dispatcher.register("2", subtract)
    dispatcher.register("3", multiply)
    dispatcher.register("4", divide)

    while True:
        print_menu()
        choice = input(" Select operation (1–5): ").strip()

        if choice == "5":
            print("\n Session ended. 🚀")
            break

        if choice in dispatcher.handlers:
            try:
                x = float(input(" Enter first number: "))
                y = float(input(" Enter second number: "))
            except ValueError:
                print(" Error: Invalid numeric input.")
                continue

            result = dispatcher.dispatch(choice, x, y)
            print(" ➤ Result:", result)
        else:
            print(" Error: Invalid selection. Try again.")

if __name__ == "__main__":
    main()
