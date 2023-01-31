from django.apps import AppConfig


class FloorCalculatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.floor_calculator'

def get_sq_footage_max(request, dimensions):
    #compute if req valid and max seats per sq 100 ft or so before factoring in flow ratio

    return("Here is your square footage")