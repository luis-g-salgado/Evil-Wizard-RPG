import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.is_defending = False  # Track if the character is using a defense ability

    def attack(self, opponent):
        damage = self.attack_power
        if opponent.is_defending:
            return
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 40)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def reset_defense(self):
        self.is_defending = False


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=35)

    def special_ability_1(self, opponent):
        # Warrior's first special ability: "Rage Strike" (increased damage)
        damage = random.randint(40,60)
        opponent.health -= damage
        print(f"{self.name} uses Rage Strike! Deals {damage} damage!")

    def special_ability_2(self, opponent):
        # Warrior's second special ability: "Battle Roar" (stuns opponent, reducing their next attack)
        print(f"{self.name} uses Battle Roar! {opponent.name} is stunned and their next attack will be weaker!")
        opponent.attack_power = max(0, opponent.attack_power - 10)  # Reduce opponent's attack power for next turn


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)

    def special_ability_1(self, opponent):
        # Mage's first special ability: "Fireball" (high damage)
        damage = random.randint(45, 55)
        opponent.health -= damage
        print(f"{self.name} casts Fireball! Deals {damage} damage!")

    def special_ability_2(self, opponent):
        # Mage's second special ability: "Mana Shield" (reduces damage from next attack)
        print(f"{self.name} casts Mana Shield! The next attack will deal reduced damage.")
        opponent.attack_power = max(0, opponent.attack_power - 10)  # Reduce opponent's attack power for next turn


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.max_health = 200

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health  # Cap health to max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    def special_ability_1(self, opponent):
        # Archer's first special ability: "Quick Shot" (double attack)
        damage = random.randint(35, 45)
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot! Deals {damage} damage!")
        damage = random.randint(20,30)
        opponent.health -= damage
        print(f"{self.name} shoots again with Quick Shot! Deals {damage} damage!")

    def special_ability_2(self):
     # Archer's special ability: "Evade" (avoid the next attack)
        self.is_defending = True
        print(f"{self.name} uses Evade and will avoid the next attack!")
       

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)

    def special_ability_1(self, opponent):
        # Paladin's first special ability: "Holy Strike" (bonus damage)
        damage = random.randint(30, 40)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike! Deals {damage} damage!")

    def special_ability_2(self):
    # Paladin's defense ability: "Divine Shield" (blocks the next attack)
        self.is_defending = True
        print(f"{self.name} activates Divine Shield! Will block the next attack.")       


# Create Character function with class selection
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
    # Save the opponent's original attack power
        original_attack_power = wizard.attack_power

        choice = input("Choose an action: ")
        if choice == '1':
                player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                print("1. Rage Strike")
                print("2. Battle Roar")
            elif isinstance(player, Mage):
                print("1. Fireball Spell")
                print("2. Mana Shield")
            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Devine Shield")

            ability_choice = input("Choose a special ability: ")

            if isinstance(player, Warrior):
                if ability_choice == '1':
                    player.special_ability_1(wizard)
                elif ability_choice == '2':
                    player.special_ability_2(wizard)
            elif isinstance(player, Mage):
                if ability_choice == '1':
                    player.special_ability_1(wizard)
                elif ability_choice == '2':
                    player.special_ability_2(wizard)
            elif isinstance(player, Archer):
                if ability_choice == '1':
                    player.special_ability_1(wizard)
                elif ability_choice == '2':
                    player.special_ability_2()
            elif isinstance(player, Paladin):
                if ability_choice == '1':
                    player.special_ability_1(wizard)
                elif ability_choice == '2':
                    player.special_ability_2()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        
        if wizard.health > 0:
            wizard.regenerate()
            if player.is_defending:
                print(f"{player.name} successfully avoids the attack!")
                player.reset_defense()
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!"
                  "\nDEFEAT!! ☠️")
            

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!"
              "\nVICTORY!! 🥳")
            break 
    
    
    # Restore the opponent's original attack power after the player's turn
        wizard.attack_power = original_attack_power
        
        
# Main function
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
