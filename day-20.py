import pdb
import copy
import math


class Image:
    SIDES = ["bottom", "left", "right", "top"]

    def __init__(self, file):
        self.tiles = self._read_tiles(file)
        self._corners = []

    def __repr__(self):
        tiles_wide = int(math.sqrt(len(self.tiles)))
        tile_length = 10
        reprs = ["|" for _ in range(tiles_wide * tile_length)]

        for i, tile in enumerate(self.tiles):
            min_row = math.floor(i / tiles_wide) * tile_length
            for j, row in enumerate(tile.image):
                reprs[min_row + j] += "".join(row) + "|"

        last_min_row = 0
        dash_len = tiles_wide * tile_length + tiles_wide - 1
        repr = "+" + "-" * dash_len + "+\n"
        for i, row in enumerate(reprs):
            min_row = math.floor(i / tiles_wide) * tile_length
            repr += "".join(row) + "\n"

            if min_row != last_min_row:
                repr += "+" + "-" * dash_len + "+\n"
            last_min_row = min_row
        repr += "+" + "-" * dash_len + "+\n"
        return repr

    def _read_tiles(self, file):
        tiles = []
        with open(file) as f:
            buffer = []
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    tiles.append(Tile("\n".join(buffer)))
                    buffer = []
                    continue
                buffer.append(line)

            if buffer:
                tiles.append(Tile("\n".join(buffer)))
                buffer = []
        return tiles

    def _tiles_are_neighbors(self, tile_a, tile_b):
        for side_a in self.SIDES:
            tile_a_method = getattr(tile_a, side_a)
            tile_a_value = tile_a_method()
            for side_b in self.SIDES:
                tile_b_method = getattr(tile_b, side_b)
                tile_b_value = tile_b_method()
                if tile_a_value == tile_b_value:
                    return side_a
        return None

    def arrange_tiles(self):
        pass
        # pick a corner
        # rotate it until neighbors are bottom, right
        #  this is the upper left corner
        #

    @property
    def corners(self):
        if self._corners:
            return self._corners

        max_checks = len(self.tiles)
        checks = 0
        queue = copy.copy(self.tiles)
        corners = []

        while checks < max_checks:
            current_tile = queue.pop()
            checks += 1
            neighbors = 0

            for tile in queue:
                if tile.id == current_tile.id:
                    continue
                side = self._tiles_are_neighbors(current_tile, tile)
                if side:
                    neighbors += 1
                    current_tile.neighbors[side] = tile
                    continue

                tile.flip()
                side = self._tiles_are_neighbors(current_tile, tile)
                if side:
                    neighbors += 1
                    current_tile.neighbors[side] = tile
                    continue

            if neighbors == 2:
                corners.append(current_tile)
            queue.insert(0, current_tile)

        self._corners = corners
        return self._corners


class Tile:
    def __init__(self, image):
        self.id = self._get_id(image)
        self.image = self._process_image(image)
        self.neighbors = {}

    def __repr__(self):
        rows = len(self.image)
        repr = f"Tile {self.id} is {rows} x {rows}\n"
        for row in self.image:
            repr += f"{''.join(row)}\n"
        return repr

    def _get_id(self, image):
        id = image.split("\n")[0]
        id = id.replace("Tile ", "")
        id = id.replace(":", "")
        return int(id)

    def _process_image(self, image):
        if not image:
            raise ValueError("Image undefined")

        self.image = []
        r = 0
        for row in image.split("\n")[1:]:
            c = 0
            self.image.append([])
            for col in row:
                self.image[r].append(col)
                c += 1
            r += 1
        return self.image

    def bottom(self):
        """Return the bottom row but as if rotated (reversed)."""
        row = copy.copy(self.image[-1])
        row.reverse()
        return row

    def left(self):
        """Return left row but rotated/oriented 90 degrees."""
        row = []
        i = len(self.image) - 1
        while i >= 0:
            row.append(self.image[i][0])
            i -= 1
        return row

    def right(self):
        return [row[-1] for row in self.image]

    def top(self):
        return self.image[0]

    def flip(self):
        new_image = []
        for row in self.image:
            new_image.insert(0, row)
        self.image = new_image

    def rotate(self):
        new_image = []
        r = 0
        for row in self.image:
            new_image.append([])
            for _ in row:
                new_image[r].append([])
            r += 1

        col = len(self.image) - 1
        row = 0
        for r in self.image:
            for c in r:
                new_image[row][col] = c
                row += 1
            col -= 1
            row = 0
        self.image = new_image


# test tile methods
image = Image("day-20-test.txt")
tile = image.tiles[0]

assert "".join(tile.bottom()) == "###..###.."
assert "".join(tile.left()) == ".#..#####."
assert "".join(tile.right()) == "...#.##..#"
assert "".join(tile.top()) == "..##.#..#."

tile.flip()
assert "".join(tile.image[0]) == "..###..###"

tile.rotate()
assert "".join(tile.image[0]) == ".#####..#."

# clean up after test
tile.flip()
tile.rotate()
print("flip and rotate pass")

# solve test puzzle

total = 1
for corner in image.corners:
    total *= corner.id
assert total == 20899048083289

print("test passed")

# solve part 1
image = Image("day-20-puzzle.txt")
total = 1
for corner in image.corners:
    total *= corner.id
print(f"Part 1: {total}")

# part 2

# can i simply pick 1 corner, rotate it to be the top left corner, and then
# fill it in?
for tile in image.tiles:
    print(f"tile {tile.id}, neighbors: {len(tile.neighbors)}")

# part 2

# build image array
pdb.set_trace()
