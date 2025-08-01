import math

class Driver():
    def __init__(self, name, age, car_name, offensive_moves, defensive_tactics):
        # private attributes, can't acces directly using .
        self.__name = name
        self.__age = age
        self.__car_name = car_name
        self.__tire_health = 100        
        self.__fuel = 500   
        self.__offensive_moves = offensive_moves       # list of objects created from OffensiveMoves class
        self.__defensive_tactics = defensive_tactics   # list of objects created from DefensiveTactics class

    def get_name(self):
        return self.__name
    
    def get_fuel(self):
        return self.__fuel

    def get_tire_health(self):
        return self.__tire_health    

    # display entire info of driver 
    def display_info(self):
        print("Driver Info:")
        print(f"Name       : {self.__name}")
        print(f"Age        : {self.__age}")
        print(f"Car        : {self.__car_name}")
        print(f"Tire Health: {self.__tire_health}")
        print(f"Fuel       : {self.__fuel}")

        print("Offensive Moves:")
        for move in self.__offensive_moves:
            print(f"- {move.get_name()}")

        print("Defensive Tactics:")
        for tactic in self.__defensive_tactics:
            print(f"- {tactic.get_name()}")

        print("--" * 30)

    # display only current stats
    def display_stats(self):
        print(f"{self.__name}'s Stats:")
        print(f"Tire Health       : {self.__tire_health}")
        print(f"Fuel              : {self.__fuel}")
        print("Offensive Moves   :")
        for move in self.__offensive_moves:
            print(f"  • {move.get_name()} (Uses left: {'∞' if move.get_uses() == math.inf else move.get_uses()})")

        print("Defensive Tactics :")
        for tactic in self.__defensive_tactics:
            print(f"  • {tactic.get_name()} (Uses left: {'∞' if tactic.get_uses() == math.inf else tactic.get_uses()})")

        print("--" * 30)


    def is_exhausted(self):  # will use later to terminate the race if true -> the driver lost the race 
        return self.__tire_health <= 0
    
    def apply_damage(self, damage):  # this variable(damage) is passed by the offense of opponent
        self.__tire_health -= int(damage)  
        self.__incoming_damage = int(damage)  # will use later in defense method

    def consume_fuel(self, amount):
        self.__fuel -= amount   
         
    def reduce_damage(self, reduced_damage):
        self.__tire_health += int(reduced_damage)
        
    def offense(self):     
        print(f"\n{self.__name}'s Offensive Moves:")
        
        # uncomment for realistic game, when fuel lower than zero cant preform both offensive and defensive
        # while commented: the driver can preform  offensive moves even fuel below zero as required 
        '''# Get minimum fuel requirement
        min_fuel_required = min(move.get_fuel_cost() for move in self.__offensive_moves if move.get_uses() > 0)

        if self.get_fuel() < min_fuel_required:
            print(f"{self.__name} does not have enough fuel to perform *any* offensive move.")
            return None, 0   
        '''
        
        for i, move in enumerate(self.__offensive_moves):
            print(f"{i+1}. {move.get_name()} (Fuel: {move.get_fuel_cost()}, Uses Left: {'∞' if move.get_uses() == math.inf else move.get_uses()})")
    
        while True:
            try:
                choice = int(input("Select your move: ")) - 1
                move = self.__offensive_moves[choice] # select the move from the list by index 
                
                '''if self.get_fuel() < move.get_fuel_cost():  # compare required with available fuel
                    print("Not enough fuel. Choose another.")
                    continue
                '''  # logical error, but its not required in the task 
                
                if move.get_uses() <= 0:
                    print("This moves not available anymore. Choose other")
                    continue
                
                self.consume_fuel(move.get_fuel_cost())  
                move()    # reduce no of uses if it wasn't infinity 
                
                return move.get_name(), move.get_impact()# return used move name and damage on opponent 
            
            except (IndexError, ValueError):
                print("Invalid choice. Try again.")


    def defense(self):
        print(f"\n{self.__name}'s Defensive Tactics:")
        
        min_fuel_required = min(tactic.get_fuel_cost() for tactic in self.__defensive_tactics if tactic.get_uses() > 0)
        if self.get_fuel() < min_fuel_required:
            print(f"{self.__name} does not have enough fuel to perform any defensive tactic.")
            return None, 0
        
        for i, tactic in enumerate(self.__defensive_tactics):
            print(f"{i+1}. {tactic.get_name()} (Fuel: {tactic.get_fuel_cost()}, Uses Left: {'∞' if tactic.get_uses() == math.inf else tactic.get_uses()})")
    
        while True:
            try:
                choice = int(input("Select your defensive move: ")) - 1
                tactic = self.__defensive_tactics[choice]

                if self.get_fuel() < tactic.get_fuel_cost():
                    print("Not enough fuel. Choose another.")
                    continue
                
                if tactic.get_uses() <= 0:
                    print("This tactic not available anymore. Choose other")
                    continue
                
                self.consume_fuel(tactic.get_fuel_cost())
                tactic()  # reduce number of uses
                reduction_percent = int(tactic.get_damage_reduction().strip('%'))
                reduced_damage = int(self.__incoming_damage * (1 - reduction_percent / 100))   # calculate the tire_health will be restored 
                self.reduce_damage(reduced_damage)
                
                return tactic.get_name(), reduction_percent  # return tatic name and reduction_ percent
            
            except (IndexError, ValueError):
                print("Invalid choice. Try again.")
                
                
    def choose_move(self):
        print(f"\n{self.__name}, it's your turn to move.")
        return self.offense()

    def respond(self):
        print(f"\n{self.__name}, it's your turn to respond.")
        
        min_fuel_required = min(tactic.get_fuel_cost() for tactic in self.__defensive_tactics if tactic.get_uses() > 0)
        if self.get_fuel() >= min_fuel_required: 
            print("1. Defend")
            print("2. Counter-Attack")

            while True:
                try:
                    choice = int(input("Choose response type: "))
                    if choice == 1:
                        return self.defense() 
                    elif choice == 2:
                        return self.offense()  
                    else:
                        print("Invalid input. Choose 1 or 2.")
                except ValueError:
                    print("Please enter a number.")
                    
        else:
            print("Your fuel is critically low. You can only perform an offensive move now")
            return self.offense()  
           
