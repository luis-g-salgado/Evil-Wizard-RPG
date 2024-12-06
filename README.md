# Fantasy Battle Game

This is a simple text-based RPG where you can choose a character class and battle against an Evil Wizard.
The game includes various character classes with unique abilities, and the player can perform actions such as attacking, using special abilities, healing, and viewing stats.

## Features

- **Character Classes**: Choose from Warrior, Mage, Archer, or Paladin.
- **Battle System**: Turn-based combat with an Evil Wizard.
- **Special Abilities**: Each character has unique special abilities that can be used during battle.
- **Healing**: Characters can heal themselves during battle.
- **Dynamic AI**: The Evil Wizard regenerates health after each turn and can handle. Damage is reduced or negated when certain 'special abilities' are used by the player.
- **Victory/Defeat**: Win by defeating the Evil Wizard, or lose if your character’s health reaches 0.

### `Characters`

- **Warrior**: A Strong fighter that has unique abilities such as "Rage Strike" (increased damage) and "Battle Roar" (stuns the opponent).
- **Mage**: A Skilled sorcerer that can cast unique spells such as "Fireball" (high damage) and "Mana Shield" (reduces incoming damage).
- **Archer**: A Ranged fighter with abilities such as "Quick Shot" (double attack) and "Evade" (avoids the next attack).
- **Paladin**: A Royal knight with abilities such as "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

### `EvilWizard`
A special enemy character with higher health and the ability to regenerate health after every attack.



## Gameplay

1. **Character Creation**: The player selects a character class (Warrior, Mage, Archer, or Paladin) and provides a name.
2. **Battle**: The player battles the Evil Wizard in a turn-based format:
   - **Attack**: Perform a basic attack on the opponent.
   - **Special Ability**: Use one of the character's special abilities (each class has two unique abilities).
   - **Heal**: Heal for a random amount of health.
   - **Stats**: View the current health and attack power.
3. **Win/Loss Conditions**: The game ends when either the player or the Evil Wizard's health reaches 0. The player wins if the Evil Wizard is defeated, and loses if their own health reaches 0.

## Requirements

- Python 3.x

## Running the Game

1. Clone or download the repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:

```bash
python evil_wizard.py
