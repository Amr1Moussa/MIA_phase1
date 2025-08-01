import math
class Move:
    def __init__(self, move_name, fuel_cost, no_uses=math.inf, description="No available description"):
        self._move_name = move_name
        self._fuel_cost = fuel_cost
        self._no_uses = no_uses
        self._description = description
        self.__initial_uses = no_uses

    def get_name(self):
        return self._move_name
    
    def get_fuel_cost(self):
        return self._fuel_cost 

    def get_uses(self):
        return self._no_uses
    
    def get_initial_uses(self):
        return self.__initial_uses

    def __str__(self):
        return (f"Name        : {self._move_name}\n"
                f"Fuel Cost   : {self._fuel_cost}\n"
                f"Uses Left   : {'∞' if self._no_uses == math.inf else self._no_uses}\n"
                f"Description : {self._description}")
    
    def __call__(self):
        if self._no_uses != math.inf:
            self._no_uses -= 1
    
    def reset_uses(self):
        if self.__initial_uses != math.inf:
            self._no_uses = self.__initial_uses        
 
class OffensiveMoves(Move):
    def __init__(self, move_name, fuel_cost, tire_impact_on_opponent, no_uses=math.inf, description="No available description"):
        super().__init__(move_name, fuel_cost, no_uses, description)
        self.__tire_impact_on_opponent = tire_impact_on_opponent

    def get_impact(self):
         return self.__tire_impact_on_opponent

    def __str__(self):
        return (f"[Offensive Move]\n"
                f"{super().__str__()}\n"
                f"Impact      : -{self.__tire_impact_on_opponent} Tire Health")

class DefensiveTactics(Move):
    def __init__(self, move_name, fuel_cost, damage_reduction, no_uses=math.inf, description="No available description"):
        super().__init__(move_name, fuel_cost, no_uses, description)
        self.__damage_reduction = damage_reduction

    def get_damage_reduction(self):
        return self.__damage_reduction

    def __str__(self):
        return (f"[Defensive Tactic]\n"
                f"{super().__str__()}\n"
                f"Reduction   : -{self.__damage_reduction} Damage Taken")