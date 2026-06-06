# simple_simulation.py
# Week 1 SimPy Practice
# Basic Event Simulation for IoT Security

import simpy

# simulation settings
simulation_time = 20

normal_interval = 2
attack_interval = 5
check_interval = 3

# counters
normal_count = 0
attack_count = 0
detected_count = 0


# normal device process
def device(env):

    global normal_count

    while True:

        normal_count += 1

        print("Time", env.now, ": Device sent normal packet")

        yield env.timeout(normal_interval)


# attacker process
def hacker(env):

    global attack_count

    while True:

        attack_count += 1

        print("Time", env.now, ": Attacker injected fake packet")

        yield env.timeout(attack_interval)


# defender process
def defender(env):

    global detected_count

    while True:

        if attack_count > detected_count:

            detected_count += 1

            print("Time", env.now, ": Attack detected")

        else:

            print("Time", env.now, ": Network is safe")

        yield env.timeout(check_interval)


# create environment
env = simpy.Environment()

# start processes
env.process(device(env))
env.process(hacker(env))
env.process(defender(env))

# run simulation
env.run(until=simulation_time)

# final results
print()
print("Simulation Finished")
print("Normal Packets :", normal_count)
print("Fake Packets :", attack_count)
print("Detected Attacks :", detected_count)