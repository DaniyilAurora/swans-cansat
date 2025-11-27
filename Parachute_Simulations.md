# Parachute Simulations

There are different pieces of information we want to calculate in order to produce most efficient parachute for our project.

Firstly, we want to calculate the area of parachute needed. Our desired speed of descent would be 1.8-2 metres per second (m/s). To calculate the area needed for parachute will use the drag equation, which looks like this.

$$D=\frac{1}{2}\rho V^2CA$$

Where:
- D = drag force (N)
- ρ = air density (1.225 kg/m³)
- V = descent velocity (2 metres per second)
- C = drag coefficient (0.75-1.5)
- A = area of parachute (m²)

At steady speed drag equals to weight.

$$mg=\frac{1}{2}\rho v^2CA$$

Now we rearrange in order to get the area.

$$A=\frac{2mg}{\rho V^2C}$$

CanSat limits mass of the satellite to be 300-350 grams, and we will use drag coefficient of 1 for our calculations. Now we apply all of the values to the formula.

$$A=\frac{2(0.350)(9.81)}{(1.225)(2)^2(1)}$$

Which results in.

$$A\approx 1.40\ m^2$$

Which means that the radius of our parachute should be.

$$A=\sqrt{\frac{A}{\pi}}=\sqrt{\frac{1.40}{\pi}}\approx 0.6\ m$$

So, now we have radius, also what we would like to know is how much time it will take for a model to descend from 1000 metres to ground. For this we do simple calculation.

$$time=\frac{distance}{velocity}=\frac{1000}{2}=500\ seconds \approx 8.3\ minutes$$

Now, this time seems to be too optimistic, so our educated guess would be 3-6 minutes.