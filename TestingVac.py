from agents import *
from notebook import psource
import time
import random


def SimpleReflexAgentProgram():
    """This agent takes action based solely on the percept. [Figure 2.10]"""

    def program(percept):
        loc, status = percept
        return ('Suck' if status == 'Dirty'
                else 'Right' if loc == loc_A
        else 'Left')

    return program



if __name__ == "__main__":
    psource(TrivialVacuumEnvironment)
    # These are the two locations for the two-state environment
    loc_A, loc_B = (0, 0), (1, 0) # 0,0 is left room and 1,0 is right room

    # Initialize the two-state environment
    trivial_vacuum_env = TrivialVacuumEnvironment()

    # Check the initial state of the environment
    program = SimpleReflexAgentProgram()
    simple_reflex_agent = Agent(program)

    trivial_vacuum_env.add_thing(simple_reflex_agent)
    print("State of the Environment: {}.".format(trivial_vacuum_env.status))
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))
    dirtyUptime = 0
    cleanUptime = 0
    room0 = 0
    room1 = 0
    goalreached = 0


    for i in range(10):
        n = random.randint(0,2) # Get a random number to decide which room we will make dirty. 0= Left room is dirty, 1= right room is dirty, 2= do nothing
        if n == 0:
            string = "Room " + str(n) + " was made dirty"
            print(string)
            trivial_vacuum_env.status[0,0] = "Dirty"
        elif n == 1:
            string = "Room " + str(n) + " was made dirty"
            print(string)
            trivial_vacuum_env.status[1,0] = "Dirty"

        print("State of the Environment: {}.".format(trivial_vacuum_env.status))
        print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))
        # Run the environment
        trivial_vacuum_env.step()

        # Check the current state of the environment
        print("State of the Environment: {}.".format(trivial_vacuum_env.status))
        print("\n")
        print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))
        if trivial_vacuum_env.status[1,0] == "Dirty":
            dirtyUptime += 1
        if trivial_vacuum_env.status[0,0] == "Dirty":
            dirtyUptime += 1
        if trivial_vacuum_env.status[1,0] == "Clean":
            cleanUptime += 1
        if trivial_vacuum_env.status[0,0] == "Clean":
            cleanUptime += 1
        if simple_reflex_agent.location == (1,0):
            room1 += 1
        if simple_reflex_agent.location == (0,0):
            room0 += 1
        if trivial_vacuum_env.status[0,0] == "Clean" and trivial_vacuum_env.status[1,0] == "Clean":
            goalreached += 1
        #time.sleep(10) # give us time to analyze. Can be commented out for faster execution.
    print("Number of times a room was dirty: ", dirtyUptime)
    print("Number of times a room was clean: ", cleanUptime)
    print("Number of times the agent was in room 0: ", room0)
    print("Number of times the agent was in room 1: ", room1)
    print("Number of times the agent reached the goal of having both rooms clean: ", goalreached)
    print("Agent performance score: ", simple_reflex_agent.performance)
