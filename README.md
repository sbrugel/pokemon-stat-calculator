# pokemon stat calculator
A program made in Python using the tkinter library to calculate the stats of a Pokemon, based on user-inputted information. I made this for personal use during my own randomized playthroughs as well as a way to find a decent Python GUI library to utilize in the future.

The information needed to calculate each stat is:
- The base of each stat (Health, Atk, Def, SpAtk, SpDef, Spd). Information for this can be found on [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page). For randomized ROMs where base stats are randomized (as is the case for most of my Pokemon playthroughs nowadays), you'll need to find this information elsewhere.
- IVs for each stat. You can find these using [PKHex](https://projectpokemon.org/home/files/file/1-pkhex/)
- EVs for each stat. You can find these using [PKHex](https://projectpokemon.org/home/files/file/1-pkhex/)
- Level of the Pokemon
- Nature of the Pokemon

This then returns the estimated stats, with a margin of error of 1 unit.

## Notes
The formulas for calculating stats are different between Gens 1-2 and Gens 3+ for three reasons:
- The special split did not exist in Gen 1-2.
- Natures did not exist in Gen 1-2.
- EVs are calculated differently between both gens.

Currently only Gen 3 calculation is implemented. Gen 1-2 calculation will be implemented later.

## To do
- [ ] Error messages for empty boxes
- [ ] Error messages for non-numerical inputs
- [ ] Implement Gen 1-2 calculations
