lab = [[0, 0, 0, 0, 0],
       [-1, -1, -1, -1, 0],
       [-1, 0, 0, -1, 0],
       [-1, -1, -1, -1, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]


def filter_pos(pos: tuple, weight: int, height: int):
    x, y = pos
    return 0 <= x < weight and 0 <= y < height


def bfs(matrix: list, start_pos: tuple, end_pos: tuple):
    checked_pos = set()
    weight, height = len(matrix), len(matrix[0])
    x, y = start_pos
    must_check = list(
        filter(lambda pos: filter_pos(pos, weight, height) and matrix[pos[1]][pos[0]] != -1,
               [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]))
    while True:

        if not must_check:
            return False

        if must_check[0] == end_pos:
            return True

        x, y = must_check[0]

        checked_pos.add((x, y))

        now_pos_next_door = list(
            filter(lambda pos: filter_pos(pos, weight, height) and pos not in checked_pos and
                               matrix[pos[1]][pos[0]] != -1,
                   [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]))

        must_check = must_check[1::] + now_pos_next_door


if __name__ == '__main__':
    print(bfs(lab, (2, 2), (4, 4)))
