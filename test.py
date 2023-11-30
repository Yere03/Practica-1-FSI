import unittest
import search



class ABTest(unittest.TestCase):
    """Realiza el test del camino desde A hasta B"""

    def setUp(self):
        self.ab = search.GPSProblem('A', 'B', search.romania)

    def test_breadth_first_search(self):
        bfs = search.breadth_first_graph_search(self.ab)
        self.assertEqual(bfs[1:], (21,16))
    
    def test_depth_first_search(self):
        dfs = search.depth_first_graph_search(self.ab)
        self.assertEqual(dfs[1:], (18,10))

    def test_branch_and_bound(self):
        bab = search.branch_and_bound(self.ab)
        self.assertEqual(bab[1:], (31,24))

    def test_branch_and_bound_heuristics(self):
        babh = search.branch_and_bound_heuristics(self.ab)
        self.assertEqual(babh[1:], (16,6))
        
class OETest(unittest.TestCase):
    def setUp(self):
        self.oe = search.GPSProblem('O', 'E', search.romania)

    def test_breadth_first_search(self):
        bfs = search.breadth_first_graph_search(self.oe)
        self.assertEqual(bfs[1:], (45, 43))

    def test_depth_first_search(self):
        dfs = search.depth_first_graph_search(self.oe)
        self.assertEqual(dfs[1:], (41, 31))

    def test_branch_and_bound(self):
        bab = search.branch_and_bound(self.oe)
        self.assertEqual(bab[1:], (43, 40))

    def test_branch_and_bound_heuristics(self):
        babh = search.branch_and_bound_heuristics(self.oe)
        self.assertEqual(babh[1:], (32, 15))

class GZTest(unittest.TestCase):
    def setUp(self):
        self.gz = search.GPSProblem('G', 'Z', search.romania)

    def test_breadth_first_search(self):
        bfs = search.breadth_first_graph_search(self.gz)
        self.assertEqual(bfs[1:], (41, 34))

    def test_depth_first_search(self):
        dfs = search.depth_first_graph_search(self.gz)
        self.assertEqual(dfs[1:], (32, 21))

    def test_branch_and_bound(self):
        bab = search.branch_and_bound(self.gz)
        self.assertEqual(bab[1:], (41, 34))

    def test_branch_and_bound_heuristics(self):
        babh = search.branch_and_bound_heuristics(self.gz)
        self.assertEqual(babh[1:], (26, 12))

class NDTest(unittest.TestCase):
    """Realiza el test del camino desde N hasta D"""

    def setUp(self):
        self.nd = search.GPSProblem('N', 'D', search.romania)

    def test_breadth_first_search(self):
        bfs = search.breadth_first_graph_search(self.nd)
        self.assertEqual(bfs[1:], (32,26))
    
    def test_depth_first_search(self):
        dfs = search.depth_first_graph_search(self.nd)
        self.assertEqual(dfs[1:], (31,19))

    def test_branch_and_bound(self):
        bab = search.branch_and_bound(self.nd)
        self.assertEqual(bab[1:], (32,26))

    def test_branch_and_bound_heuristics(self):
        babh = search.branch_and_bound_heuristics(self.nd)
        self.assertEqual(babh[1:], (23,12))

class MFTest(unittest.TestCase):
    def setUp(self):
        self.mf = search.GPSProblem('M', 'F', search.romania)

    def test_breadth_first_search(self):
        bfs = search.breadth_first_graph_search(self.mf)
        self.assertEqual(bfs[1:], (31, 23))

    def test_depth_first_search(self):
        dfs = search.depth_first_graph_search(self.mf)
        self.assertEqual(dfs[1:], (29, 18))

    def test_branch_and_bound(self):
        bab = search.branch_and_bound(self.mf)
        self.assertEqual(bab[1:], (36, 27))

    def test_branch_and_bound_heuristics(self):
        babh = search.branch_and_bound_heuristics(self.mf)
        self.assertEqual(babh[1:], (25, 16))

if __name__ == '__main__':
    unittest.main()