# How can this simulation be extended to include random dirt generation in the environment during the simulation using vaccum cleaner?
import random

class VacuumCleanerEnvironment:
    def __init__(self):
        self.state = {'A': 'dirty', 'B': 'dirty'}
    
    def is_dirty(self, location):
        return self.state[location] == 'dirty'
    
    def clean(self, location):
        self.state[location] = 'clean'
    
    def print_state(self):
        print(f"Location A is {self.state['A']}, Location B is {self.state['B']}")
    
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.current_location = 'A'
    
    def move(self, location):
        self.current_location = location
    
    def act(self):
        if self.environment.is_dirty(self.current_location):
            print(f"Cleaning {self.current_location}")
            self.environment.clean(self.current_location)
        else:
            print(f"{self.current_location} is already clean.")
        self.move('B' if self.current_location == 'A' else 'A')

def run_vacuum_cleaner_simulation(steps=3):
    env = VacuumCleanerEnvironment()
    agent = VacuumCleanerAgent(env)
    
    for step in range(steps):
        print(f"Step {step + 1}:")
        env.print_state()
        agent.act()
        print()

run_vacuum_cleaner_simulation()
