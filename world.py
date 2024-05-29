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
        return -1, -1

    def count_tile_type(self, tile_type):
        count = 0
        for row in self.world_map:
            for tile in row:
                if tile.tile_type == tile_type:
                    count += 1
        return count

    def draw_world(self, screen):
        for row in self.world_map:
            for tile in row:
                tile.draw_tile(screen)

    def save_world(self, file_name):
        if len(file_name) != 0:
            f = open("worlds/" + file_name, "w")
            start = False
            for row in self.world_map:
                row_data = ""
                for tile in row:
                    if tile.has_coin:
                        row_data += "C"
                    elif tile.has_enemy:
                        row_data += "W"
                    elif tile.tile_type == 0:
                        row_data += "."
                    elif tile.tile_type == 1:
                        row_data += "#"
                    elif tile.tile_type == 2:
                        if not start:
                            row_data += "S"
                            start = True
                        else:
                            row_data += "E"
                f.write(row_data + "\n")

            f.close()

    def load_world(self, file_name):
        map = []
        world_file = open("worlds/"+file_name, "r")
        for row in world_file:
            map_row = []
            for tile in row:
                if tile == ".":
                    map_row.append((0, "."))
                if tile == "#":
                    map_row.append((1, "#"))
                if tile == "S" or tile == "E":
                    map_row.append((2, "S"))
                if tile == "C":
                    map_row.append((1, "C"))
                if tile == "W":
                    map_row.append((1, "W"))
            map.append(map_row)

        for i in range(30):
            for j in range(40):
                self.world_map[i][j].set_tile(map[i][j][0])
                self.world_map[i][j].has_coin = False
                if map[i][j][1] == "C":
                    self.world_map[i][j].has_coin = True
                elif map[i][j][1] == "W":
                    self.world_map[i][j].has_enemy = True
