import math 
from driver import Driver
from moves import OffensiveMoves, DefensiveTactics

# Offensive Moves
turbo_start = OffensiveMoves(
    move_name="Turbo Start",
    fuel_cost=50,
    tire_impact_on_opponent=10,
    no_uses=math.inf,
    description="Early burst of speed."
)

mercedes_charge = OffensiveMoves(
    move_name="Mercedes Charge",
    fuel_cost=90,
    tire_impact_on_opponent=22,
    no_uses=math.inf,
    description="Full-throttle attack."
)

corner_mastery = OffensiveMoves(
    move_name="Corner Mastery",
    fuel_cost=25,
    tire_impact_on_opponent=7,
    no_uses=math.inf,
    description="Skilled turning for efficiency."
)

drs_boost = OffensiveMoves(
    move_name="DRS Boost",
    fuel_cost=45,
    tire_impact_on_opponent=12,
    no_uses=math.inf,
    description="Drag Reduction System, is a mechanism that allows drivers to temporarily increase their straight-line speed."
)

red_bull_surge = OffensiveMoves(
    move_name="Red Bull Surge",
    fuel_cost=80,
    tire_impact_on_opponent=20,
    no_uses=math.inf,
    description="Aggressive acceleration, high tire wear."
)

precision_turn = OffensiveMoves(
    move_name="Precision Turn",
    fuel_cost=30,
    tire_impact_on_opponent=8,
    no_uses=math.inf,
    description="Tactical turn to gain time with minimal fuel."
)

# Defensive Tactics
brake_late = DefensiveTactics(
    move_name="Brake Late",
    fuel_cost=25,
    damage_reduction="30%", 
    no_uses=math.inf,
    description="Uses ultra-late braking to reduce attack impact. Common but risky."
)

ers_deployment = DefensiveTactics(
    move_name="ERS Deployment",
    fuel_cost=40,
    damage_reduction="50%",
    no_uses=3,
    description="Deploys electric recovery system defensively to absorb incoming pressure and recover next turn."
)

slipstream_cut = DefensiveTactics(
    move_name="Slipstream Cut",
    fuel_cost=20,
    damage_reduction="40%",
    no_uses=math.inf,
    description="Cuts into the airflow behind the leading car to reduce their advantage and limit damage."
)

aggressive_block = DefensiveTactics(
    move_name="Aggressive Block",
    fuel_cost=35,
    damage_reduction="100%",
    no_uses=2,
    description="Swerves defensively to completely block a single incoming move. Can only be used once due to risk."
)


def main():
    print("\n🏁 Welcome to The Final Race – Verstappen vs Mostafa 🏁")

    # Create Drivers
    max_driver = Driver(
        name="Max Verstappen",
        age=27,
        car_name="Red Bull Racing",
        offensive_moves=[turbo_start, mercedes_charge, corner_mastery],
        defensive_tactics=[brake_late, ers_deployment]
    )

    hassan_driver = Driver(
        name="Hassan Mostafa",
        age=24,
        car_name="Ferrari SF-75",
        offensive_moves=[drs_boost, red_bull_surge, precision_turn],
        defensive_tactics=[slipstream_cut, aggressive_block]
    )

    drivers = [max_driver, hassan_driver]
    round_number = 1

    while True:
        print(f"\n{'='*15} ROUND {round_number} {'='*15}")
        
        for turn_index in range(2):
            attacker = drivers[turn_index]
            defender = drivers[1 - turn_index]

            print(f"\n🔻 Turn {turn_index + 1} – {attacker.get_name()}'s Move 🔻")

            # Attacker chooses move
            move_name, damage = attacker.choose_move()

            # Defender takes damage
            defender.apply_damage(damage)

            # Defender responds (either blocks or counterattacks)
            response_name, effect = defender.respond()    # both return two values
            
            if defender.is_exhausted():
                print(f"\n🏆 {attacker.get_name()} wins the race!\n")
                return
            
            if isinstance(effect, int):
                print(f"{defender.get_name()} defended with {response_name}, reducing damage by {effect}%.")
            else:
                # Counterattack applied to attacker
                attacker.apply_damage(effect)
                if attacker.is_exhausted():
                    print(f"\n🏆 {defender.get_name()} wins the race!\n")
                    return

            # Turn Summary
            print("\n📋 Turn Summary:")
            print(f"• {attacker.get_name()} used: {move_name}")
            print(f"• {defender.get_name()} responded with: {response_name}")
            print("\nCurrent Stats:")
            max_driver.display_stats()
            hassan_driver.display_stats()

            # Mid-round check(necessary because defender can respond by an offensive move)
            if attacker.is_exhausted() or defender.is_exhausted():
                break

        # End of round check
        if max_driver.is_exhausted():
            print("\n🏁 Hassan Mostafa wins the race!")
            break
        elif hassan_driver.is_exhausted():
            print("\n🏁 Max Verstappen wins the race!")
            break

        round_number += 1



if __name__ == '__main__':
    main()