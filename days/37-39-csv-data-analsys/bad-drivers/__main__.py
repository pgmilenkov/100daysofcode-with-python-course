from research import BadDriversResearch

research = BadDriversResearch()

# for state in research.sort_states_by_died_drivers()[:5]:
#     print("'{}' and died '{}'".format(state.state, state.drivers_fatal_collisions))
#
# print("#" * 20)

for state in research.sort_states_by_speed()[:10]:
    print("'{}' and speeding '{}'".format(state.state, state.drivers_fatal_collisions))

# print("#" * 20)
#
# for state in research.sort_states_by_alcohol()[:5]:
#     print("'{}' and drinking '{}'".format(state.state, state.drivers_fatal_collisions))
#
print("#" * 20)

for state in research.sort_states_by_insurance_company_loss()[:10]:
    print("'{}' and insurance losses '{}'".format(state.state, state.drivers_fatal_collisions))

