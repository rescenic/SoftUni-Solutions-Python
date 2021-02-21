class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemon:
            if p.name == pokemon_name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        t_data = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon)}\n"

        p_data = ""
        for p in self.pokemon:
            p_data += f"- {p.pokemon_details()}\n"
        return t_data + p_data
