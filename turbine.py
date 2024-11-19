from logger import logger

class Turbine:
    def __init__(self, index, status):
        self.index = index
        self.status = status

def show_status_turbines(turbines):
    for turbine in turbines:
        if turbine.status:
            logger.info(f'Turbine {turbine.index} operation status: {turbine.status}')
        else:
            logger.warning(f'Turbine {turbine.index} operation status: {turbine.status}')