# How can you implement a simulation for a motion light detection system where a light turns on if motion is detected and turns off after a specified duration if no motion is detected? Extend the simulation to randomly simulate motion events at regular intervals.

import random

class motionLightDetection:
        def __init__(self, motion):
                self.motion=motion
        
        def is_motion(self):
                return self.motion==True
        def no_motion(self):
                return self.motion==False
        def print_statement(self):
                if self.motion:
                    print("Motion is detected")
                else:
                       print("Motion is not detected")
class MotionLightAgent:
    def __init__(self, environment):
              self.environment=environment
    def light_on(self):
            if self.environment.is_motion():
                  print("Light is on")
            else:
                print("Light is off")

def main():
    e1=motionLightDetection(True)
    e1.print_statement()

    agent=MotionLightAgent(e1)
    agent.light_on

    e1=motionLightDetection(False)
    e1.print_statement()

    agent=motionLightDetection(e1)
    e1.print_statement()

main()


              