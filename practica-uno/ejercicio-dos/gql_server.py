import graphene
from graphene import ObjectType, String, Int, Boolean, List, Field, Mutation, ID
class Plant(ObjectType):
    id= ID()
    cname= String()
    species = String()
    age = Int()
    height = Int()
    has_fruits = Boolean()
    
plants =[
    Plant(id=1, common_name="Rosa", species="Rosa gallica", age=6, height=50, has_fruits=True),
    Plant(id=2, common_name="Tulipán", species="Tulipa gesneriana", age=3, height=30, has_fruits=False),
    Plant(id=3, common_name="Girasol", species="Helianthus annuus", age=4, height=180, has_fruits=True),
]

class Query(ObjectType):
    all_plants = List(Plant)
    plant_by_species = List(Plant, species=String())
    plants_with_fruits = List(Plant)

    def resolve_all_plants(self, info):
        return plants

    def resolve_plant_by_species(self, info, species):
        return [plant for plant in plants if plant.species == species]

    def resolve_plants_with_fruits(self, info):
        return [plant for plant in plants if plant.has_fruits]


class PlantMutation(Mutation):
    class Arguments:
        common_name = String(required=True)
        species = String(required=True)
        age = Int(required=True)
        height = Int(required=True)
        has_fruits = Boolean(required=True)

    plant = Field(Plant)

    def mutate(self, info, common_name, species, age, height, has_fruits):
        new_plant = Plant(id=len(plants) + 1, common_name=common_name, species=species, age=age, height=height, has_fruits=has_fruits)
        plants.append(new_plant)
        return PlantMutation(plant=new_plant)

class Mutation(ObjectType):
    create_plant = PlantMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
app = graphene.test.test_app.test_app(schema)

if __name__ == "__main__":
    app.run(debug=True)