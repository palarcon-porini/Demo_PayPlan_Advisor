import GraphColection.PayPlan.Function as f
from GraphColection.PayPlan.Graph import Graph ,Node

class PayPlan_Graph:
    def __init__(self) -> None:
        self.node : Node = {
            'START': f.START,
            'BASE_GENERATE': f.BASE_GENERATE,
            'SPLIT_DOCUMENTS': f.SPLIT_DOCUMENTS,
            'DECIDE_TO_GENERATE': f.DECIDE_TO_GENERATE,
        }
        self.graph = Graph(self.node)

    def invoke(self, state):
        return self.graph.invoke(state)
