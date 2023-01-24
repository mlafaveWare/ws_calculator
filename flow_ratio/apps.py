from django.apps import AppConfig


class FlowRatioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flow_ratio'
def flow_needed(request, dimensions):
            #open(file, extract dimensions, )
    #compute ratio between 1.3-1.6 sq footage to forecast for 5 years
    # flow_need  = sq footage * 1.45 ie
    #return flow_need
    return("Here is your flow needed:")

