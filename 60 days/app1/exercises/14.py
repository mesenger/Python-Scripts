# FREEZING_POINT = 0
# BOILING_POINT = 100

# def water_state(temperature):
#     if temperature <= FREEZING_POINT:
#         return 'ice'
#     elif temperature >= BOILING_POINT:
#         return 'steam'
#     else:
#         return 'liquid'

def water_state(temperature):
    if temperature > 25:
        return 'Hot'
    elif temperature <= 25 and temperature >= 15:
        return 'Warm'
    else:
        return 'Cold'