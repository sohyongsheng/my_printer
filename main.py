from my_printer.printer import NamedPrinter

if __name__ == '__main__':
    printer = NamedPrinter("James", "Bond")
    printer.print_name()
    printer.print_msg("Hello world!")
