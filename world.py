from tile import Tile
import random


def generate_world():
    map = []
    column = 0
    y = 10
    for i in range(30):
        tiles = []
        row = 0
        x = 10
        for i in range(40):
            t = Tile(x, y, 1, row, column)
            row += 1
            x = x + 24
            tiles.append(t)
        column += 1
        y = y + 24
        map.append(tiles)
    return map


def check_tile_clicked(position, world_map):
    for row in world_map:
        for tile in row:
            if tile.rect.collidepoint(position):
                print(tile.row, tile.column)
