import math
from inspection import print_local_variables

# https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity
wire_r_l_coeff = {  'silver' : 0.0000000159,
                    'copper' : 0.0000000168,
                    'aluminium' : 0.0000000172}
wire_r_t_coeff = {  'silver' : 0.0038,
                    'copper' : 0.00404,
                    'aluminium' : 0.0039}
# https://nepsi.com/resources/calculators/short-time-current-rating-of-conductor.htm
wire_t_i_coeff = {  'copper' : 0.0297,
                    'aluminium' : 0.0125}






def calc_wire_loading_time(temp1=30, temp2=130, area_mmsq=2.5, current=25, material='copper'):
    # no dissipation
    time = wire_t_i_coeff[material] * math.log10((1.0*temp2+234)/(1.0*temp1+234)) * math.pow(1973.52524139*area_mmsq, 2) * math.pow(current, -2)

    print_local_variables()
    return time

def calc_voltage_drop(temp_deg=130, length=25, area_mmsq=2.5, current=32, material='copper'):
    voltage = (1 + wire_r_t_coeff[material]*(temp_deg-20)) * wire_r_l_coeff[material] * current * length / (0.000001*area_mmsq)    

    print_local_variables()
    return voltage

calc_voltage_drop()
calc_wire_loading_time()