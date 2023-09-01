from database import Database
from pokedex import Pokedex
db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db);

pokedex.get_first_evolution_pokemons()
pokedex.get_rare_pokemons()
pokedex.get_last_evoultion_with_one_weakness()
pokedex.get_pokemons_by_candy_count_range(10, 50)
pokedex.get_pokemons_with_single_type("Poison")
