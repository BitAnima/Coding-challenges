"""Space Week Day 7: Launch Fuel
For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit.
Determine the amount of fuel needed to send your payload to orbit using the following rules:

Rockets require 1 kg of fuel per 5 kg of mass they must lift.
Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again.
Repeat this process until the additional fuel required is less than 1 kg, then stop.
Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.
For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5),
which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg),
which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg -
which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.

Return the amount of fuel needed rounded to one decimal place.
"""

def launch_fuel(payload: int = 50) -> float:
    """Calculates the total fuel required to launch a payload into orbit.

        This function iteratively calculates fuel based on the principle that
        fuel itself has mass and requires additional fuel to be lifted. The
        calculation starts with the payload's mass and repeatedly computes
        the fuel needed for the mass of the fuel added in the previous step.

        The process stops once the amount of additional fuel required in a
        single step is less than 1 kg.

        Args:
            payload_mass (int): The initial mass of the payload in kilograms.

        Returns:
            float: The total amount of fuel needed in kilograms, rounded to
                   one decimal place.

        Example:
            launch_fuel(50)
            12.4"""

    current_weight: float = float(payload)
    fuel_needed: float = 0.0

    while True:
        additional_fuel: float = current_weight / 5
        print(additional_fuel)
        if additional_fuel < 1:
            fuel_needed += additional_fuel
            print(fuel_needed)
            break

        fuel_needed += additional_fuel

        current_weight = additional_fuel

    return round(fuel_needed, 1)

launch_fuel()


