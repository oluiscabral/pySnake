from pySnake.config import GeneralConfig
import typing
from pySnake.display import Display
from pySnake.displays.game_display.game.grid.unit import Unit

class Grid(Display):
    def __init__(self, config: GeneralConfig, parent: 'Display', pos: typing.Tuple[int,int], size: typing.Tuple[int,int], grid_unit: int):
        super().__init__(config, parent, pos, size, True)
        size = self.get_size()
        x_units = size[0] // grid_unit
        y_units = size[1] // grid_unit
        
        x_units_coverage = x_units * grid_unit
        y_units_coverage = y_units * grid_unit
        
        x_units_coverage_remain = size[0] - x_units_coverage
        y_units_coverage_remain = size[1] - y_units_coverage
        
        x_displacement = x_units_coverage_remain // 2
        y_displacement = y_units_coverage_remain // 2
        
        actual_x = self.get_x() + x_displacement
        actual_y = self.get_y() + y_displacement
        
        units = []
        
        for i,y in enumerate(range(actual_y, y_units_coverage + 1, grid_unit)):
            units.append([])
            for x in range(actual_x, x_units_coverage + 1, grid_unit):
                units[i].append(Unit(self.get_surface(), self, (x, y), (grid_unit, grid_unit)))
        
        for line in units:
            self.add_childs(line)
    
