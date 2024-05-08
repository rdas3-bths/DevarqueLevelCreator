from tile import Tile
import random

class World:

    def __init__(self):
        self.world_map = self.generate_world()

    def generate_world(self):
        map = []
        row = 0
        y = 10
        for i in range(30):
            tiles = []
            column = 0
            x = 10
            for j in range(40):
                t = Tile(x, y, 1, row, column)
                column += 1
                x = x + 24
                tiles.append(t)
            row += 1
            y = y + 24
            map.append(tiles)
        return map

    def get_clicked_tile(self, position):
        for row in self.world_map:
            for tile in row:
                if tile.rect.collidepoint(position):
                    return tile.row, tile.column

    def count_tile_type(self, tile_type):
        count = 0
        for row in self.world_map:
            for tile in row:
                if tile.tile_type == tile_type:
                    count += 1
        return count
