class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("\n🔥 Начало битвы героев! 🔥")
        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print("\n" + "=" * 30)
            print(f"⚔️ Раунд {round_num} ⚔️")

            # Ход игрока
            self.player.attack(self.computer)
            print(
                f"{self.player.name} атаковал {self.computer.name}. "
                f"Здоровье {self.computer.name}: {max(0, self.computer.health)}"
            )
            if not self.computer.is_alive():
                print(f"\n💀 {self.computer.name} повержен! {self.player.name} одержал победу! 🏆")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(
                f"{self.computer.name} атаковал {self.player.name}. "
                f"Здоровье {self.player.name}: {max(0, self.player.health)}"
            )
            if not self.player.is_alive():
                print(f"\n💀 {self.player.name} повержен! {self.computer.name} одержал победу! 🏆")
                break

            round_num += 1


if __name__ == "__main__":
    game = Game()
    game.start()