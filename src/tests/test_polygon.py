from geometry.polygon import Polygon
from geometry.point import Point

# class TestPolygon:
#     def test_edges_from_points(self):
#         output = Polygon.edges_from_points(
#             Point(1, 1),
#             Point(1, 5), 
#             Point(3, 5), # excluded from output 
#             Point(5, 5), # excluded from output
#             Point(7, 5),
#             Point(7, 1),
#             Point(5, 1)  # excluded from output
#         )

#         """ 

#         0         1         2         3
#         x ------- x ------- x ------- x
#         |                             |
#         |                             |
#         |                             |
#         x ----------------- x ------- x
#         6, -1               5         4

#         """

#         assert False #len(output) == 4