Vehicle handling parameters
================================

There are 50 parameters in 6 groups, plus additional sub handling data. 

Physical Attributes
----------------------

handlingName
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is used by the vehicles.meta file to identify the handling line of the vehicle. 

**Value:**

* ``string`` -- Any text string no more than 14 characters. By default, the handlingName consists of uppercase letters and numbers

================================

fMass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is th weight of the vehicle in kilograms. Only used when the vehicle collides with another vehicle or non-static object. 

**Value:**

* ``float`` -- The weight of the vehicle in kilograms. 0.0 - 10000.0 and above.

================================

fInitialDragCoeff
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the drag coefficient on the rage physics archetype of the vehicle (proportional to velocity squared). Increase to simulate aerodynamic drag.
This affects the maximum speed of the vehicle. Greater value will lower the maximum speed.

**Value:**

* ``int`` -- The drag coefficient of the vehicle. 10 - 120.

================================

fDownForceModifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the amount of downforce applied to the vehicle. Increase this value to increase the grip at high speed.

**Value:**

* ``int`` -- The downforce of the vehicle. 0 - 150 and above.

================================

fPercentSubmerged
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A percentage of vehicle height in the water before vehicle "floats". So as the vehicle falls into the water, at 85% vehicle height (seemingly the default for road vehicles) it will stop sinking to float for a moment before it sinks (boats excluded).

**Value:**

* ``int`` -- any percentage expressed as a decimal (eg., 85% = 0.85). An invalid number will cause the vehicle to sink without the driver drowning, eventually teleporting the vehicle to the surface.

================================

vecCentreOfMassOffset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This value shifts the center of gravity in meters from side to side (when in vehicle looking forward). 

**Value:**

* ``TBD, possible VECTOR3`` -- This value shifts the center of gravity in meters from side to side (when in vehicle looking forward). -5.0 - 5.0 per coordinate.

================================

vecInertiaMultiplier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This value is resistance to rotation around each axis. Therefore, the x axis affects how quickly the car shifts forward and back under braking and acceleration and how it rotates end over end in the air, the y axis affects how quickly the car shifts from side to side when cornering (or in the air) and the z axis affects how the car rotates around the middle, which manifests in normal driving as how quickly the vehicle appears to react to steering inputs. Recommend keeping the z value above 2.0 unless you want arcade style immediate reaction to steering inputs
Note: Four cars do not respond typically to this value; the police3 (Police Interceptor), Gang Burrito, 190Z and Zion Classic. They need lower z values or else they will rotate too slowly. 

**Value:**

* ``TBD, possible VECTOR3`` -- 0.0 - 4.0 per coordinate.

================================

Transmission Attributes
-----------------------------

These values describe the vehicle's straight line performance. Rate of acceleration is determined by fDriveBiasFront, nInitialDriveGears, fInitialDriveForce, fDriveInertia, and fInitialDriveMaxFlatVel. Rate of deceleration is determined by fBrakeForce and fBrakeBiasFront. fSteeringLock can be thought of as a measure of sideways acceleration. 

fDriveBiasFront
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Value:**

* ``float`` -- 0.0 is rear wheel drive, 1.0 is front wheel drive, and any value between 0.01 and 0.99 is four wheel drive (0.5 give both front and rear axles equal force, being perfect 4WD.)

================================

nInitialDriveGears
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How many forward speeds a transmission contains.

**Value:**

* ``int`` -- 1 - 10 gear.

================================

fInitialDriveForce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This value specifies the drive force of the car, at the wheels. 

**Formula:**

.. code-block:: lua
    :linenos:
    
    fInitialDriveForce = TorqueWheelsNm/WeightKg

**Value:**

* ``float`` -- 0.01 - 2.0 and above. 1.0 uses drive force calculation unmodified. Values less than 1.0 will in effect give the vehicle less drive force and values greater than 1.0 will produce more drive force. Most cars have between 0.10 and 0.40.

This value is calculated with the vehicle weight, so heavy and light vehicles have an accurate acceleration. 

================================

fDriveInertia
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Describes how fast an engine will rev. For example an engine with a long stroke crank and heavy flywheel will take longer to redline than an engine with a short stroke and light flywheel. 

**Formula:**

.. code-block:: lua
    :linenos:
    
    TBD

**Value:**

* ``float`` -- 0.01 - 2.0. Default value is 1.0, or no modification of drive intertia. Bigger value = quicker redline

================================

fClutchChangeRateScaleUpShift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clutch speed multiplier on up shifts, bigger number = faster shifts. Recommended to not go over 13. A value of 1 = 0.9 seconds to shift gears. 

**Value:**

* ``float`` -- 0.01 - 13.0. Default value is 1.0, or no modification of clutch speed. Bigger value = quicker shifts

================================

fClutchChangeRateScaleDownShift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clutch speed multiplier on down shifts, bigger number = faster shifts. Recommended to not go over 13. A value of 1 = 0.9 seconds to shift gears.

**Value:**

* ``float`` -- 0.01 - 13.0. Default value is 1.0, or no modification of clutch speed. Bigger value = quicker shifts

================================

fInitialDriveMaxFlatVel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Determines the speed at redline in top gear; Controls the final drive of the vehicle's gearbox. Setting this value does not guarantee the vehicle will reach this speed. Multiply the number in the file by 0.82 to get the speed in mph or multiply by 1.32 to get kph. To find the right value for a given kph figure, kph * 0.75. 

**Formula:**

.. code-block:: lua
    :linenos:
    
    TopSpeedKph = (fInitialDriveMaxFlatVel * 1.2) / 0.9 

**Value:**

* ``float`` -- 0.01 - 500.0. Default value is 1.0, or no modification of clutch speed. Bigger value = quicker shifts

The top speeds for different gears can be calculated by replacing the 0.9 in the formula with the ratio of the specific gear. GTA V uses a ratio of 0.9 for the top gear by default. 

================================

fBrakeForce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multiplies the game's calculation of deceleration. Bigger number = harder braking 

**Formula:**

.. code-block:: lua
    :linenos:
    
    TBD

**Value:**

* ``float`` -- 0.01 - 2.0 and above. 1.0 uses brake force calculation unmodified.

================================

fBrakeBiasFront
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This controls the distribution of braking force between the front and rear axles. 

**Value:**

``float`` -- 0.0 - 1.0. Default value is 0.5, or no modification of brake force. Bigger value = more force on front axle.

================================

fHandBrakeForce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Braking power for handbrake. Bigger number = harder braking 

**Value:**

``float`` -- 0.01 - 2.0 and above. 1.0 uses brake force calculation unmodified.

================================
