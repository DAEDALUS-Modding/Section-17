# Changelog

## v0.8.0 (2024-05-03)

### Katrina (NEW UNIT)
- T2 multiple rocket launcher vehicle
- Low accuracy, high spread, high projectile count
- 310 range
- Costs 1700 metal

### Energy Coil (NEW UNIT)
- Unstable T1 Energy source
- Produces 1200 energy per second
- Costs 600 metal
- Discharges for 30 seconds (stops producing energy) if enemy units enter within 200 range
- Destroyed permanently if an enemy orbital unit enters within 200 range

### Ægir (NEW UNIT)
- Legion equivalent of Poseidon (Naval Titan)
- Statistically and visually identical for now
- Will change in the future

### Poseidon
- Build Bar icon color has changed to reflect MLA only status

### Dox Materializer
- New Model
- Cost: 300 -> 270

### Sigma
These cost increases are a temporary stopgap measure that will be partially reverted in a future Section 17 update.
- Cost: 90,000 -> 300,000
- Health: 80,000 -> 60,000

### Ligma
These cost increases are a temporary stopgap measure that will be partially reverted in a future Section 17 update.
- Cost: 90,000 -> 300,000
- Health: 40,000 -> 30,000
#### Bomber Drone
- Target priorities are less precise in order to fix previous aggro issues
#### Fighter Drone
- Guard Radius: 250 -> 5000

### Big Bill
- Cost: 10000 -> 8000
- Health: 5000 -> 3500

### Floater
- Cost: 4000 -> 3800

### Horntail
- Cost: 4000 -> 3600
- Bomb impact changed from normal damage to metal damage
- Bomb impact damage: 300 -> 400
- Bomb impact splash radius: 25 -> 4
- Range: 15 -> 5
- Bomb dispersion deviation: 4 -> 2
- Energy needed per bomb: 18000 -> 15000

### Pineapple
- Cost: 8000 -> 6000
- Health: 8000 -> 6000

### AI Changes
The Vanilla AI (not Queller) and some modded variants can now build:
- Katrina
- Dox Materializer
- Energy Coil

## v0.7.0 (2023-08-30)

### Ligma (NEW UNIT)
- Legion alternative to Sigma
- More fragile than Sigma, but can overwhelm enemies with massive drone swarms
- Carries 80 orbital fighter drones and 80 bomber drones
- 12 second Planetary Annihilation Cooldown (normal orbital units have 3 seconds)

### Sigma
- Planetary Arrival Cooldown: 3 seconds -> 12 seconds
- Hitbox size increased significantly

## v0.6.0 (2023-06-12)

### General
- Update unit shadows
  - TITANS Build 116982
  - Legion 1.28.0-116982

- Add Custom58 support.
  - Likely less conflicts with Thorosmen now.

### Dox Materializer
- Cost: 450 -> 300


## v0.5.0 (2023-02-11)

### General

- All experimental negative energy production values have been converted into energy consumption.
  - This means that you can power experimentals down now instead of having to delete them to regain energy. 
  - This is a buff.
- Update unit shadows
  - TITANS Build 116400
  - Legion v1.26.0-116242
- Add consistent language localization support

### Dox Materializer
New Unit Addition
- Costs 450 metal
- Spawns a free Dox every 30 seconds
- Includes a Dox preloaded

### Poseidon
Metal draw of the Poseidon has been decreased, with metal per shot lowered to compensate. This means that the Poseidon should be a bit more consistent in performance regardless of available metal. Torpedo drone capacity has also gone up.

- Air Drone Launcher buffs:
  - Ammo Demand: 50 -> 30
  - Ammo per Shot: 25 -> 15
  - Ammo Capacity: 50 -> 30
- Amphibious Drone Launcher buffs:
  - Ammo Demand: 25 -> 15
  - Ammo per Shot: 25 -> 15
  - Ammo Capacity: 25 -> 15
- Torpedo Drone Launcher buffs:
  - Ammo Demand: 50 -> 30
  - Ammo per Shot: 25 -> 15
  - Ammo Capacity: 25 -> 30

### Horntail
- Metal Cost: 5000 -> 4000
- Bomb Damage: 150 -> 300
- Bomb Splash Damage: 100 -> 200
- Larva Metal Damage: 5 -> 10

## v0.4.0 (2022-02-21)
- Update Legion compat to v1.22.0

### Pineapple
- Improve attack effects greatly (thanks to Ferretmaster)
- Rate of Fire: 4 -> 1
- Damage: 100 -> 400

### Sigma
- Changes thanks to Ferretmaster
- Upgrade textures from 256x256 to 512x512
- Significantly upgraded visual and sound effects
- Anti-Orbital Railgun changed:
  - Rate of Fire: 10 -> 0.5
  - Damage: 500 -> 2500
  - Full Damage Splash Radius: 5 -> 40
  - Fire Delay: 0.25 -> 0
- Anti-Surface Cannons changed:
  - Full Damage Splash Radius: 2 -> 20
  - Splash Radius: 20 -> 30
  - Firing Standard Deviation: 0 -> 1.5

### Poseidon
- Health: 40,000 -> 20,000
- Air Drone Launcher changed:
  - Rate of Fire: 1.5 -> 2.0
  - Ammo Demand: 75 -> 50
  - Ammo per Shot: 50 -> 25
  - Ammo Capacity: 50 -> 25
- Amphibious Drone Launcher changed:
  - Rate of Fire: 0.5 -> 1.0
  - Ammo per Shot: 50 -> 25
  - Ammo Capacity: 50 -> 25
- Torpedo Drone Launcher changed:
  - Rate of Fire: 1.0 -> 2.0
  - Ammo per Shot: 50 -> 25
  - Ammo Capacity: 50 -> 25
  - Damage: 250 -> 500
  - Full Damage Splash Radius: 0 -> 5
  - Splash Damage: 0 -> 250
  - Splash Radius: 0 -> 10

## v0.3.0 (2021-10-24)
- Fix `modinfo.json` schema issues for PAMM compatibility
- Reduce Sigma anti-surface range from 375 to 275

## v0.2.2 (2021-07-25)

- Fix Sigma not always being visible while being built
- Fix Horntail being buildable by T2 Air Fabs
- Fix Legion Orbital Fabs not being able to build Poseidon

## v0.2.1 (2021-06-27)

- Fix build bar location conflict between S17 Yellowjacket and 2W Pegasus
- Add a new MLA Orbital unit, the Sigma Fathership

## v0.2.0 (2021-05-02)

- Full compatibility with Legion
- The Experimental Land Gantry has become just the Experimental Gantry
  - Colonels and Praetorians may now build the Experimental Gantry
  - T2 Air Fabs may now build the Experimental Gantry
  - The Experimental Gantry may now be built on water
- The Horntail is now built from the Experimental Gantry
- The Pineapple is now Amphibious
- Experimentals are no longer buildable from the T2 Vehicle factory when neither Legion nor Second Wave are on

## v0.1.1 (2021-03-09)

- Add forum link to `modinfo.json`

## v0.1.0 (2021-03-09)

- Initial stable release

## v0.0.7 (2021-03-04)

- Move Equestrian above Centaur in build bar

## v0.0.6 (2021-03-04)

- Update `modinfo.json`

## v0.0.5 (2021-03-04)

- Update `modinfo.json`

## v0.0.4 (2021-03-04)

- Adjust Poseidon usability and balance

## v0.0.1 (2021-01-08)

- Initial public release (Experimental Vehicle Gantry and Big Bill)