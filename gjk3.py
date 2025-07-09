import numpy as np
import matplotlib.pyplot as plt

# 両点の間の計算
def dist(p1, p2):
    return np.linalg.norm(p1 - p2)

# 点と線分の間の最短距離の計算および２点
def point_to_segment_distance(pt, v1, v2):
    line_vec = v2 - v1
    point_vec = pt - v1
    line_len = np.dot(line_vec, line_vec)
    if line_len == 0.0:
        return dist(pt, v1), v1  # v1 == v2 のとき，線分は点となる

    t = np.dot(point_vec, line_vec) / line_len
    t = max(0, min(1, t))  #  t が [0, 1] 内に収まる
    projection = v1 + t * line_vec
    return dist(pt, projection), projection

# 線分の間の最短距離および最短となる２点
def segment_to_segment_distance(v1, v2, u1, u2):
    """ 線分return，v1v2  u1u2 の間の最短距離および最短となる２点"""
    min_dist = float('inf')
    closest_points = (None, None)

    #  v1v2 の端点から までのu1u2 の距離
    for pt in [v1, v2]:
        d, proj = point_to_segment_distance(pt, u1, u2)
        if d < min_dist:
            min_dist = d
            closest_points = (pt, proj)

    #  u1u2 の端点から v1v2 までの距離
    for pt in [u1, u2]:
        d, proj = point_to_segment_distance(pt, v1, v2)
        if d < min_dist:
            min_dist = d
            closest_points = (proj, pt)

    return min_dist, closest_points

# 交差しているかを検証
def do_lines_intersect(p1, p2, q1, q2):
    """ p1p2 と q1q2 は交差しているか"""
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
    return ccw(p1, q1, q2) != ccw(p2, q1, q2) and ccw(p1, p2, q1) != ccw(p1, p2, q2)

# 二つの図形は交差しているか
def is_intersect(rect1, rect2):
    # 長方形を4つの辺に分ける
    edges1 = [(rect1[i], rect1[(i + 1) % 4]) for i in range(4)]
    edges2 = [(rect2[i], rect2[(i + 1) % 4]) for i in range(4)]

    # 交差している辺はあるか
    for v1, v2 in edges1:
        for u1, u2 in edges2:
            if do_lines_intersect(v1, v2, u1, u2):
                return True

    return False

# 二つの図形の間の最短距離を計算
def closest_distance(rect1, rect2):
    if is_intersect(rect1, rect2):
        return 0.0, None, None

    min_dist = float('inf')
    closest_points = (None, None)

    # 長方形を4つの辺で示す
    edges1 = [(rect1[i], rect1[(i + 1) % 4]) for i in range(4)]
    edges2 = [(rect2[i], rect2[(i + 1) % 4]) for i in range(4)]

    # 2辺ごとの間の距離
    for v1, v2 in edges1:
        for u1, u2 in edges2:
            d, points = segment_to_segment_distance(v1, v2, u1, u2)
            if d < min_dist:
                min_dist = d
                closest_points = points

    return min_dist, closest_points[0], closest_points[1]

# 可視化する
def visualize(rect1, rect2, distance, point1, point2):
    fig, ax = plt.subplots()
    rect1_plot = np.append(rect1, [rect1[0]], axis=0)  
    rect2_plot = np.append(rect2, [rect2[0]], axis=0)

    # 描画
    ax.plot(rect1_plot[:, 0], rect1_plot[:, 1], 'b-', label='Rectangle 1')
    ax.fill(rect1_plot[:, 0], rect1_plot[:, 1], color='blue', alpha=0.3)

    ax.plot(rect2_plot[:, 0], rect2_plot[:, 1], 'g-', label='Rectangle 2')
    ax.fill(rect2_plot[:, 0], rect2_plot[:, 1], color='green', alpha=0.3)

    # 点と距離を描画
    if point1 is not None and point2 is not None:
        ax.plot(*zip(*[point1, point2]), 'm--', label='Connection Line')
        ax.scatter(*point1, color='red', label='Point 1')
        ax.scatter(*point2, color='orange', label='Point 2')
        ax.text(*(point1 + point2) / 2, f'{distance:.2f}', color='purple')

    ax.legend()
    ax.set_title('Rectangles and Closest Distance')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid()
    plt.show()

# # # テスト：交差している図形
# rect1 = np.array([[0, 0], [4, 0], [4, 3], [0, 3]])  # 図形1
# rect2 = np.array([[4, 3], [4, 5], [6, 5], [6, 3]])  # 図形2

# # テスト：交差していない図形
# rect1 = np.array([[2, 0], [3, 1], [1, 3], [0, 2]])  # 図形1
# rect2 = np.array([[5, 5], [7, 5], [7, 8], [5, 8]])  # 図形2



# 最短距離計算
# # distance, point1, point2 = closest_distance(rect1, rect2)
# if distance == 0:
#     print("交差しています")
# else:
#     print(f"最短距離は {distance}")
#     print(f"最短となる２点は {point1} 和 {point2}")

# 可視化
# visualize(rect1, rect2, distance, point1, point2)
