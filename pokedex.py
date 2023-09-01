from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def get_last_evoultion_with_one_weakness(self):
        try:
            filter = {
                'next_evolution': {
                    '$exists': False
                }, 
                'weaknesses': {
                    '$size': 1
                }
            }

            result = self.database.collection.find(
              filter=filter
            )

            writeAJson(result, "last_evolutions")
            print("Got all one evolution pokemons")
        except Exception as e:
            print(e)

    def get_rare_pokemons(self):
        try :
            filter = {
                'egg': 'Not in Eggs', 
                'spawn_chance': {
                    '$lt': 0.09
                }
            }

            sort = list({
                'spawn_chance': 1
            }.items())

            result = self.database.collection.find(
              filter=filter,
              sort=sort
            )

            writeAJson(result, "rare_pokemons")
            print("Got all rare pokemons")
        except Exception as e:
            print(e)

    def get_first_evolution_pokemons(self):
        try:
            filter = {
                'prev_evolution': {
                    '$exists': False
                }
            }

            project = {
                'name': 1, 
                'next_evolution': 1, 
                'img': 1
            }

            result = self.database.collection.find(
              filter=filter,
              projection=project
            )

            writeAJson(result, "first_evolution_pokemons")
            print("Got all first evolution pokemons")
        except Exception as e:
            print(e)

    def get_pokemons_by_candy_count_range(self, min, max):
        try:
            filter = {
                'candy_count': {
                    '$gt': min, 
                    '$lt': max
                }
            }

            project = {
                'id': 1, 
                'name': 1, 
                'candy': 1, 
                'candy_count': 1
            }

            sort = list({
                'candy_count': 1
            }.items())

            result = self.database.collection.find(
              filter=filter,
              projection=project,
              sort=sort
            )

            writeAJson(result, "pokemons_by_candy_count_range")
            print("Got all first evolution pokemons")
        except Exception as e:
            print(e)

    def get_pokemons_with_single_type(self, desired_type):
        try:
            filter={
                'type': {
                    '$elemMatch': {
                        '$eq': desired_type,
                    }, 
                    '$size': 1
                }
            }

            project={
                'name': 1, 
                'type': 1
            }

            result = self.database.collection.find(
              filter=filter,
              projection=project
            )

            writeAJson(result, "single_type_pokemons")
            print("Got all pokemons for given single type")
        except Exception as e:
            print(e)


