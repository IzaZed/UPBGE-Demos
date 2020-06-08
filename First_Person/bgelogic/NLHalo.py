#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionOnUpdate()
    PAR0001 = bgelogic.ParamOwnerObject()
    PAR0002 = bgelogic.ParameterObjectAttribute()
    ACT0003 = bgelogic.ActionAlignAxisToVector()
    PAR0002.game_object = "Object:Sphere"
    PAR0002.attribute_name = "worldPosition"
    ACT0003.condition = CON0000
    ACT0003.game_object = PAR0001
    ACT0003.vector = PAR0002
    ACT0003.axis = 2
    ACT0003.factor = 1.0
    network.add_cell(CON0000)
    network.add_cell(PAR0002)
    network.add_cell(PAR0001)
    network.add_cell(ACT0003)
    owner["Halo"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Halo')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Halo")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
