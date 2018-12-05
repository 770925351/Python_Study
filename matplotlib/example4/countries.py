''' 新的pygal版本不再包括i18n库,需要自行安装 '''
''' python -m pip install --user pygal_maps_world '''
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name :
            return code
    return None        
