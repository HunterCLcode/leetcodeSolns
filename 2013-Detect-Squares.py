class CountSquares:

    def __init__(self):
        self.point_map = defaultdict(list)
        self.reverse_map = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.point_map[point[0]].append(point[1])
        self.reverse_map[point[1]].append(point[0])

    def count(self, point: List[int]) -> int:
        res = 0
        for y_point in self.point_map[point[0]]:
            if y_point == point[1]: continue
            distance = abs(point[1] - y_point)
            expected_xs = [point[0] - distance, point[0] + distance]
            for x_point1 in self.reverse_map[y_point]:
                if not x_point1 in expected_xs: continue
                for x_point2 in self.reverse_map[point[1]]:
                    if x_point1 != x_point2: continue
                    res += 1
        return res
