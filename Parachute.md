# The Parachute 

To build a parachute, we had to do a lot of research regarding the available materials, the different parachute shapes and the size required of each respective combination of parachute shape and material. On this page we will try to discuss all of our research in detail and explain how we got to our final parachute design.

### Parachute Shapes

We based our research on the ESA teachers guide for parachute design. In it, 4 different parachute shapes are presented. The shapes are:
- Hemispherical Parachute
- Cross Parachute
- Paraglider
- Flat Parachute

We also took a look at the drag coefficient of each parachute as with a higher drag coefficient, the area of the parachute doesn't need to be as large.
| Parachute Shape | Drag Coefficient |
| --------------- | ---------------- | 
| Hemispherical | 0.62-0.77 |
| Cross | 0.6-0.8 |
| Paraglider | 0.75-1.10 |
| Flat | 0.75-0.8 |

After reading through the description of each parachute, we were quickly able to rule out the paraglider shape as we do not need its steerability combined with the additional complexity. 

We also ruled out the hemispherical parachute shape as it is more complicated to assemble than a flat or cross parachute with little advantages over the other two designs.

This left us the cross shape parachute and flat parachute that would move on to our testing.

### Parachute Material

We chose two different materials to test the parachute shapes with: Polyester Fabric and Ripstop Nylon.

Ripstop Nylon was an obvious choice as it is the material recommended in the ESA teachers guide and in many other resources. 

Polyester Fabric may seem less obvious, but we chose it as it is partially breathable and lets some air through. Although this may seem like a disadvantage as a parchute needs to not let air pass to increase drag, it is actually a good thing. If the parachute material does not let air out, air will get trapped in the parachute which will result in instability and oscilations. On most parachutes this is solved with vent holes however those must be calculated well to not be too large or too small. Polyester fabric on the other hand already lets a small amount of air out, removing the need for vents. We are very grateful to Alfred Burger from Tree Frog Satellites for bringing this up to our attention.

### Parachute Experimenting

To find what shape and material combination we will use in our final parachute, we will hold a test. We will assemble a Cross parachute and a flat parachute of various sizes from each material and compare the results in a table. We will analyse the price, mass, flight time, drag coefficients and size to decide which combination to use for the final parachute.

### Formulas

There are different pieces of information we want to calculate in order to produce most efficient parachute for our project.

Firstly, we want to calculate the area of parachute needed. Our desired speed of descent is between 8 and 10 metres per second (m/s) as the minimum descent speed is 5 m/s and the maximum descent speed is 12 m/s due to safety reasons. To calculate the area needed for parachute will use the drag equation, which looks like this.

$$D=\frac{1}{2}\rho V^2CA$$

Where:
- D = drag force (N)
- ρ = air density (1.225 kg/m³)
- V = descent velocity (9 metres per second)
- C = drag coefficient (0.6-0.8)
- A = area of parachute (m²)

At steady speed drag equals to weight.

$$mg=\frac{1}{2}\rho v^2CA$$

Now we rearrange in order to get the area.

$$A=\frac{2mg}{\rho V^2C}$$

We will set all values to be the middle of their ranges. This means the mass will be 325 grams and we will use drag coefficient of 0.7 for our calculations. Now we apply all of the values to the formula.

$$A=\frac{2(0.350)(9.81)}{(1.225)(9)^2(0.7)}$$

Which results in.

$$A\approx 0.0989\ m^2$$

However we rounded the number up to 0.1 $$m^2$$

Which means that the radius of our parachute should be.

$$A=\sqrt{\frac{A}{\pi}}=\sqrt{\frac{1.40}{\pi}}\approx 0.6\ m$$

So, now we have radius, also what we would like to know is how much time it will take for a model to descend from 1000 metres to ground. For this we do simple calculation.

$$time=\frac{distance}{velocity}=\frac{1000}{2}=500\ seconds \approx 8.3\ minutes$$

Now, this time seems to be too optimistic, so our educated guess would be 3-6 minutes.
