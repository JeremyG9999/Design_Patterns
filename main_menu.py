import os
import time
from scripts.observer_pattern import ObserverPattern
from scripts.state_pattern import StatePattern
from scripts.strategy_pattern import StrategyPattern
from scripts.adapter_pattern import AdapterPattern
from scripts.builder_pattern import BuilderPattern
from scripts.factory_pattern import FactoryPattern
from scripts.singleton_pattern import SingletonPattern

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a design pattern demo:")
            print("1. Observer Pattern")
            print("2. State Pattern")
            print("3. Strategy Pattern")
            print("4. Adapter Pattern")
            print("5. Builder Pattern")
            print("6. Factory Pattern")
            print("7. Singleton Pattern")
            print("8. Clear Terminal")
            print("9. Exit")
            option = input("Enter your choice: ")
            if option == "1":
                self.cls()
                ObserverPattern.main()
            elif option == "2":
                self.cls()
                StatePattern.main()
            elif option == "3":
                self.cls()
                StrategyPattern.main()
            elif option == "4":
                self.cls()
                AdapterPattern.main()
            elif option == "5":
                self.cls()
                BuilderPattern.main()
            elif option == "6":
                self.cls()
                FactoryPattern.main()
            elif option == "7":
                self.cls()
                SingletonPattern.main()
            elif option == "8":
                self.cls()
            elif option == "9":
                break
            else:
                print("Invalid choice.")

    def cls(self):
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()
