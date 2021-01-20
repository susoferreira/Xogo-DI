

class Resources():  # almacena Recursos

    def __init__(self, food_count: int, building_mat_count: int, reasearch_pts: int):
        self.food_count = food_count
        self.building_mat_count = building_mat_count
        self.research_pts = reasearch_pts

    def add(self, resources: "Resources") -> "Resources":
        return Resources(self.food_count + resources.food_count,
                         self.building_mat_count + resources.building_mat_count,
                         self.research_pts + resources.research_pts)


class Person():  # Buildings are populated by persons

    def __init__(self, attack_power: int, deffense_power: int, count: float):
        self.attack_power = attack_power
        self.deffense_power = deffense_power
        self.count = count

    @abstractmethod
    def getResources(self) -> Resources:
        pass



class Worker(Person):  # tipo de persona que genera recursos
    BASE_WORKER_POWER = 1
    BASE_WORKER_DEFFENSE = 1

    def __init__(self, count):
        super().__init__(Worker.BASE_WORKER_POWER, Worker.BASE_WORKER_DEFFENSE, count)


class Population():
    POPULATION_TYPES: Dict[Any, float] = {
        Person: 0,
        Worker: 0,
    }

    def __init__(self, pop: List[Person]):
        self.persons = Population.POPULATION_TYPES
        self.add_population(pop)

    def add_population(self, pop: List[Person]):
        for i in pop:
            if type(i) in self.persons:
                self.persons[type(i)] += i.count

    def get_count(self)-> List[int]:
        return [int(j) for _,j in self.persons.items()]