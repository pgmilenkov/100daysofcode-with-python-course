from research import BadDriversResearch

research = BadDriversResearch()

print("States sorted by died drivers:")
for state in research.sort_states_by_died_drivers()[:5]:
    print("'{}' and died '{}'".format(state.state, state.drivers_fatal_collisions))

print("#" * 20)

print("States sorted by speeding drivers:")
for state in research.sort_states_by_speed()[:10]:
    print(f"'{state.state}' and speeding '{state.drivers_fatal_collisions}'".format(state))

print("#" * 20)

print("States sorted by drinking drivers:")
for state in research.sort_states_by_alcohol()[:5]:
    print(f"'{state.state}' and drinking '{state.drivers_alcohol_impaired}'".format(state))

print("#" * 20)

print("States sorted by insurance companies losses:")
for state in research.sort_states_by_insurance_company_loss()[:10]:
    print("'{}' and insurance losses '{}'".format(state.state, state.drivers_fatal_collisions))

