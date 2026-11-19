from data import CountyDemographics


def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for i in counties:
        total += i.population["2014 Population"]
    return total

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state]

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    # 2014 population × percentage / 100
    return sum([(population_total([county]) * county.education[key] / 100) for county in counties])

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    # 2014 population × percentage / 100
    return sum([(population_total([county]) * county.ethnicities[key] / 100) for county in counties])

def population_by_poverty(counties: list[CountyDemographics]) -> float:
    # 2014 population × percentage / 100
    return sum([(population_total([county]) * county.income["Persons Below Poverty Level"] / 100) for county in counties])
# 100 × (sub-population total / total population)

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    return (100 * ((population_by_education(counties, key) / population_total(counties))))

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    return (100 * ((population_by_ethnicity(counties, key) / population_total(counties))))

def percent_below_poverty_level(counties: list[CountyDemographics], key: str) -> float:
    return (100 * ((population_by_poverty(counties, key) / population_total(counties))))

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.education[key] > threshold]
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities[key] > threshold]
def poverty_greater_than(counties: list[CountyDemographics], threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] > threshold]

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.education[key] < threshold]
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities[key] < threshold]
def poverty_less_than(counties: list[CountyDemographics], threshold: float)  -> list[CountyDemographics]:
    return [county for county in counties if county.income["Persons Below Poverty Level"] < threshold]
 