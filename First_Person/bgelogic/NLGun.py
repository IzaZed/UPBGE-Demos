#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    ACT0000 = bgelogic.ActionPlayAction()
    ACT0001 = bgelogic.ActionStopAnimation()
    CON0002 = bgelogic.ConditionMousePressed()
    PAR0003 = bgelogic.ParameterObjectAttribute()
    PAR0004 = bgelogic.ParameterObjectAttribute()
    ACT0005 = bgelogic.ActionApplyImpulse()
    ACT0006 = bgelogic.ActionSetObjectAttribute()
    ACT0007 = bgelogic.ActionAddObject()
    ACT0008 = bgelogic.ActionRayPick()
    ACT0000.condition = ACT0001.OUT
    ACT0000.game_object = "Object:Gun_Bones"
    ACT0000.action_name = "Fire"
    ACT0000.stop = True
    ACT0000.start_frame = 0.0
    ACT0000.end_frame = 7.0
    ACT0000.layer = 0
    ACT0000.priority = 0
    ACT0000.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0000.layer_weight = 1.0
    ACT0000.speed = 1.0
    ACT0000.blendin = 0.0
    ACT0000.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0001.condition = CON0002
    ACT0001.game_object = "Object:Gun_Bones"
    ACT0001.action_layer = 0
    CON0002.mouse_button_code = bge.events.LEFTMOUSE
    CON0002.pulse = False
    PAR0003.game_object = "Object:Nozzle"
    PAR0003.attribute_name = "worldPosition"
    PAR0004.game_object = "Object:Aim"
    PAR0004.attribute_name = "worldPosition"
    ACT0005.local = False
    ACT0005.condition = ACT0008
    ACT0005.game_object = ACT0008.PICKED_OBJECT
    ACT0005.point = ACT0008.POINT
    ACT0005.impulse = ACT0008.DIRECTION
    ACT0006.condition = ACT0007.OUT
    ACT0006.game_object = ACT0007.OBJ
    ACT0006.attribute_value = ACT0008.POINT
    ACT0006.value_type = 'worldPosition'
    ACT0007.condition = ACT0008
    ACT0007.name = "HIT"
    ACT0007.life = 10
    ACT0008.condition = CON0002
    ACT0008.origin = PAR0003
    ACT0008.destination = PAR0004
    ACT0008.property_name = ""
    ACT0008.distance = 100.0
    network.add_cell(CON0002)
    network.add_cell(PAR0004)
    network.add_cell(ACT0001)
    network.add_cell(ACT0000)
    network.add_cell(PAR0003)
    network.add_cell(ACT0008)
    network.add_cell(ACT0005)
    network.add_cell(ACT0007)
    network.add_cell(ACT0006)
    owner["Gun"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__Gun')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("Gun")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
