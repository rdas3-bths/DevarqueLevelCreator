from tile import Tile
import random


def generate_world():
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


def get_clicked_tile(position, world_map):
    for row in world_map:
        for tile in row:
            if tile.rect.collidepoint(position):
                return tile.row, tile.column
