# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pywrapgraph')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pywrapgraph')
    _pywrapgraph = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pywrapgraph', [dirname(__file__)])
        except ImportError:
            import _pywrapgraph
            return _pywrapgraph
        try:
            _mod = imp.load_module('_pywrapgraph', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pywrapgraph = swig_import_helper()
    del swig_import_helper
else:
    import _pywrapgraph
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SimpleMaxFlow(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SimpleMaxFlow, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SimpleMaxFlow, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pywrapgraph.new_SimpleMaxFlow()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def AddArcWithCapacity(self, tail, head, capacity):
        return _pywrapgraph.SimpleMaxFlow_AddArcWithCapacity(self, tail, head, capacity)

    def NumNodes(self):
        return _pywrapgraph.SimpleMaxFlow_NumNodes(self)

    def NumArcs(self):
        return _pywrapgraph.SimpleMaxFlow_NumArcs(self)

    def Tail(self, arc):
        return _pywrapgraph.SimpleMaxFlow_Tail(self, arc)

    def Head(self, arc):
        return _pywrapgraph.SimpleMaxFlow_Head(self, arc)

    def Capacity(self, arc):
        return _pywrapgraph.SimpleMaxFlow_Capacity(self, arc)
    OPTIMAL = _pywrapgraph.SimpleMaxFlow_OPTIMAL
    POSSIBLE_OVERFLOW = _pywrapgraph.SimpleMaxFlow_POSSIBLE_OVERFLOW
    BAD_INPUT = _pywrapgraph.SimpleMaxFlow_BAD_INPUT
    BAD_RESULT = _pywrapgraph.SimpleMaxFlow_BAD_RESULT

    def Solve(self, source, sink):
        return _pywrapgraph.SimpleMaxFlow_Solve(self, source, sink)

    def OptimalFlow(self):
        return _pywrapgraph.SimpleMaxFlow_OptimalFlow(self)

    def Flow(self, arc):
        return _pywrapgraph.SimpleMaxFlow_Flow(self, arc)

    def GetSourceSideMinCut(self):
        return _pywrapgraph.SimpleMaxFlow_GetSourceSideMinCut(self)

    def GetSinkSideMinCut(self):
        return _pywrapgraph.SimpleMaxFlow_GetSinkSideMinCut(self)

    def SetArcCapacity(self, arc, capacity):
        return _pywrapgraph.SimpleMaxFlow_SetArcCapacity(self, arc, capacity)
    __swig_destroy__ = _pywrapgraph.delete_SimpleMaxFlow
    __del__ = lambda self: None
SimpleMaxFlow_swigregister = _pywrapgraph.SimpleMaxFlow_swigregister
SimpleMaxFlow_swigregister(SimpleMaxFlow)

class MinCostFlowBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MinCostFlowBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MinCostFlowBase, name)
    __repr__ = _swig_repr
    NOT_SOLVED = _pywrapgraph.MinCostFlowBase_NOT_SOLVED
    OPTIMAL = _pywrapgraph.MinCostFlowBase_OPTIMAL
    FEASIBLE = _pywrapgraph.MinCostFlowBase_FEASIBLE
    INFEASIBLE = _pywrapgraph.MinCostFlowBase_INFEASIBLE
    UNBALANCED = _pywrapgraph.MinCostFlowBase_UNBALANCED
    BAD_RESULT = _pywrapgraph.MinCostFlowBase_BAD_RESULT
    BAD_COST_RANGE = _pywrapgraph.MinCostFlowBase_BAD_COST_RANGE

    def __init__(self):
        this = _pywrapgraph.new_MinCostFlowBase()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pywrapgraph.delete_MinCostFlowBase
    __del__ = lambda self: None
MinCostFlowBase_swigregister = _pywrapgraph.MinCostFlowBase_swigregister
MinCostFlowBase_swigregister(MinCostFlowBase)

class SimpleMinCostFlow(MinCostFlowBase):
    __swig_setmethods__ = {}
    for _s in [MinCostFlowBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SimpleMinCostFlow, name, value)
    __swig_getmethods__ = {}
    for _s in [MinCostFlowBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SimpleMinCostFlow, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pywrapgraph.new_SimpleMinCostFlow()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def AddArcWithCapacityAndUnitCost(self, tail, head, capacity, unit_cost):
        return _pywrapgraph.SimpleMinCostFlow_AddArcWithCapacityAndUnitCost(self, tail, head, capacity, unit_cost)

    def SetNodeSupply(self, node, supply):
        return _pywrapgraph.SimpleMinCostFlow_SetNodeSupply(self, node, supply)

    def Solve(self):
        return _pywrapgraph.SimpleMinCostFlow_Solve(self)

    def SolveMaxFlowWithMinCost(self):
        return _pywrapgraph.SimpleMinCostFlow_SolveMaxFlowWithMinCost(self)

    def OptimalCost(self):
        return _pywrapgraph.SimpleMinCostFlow_OptimalCost(self)

    def MaximumFlow(self):
        return _pywrapgraph.SimpleMinCostFlow_MaximumFlow(self)

    def Flow(self, arc):
        return _pywrapgraph.SimpleMinCostFlow_Flow(self, arc)

    def NumNodes(self):
        return _pywrapgraph.SimpleMinCostFlow_NumNodes(self)

    def NumArcs(self):
        return _pywrapgraph.SimpleMinCostFlow_NumArcs(self)

    def Tail(self, arc):
        return _pywrapgraph.SimpleMinCostFlow_Tail(self, arc)

    def Head(self, arc):
        return _pywrapgraph.SimpleMinCostFlow_Head(self, arc)

    def Capacity(self, arc):
        return _pywrapgraph.SimpleMinCostFlow_Capacity(self, arc)

    def Supply(self, node):
        return _pywrapgraph.SimpleMinCostFlow_Supply(self, node)

    def UnitCost(self, arc):
        return _pywrapgraph.SimpleMinCostFlow_UnitCost(self, arc)
    __swig_destroy__ = _pywrapgraph.delete_SimpleMinCostFlow
    __del__ = lambda self: None
SimpleMinCostFlow_swigregister = _pywrapgraph.SimpleMinCostFlow_swigregister
SimpleMinCostFlow_swigregister(SimpleMinCostFlow)

class LinearSumAssignment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LinearSumAssignment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LinearSumAssignment, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pywrapgraph.new_LinearSumAssignment()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def AddArcWithCost(self, left_node, right_node, cost):
        return _pywrapgraph.LinearSumAssignment_AddArcWithCost(self, left_node, right_node, cost)

    def NumNodes(self):
        return _pywrapgraph.LinearSumAssignment_NumNodes(self)

    def NumArcs(self):
        return _pywrapgraph.LinearSumAssignment_NumArcs(self)

    def LeftNode(self, arc):
        return _pywrapgraph.LinearSumAssignment_LeftNode(self, arc)

    def RightNode(self, arc):
        return _pywrapgraph.LinearSumAssignment_RightNode(self, arc)

    def Cost(self, arc):
        return _pywrapgraph.LinearSumAssignment_Cost(self, arc)
    OPTIMAL = _pywrapgraph.LinearSumAssignment_OPTIMAL
    INFEASIBLE = _pywrapgraph.LinearSumAssignment_INFEASIBLE
    POSSIBLE_OVERFLOW = _pywrapgraph.LinearSumAssignment_POSSIBLE_OVERFLOW

    def Solve(self):
        return _pywrapgraph.LinearSumAssignment_Solve(self)

    def OptimalCost(self):
        return _pywrapgraph.LinearSumAssignment_OptimalCost(self)

    def RightMate(self, left_node):
        return _pywrapgraph.LinearSumAssignment_RightMate(self, left_node)

    def AssignmentCost(self, left_node):
        return _pywrapgraph.LinearSumAssignment_AssignmentCost(self, left_node)
    __swig_destroy__ = _pywrapgraph.delete_LinearSumAssignment
    __del__ = lambda self: None
LinearSumAssignment_swigregister = _pywrapgraph.LinearSumAssignment_swigregister
LinearSumAssignment_swigregister(LinearSumAssignment)


def DijkstraShortestPath(node_count, start_node, end_node, graph, disconnected_distance):
    return _pywrapgraph.DijkstraShortestPath(node_count, start_node, end_node, graph, disconnected_distance)
DijkstraShortestPath = _pywrapgraph.DijkstraShortestPath

def BellmanFordShortestPath(node_count, start_node, end_node, graph, disconnected_distance):
    return _pywrapgraph.BellmanFordShortestPath(node_count, start_node, end_node, graph, disconnected_distance)
BellmanFordShortestPath = _pywrapgraph.BellmanFordShortestPath

def AStarShortestPath(node_count, start_node, end_node, graph, heuristic, disconnected_distance):
    return _pywrapgraph.AStarShortestPath(node_count, start_node, end_node, graph, heuristic, disconnected_distance)
AStarShortestPath = _pywrapgraph.AStarShortestPath
# This file is compatible with both classic and new-style classes.


