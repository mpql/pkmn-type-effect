"""Module to calculate the type effectiveness of a move against a Pokemon."""
import json
import sys

def format_decimal(decimal):
    """Format a number to 1 decimal places."""
    return f"{decimal:.1f}"

def calc_effect(attack, defend_1, defend_2):
    """Calculate the type effectiveness of a move against a Pokemon with given types."""
    # import type-data.json as object
    with open("type-data.json", encoding="utf8") as json_file:
        type_data = json.load(json_file)

    # get the effect of the attack against the first type
    effect_1 = type_data[attack][defend_1]
    print(f"{attack} against {defend_1}: {format_decimal(effect_1)}x")

    # get the effect of the attack against the second type, if any
    if defend_2 != "None":
        effect_2 = type_data[attack][defend_2]
        print(f"{attack} against {defend_2}: {format_decimal(effect_2)}x")
        return format_decimal(effect_1 * effect_2)
    else:
        return format_decimal(effect_1)

def main():
    """Main function."""
    attack    = sys.argv[1]
    defend_1  = sys.argv[2]
    # set defend_2 to "None" if not provided
    defend_2  = sys.argv[3] if len(sys.argv) > 3 else "None"

    print(f"Attacking: {attack}")
    print(f"Defending: {defend_1}, {defend_2}")

    print(f"\nEffectiveness: {calc_effect(attack, defend_1, defend_2)}x")

# invoke main function
if __name__ == "__main__":
    main()
