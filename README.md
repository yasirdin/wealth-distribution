# Wealth Distribution Simulation

## Summary
This project is inspired by an article I read which very roughly demonstrated the following simulation:
Assume a population N individuals. At time=0, each individual  starts with 1 unit of currency (1 coin). And at the end of each second (or some other interval $\delta t$),
every individual selects another at *random* and passes 1 coin to them, if the individual has no coins, they pass nothing.

As this system evolves, some states of stability are achieved whereby the wealth distribution amongst the popoulation remains relatively constant, and one such states mimics
the pareto distribution (where 20% of the population have accumulated 80% of total wealth). This project attempts to run this simulation and explore further.
