from django.apps import AppConfig


class FlowRatioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.flow_ratio'
def flow_needed(request, dimensions, color):
            #open(file, extract dimensions, )
    #compute ratio between 1.3-1.6 sq footage to forecast for 5 years

    #red = 1.3 * sq_footage
    #orange = 1.45 * sq_footage
    #green = 1.6 * sq_footage
    # flow_need  =
    #return flow_need
    return("Here is your flow needed:")

