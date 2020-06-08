#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    ACT0001 = bgelogic.ActionApplyLocation()
    ACT0002 = bgelogic.ActionPlayAction()
    CON0003 = bgelogic.ConditionOnInit()
    CON0000.key_code = bge.events.AKEY
    CON0000.pulse = True
    ACT0001.local = True
    ACT0001.condition = CON0000
    ACT0001.game_object = "Object:Sphere.001"
    ACT0001.movement = mathutils.Vector((0.05999999865889549, 0.0, 0.0))
    ACT0002.condition = CON0003
    ACT0002.game_object = "Object:Armature"
    ACT0002.action_name = "idle"
    ACT0002.stop = False
    ACT0002.start_frame = 100.0
    ACT0002.end_frame = 180.0
    ACT0002.layer = 0
    ACT0002.priority = 0
    ACT0002.play_mode = bge.logic.KX_ACTION_MODE_LOOP
    ACT0002.layer_weight = 1.0
    ACT0002.speed = 1.0
    ACT0002.blendin = 0.0
    ACT0002.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    network.add_cell(CON0000)
    network.add_cell(CON0003)
    network.add_cell(ACT0001)
    network.add_cell(ACT0002)
    owner["player_main"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__player_main')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("player_main")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
