#MACHINE GENERATED
import bge
import mathutils
import bgelogic
import math

def _initialize(owner):
    network = bgelogic.LogicNetwork()
    CON0000 = bgelogic.ConditionKeyPressed()
    CON0001 = bgelogic.ConditionKeyPressed()
    CON0002 = bgelogic.ConditionKeyPressed()
    CON0003 = bgelogic.ConditionKeyPressed()
    ACT0004 = bgelogic.ActionSetGlobalValue()
    ACT0005 = bgelogic.ActionSetGlobalValue()
    ACT0006 = bgelogic.ActionSetGlobalValue()
    ACT0007 = bgelogic.ActionSetGlobalValue()
    CON0008 = bgelogic.ConditionOr()
    CON0009 = bgelogic.ConditionOr()
    ACT0010 = bgelogic.InvertBool()
    ACT0011 = bgelogic.InvertBool()
    ACT0012 = bgelogic.ActionSetGlobalValue()
    ACT0013 = bgelogic.ActionSetGlobalValue()
    PAR0014 = bgelogic.ParameterGetGlobalValue()
    PAR0015 = bgelogic.ParameterGetGlobalValue()
    PAR0016 = bgelogic.ParameterVector3Simple()
    PAR0017 = bgelogic.ParameterVectorMath()
    PAR0018 = bgelogic.ParameterSimpleValue()
    PAR0019 = bgelogic.ParameterArithmeticOp()
    CON0020 = bgelogic.ConditionOnUpdate()
    PAR0021 = bgelogic.ParamOwnerObject()
    ACT0022 = bgelogic.ActionApplyLocation()
    PAR0023 = bgelogic.GetSensor()
    ACT0024 = bgelogic.ActionSetGameObjectGameProperty()
    ACT0025 = bgelogic.ActionSetGameObjectVisibility()
    PAR0026 = bgelogic.SensorValue()
    ACT0027 = bgelogic.ActionSetGameObjectVisibility()
    PAR0028 = bgelogic.ParameterObjectProperty()
    ACT0029 = bgelogic.ActionExecuteNetwork()
    CON0030 = bgelogic.ConditionOnUpdate()
    ACT0031 = bgelogic.ActionMouseLook()
    CON0032 = bgelogic.ConditionOnce()
    CON0000.key_code = bge.events.WKEY
    CON0000.pulse = True
    CON0001.key_code = bge.events.SKEY
    CON0001.pulse = True
    CON0002.key_code = bge.events.AKEY
    CON0002.pulse = True
    CON0003.key_code = bge.events.DKEY
    CON0003.pulse = True
    ACT0004.condition = CON0000
    ACT0004.data_id = "movement"
    ACT0004.persistent = False
    ACT0004.key = "x"
    ACT0004.value = 1
    ACT0005.condition = CON0001
    ACT0005.data_id = "movement"
    ACT0005.persistent = False
    ACT0005.key = "x"
    ACT0005.value = -1
    ACT0006.condition = CON0002
    ACT0006.data_id = "movement"
    ACT0006.persistent = False
    ACT0006.key = "y"
    ACT0006.value = 1
    ACT0007.condition = CON0003
    ACT0007.data_id = "movement"
    ACT0007.persistent = False
    ACT0007.key = "y"
    ACT0007.value = -1
    CON0008.condition_a = ACT0004.OUT
    CON0008.condition_b = ACT0005.OUT
    CON0009.condition_a = ACT0006.OUT
    CON0009.condition_b = ACT0007.OUT
    ACT0010.value = CON0008
    ACT0011.value = CON0009
    ACT0012.condition = ACT0010.OUT
    ACT0012.data_id = "movement"
    ACT0012.persistent = False
    ACT0012.key = "x"
    ACT0012.value = 0
    ACT0013.condition = ACT0011.OUT
    ACT0013.data_id = "movement"
    ACT0013.persistent = False
    ACT0013.key = "y"
    ACT0013.value = 0
    PAR0014.data_id = "movement"
    PAR0014.key = "x"
    PAR0015.data_id = "movement"
    PAR0015.key = "y"
    PAR0016.input_x = PAR0014
    PAR0016.input_y = PAR0015
    PAR0016.input_z = 0.0
    PAR0017.op = 'normalize'
    PAR0017.vector = PAR0016.OUTV
    PAR0017.vector_2 = mathutils.Vector((0.0, 0.0, 0.0))
    PAR0017.factor = 0.0
    PAR0018.value = 0.05000000074505806
    PAR0019.operator = bgelogic.ParameterArithmeticOp.op_by_code("MUL")
    PAR0019.operand_a = PAR0017
    PAR0019.operand_b = PAR0018
    ACT0022.local = True
    ACT0022.condition = CON0020
    ACT0022.game_object = PAR0021
    ACT0022.movement = PAR0019
    PAR0023.obj_name = bgelogic.GetSensor.obj("Object:Sphere")
    PAR0023.sens_name = bgelogic.GetSensor.sens("Collision")
    ACT0024.condition = PAR0023
    ACT0024.game_object = "Object:Sphere"
    ACT0024.property_name = "has_gun"
    ACT0024.property_value = True
    ACT0025.condition = PAR0023
    ACT0025.game_object = PAR0026.VAL
    ACT0025.visible = False
    ACT0025.recursive = True
    PAR0026.obj_name = bgelogic.SensorValue.obj("Object:Sphere")
    PAR0026.sens_name = bgelogic.SensorValue.sens("Collision")
    PAR0026.field = "hitObject"
    ACT0027.condition = CON0032
    ACT0027.game_object = "Object:Walther"
    ACT0027.visible = True
    ACT0027.recursive = True
    PAR0028.game_object = "Object:Sphere"
    PAR0028.property_name = "has_gun"
    ACT0029.condition = PAR0028
    ACT0029.target_object = "Object:Sphere"
    ACT0029.tree_name = 'Gun'
    ACT0031.condition = CON0030
    ACT0031.game_object_x = "Object:Sphere"
    ACT0031.game_object_y = "Object:Empty"
    ACT0031.inverted = False
    ACT0031.sensitivity = 1.0
    ACT0031.use_cap_z = False
    ACT0031.cap_z = mathutils.Vector((0.0, 0.0))
    ACT0031.use_cap_y = True
    ACT0031.cap_y = mathutils.Vector((80.0, 80.0))
    CON0032.input_condition = PAR0028
    CON0032.repeat = False
    network.add_cell(CON0000)
    network.add_cell(CON0002)
    network.add_cell(ACT0004)
    network.add_cell(ACT0006)
    network.add_cell(PAR0014)
    network.add_cell(PAR0018)
    network.add_cell(CON0020)
    network.add_cell(PAR0023)
    network.add_cell(PAR0026)
    network.add_cell(PAR0028)
    network.add_cell(CON0030)
    network.add_cell(CON0032)
    network.add_cell(CON0001)
    network.add_cell(ACT0005)
    network.add_cell(CON0008)
    network.add_cell(ACT0010)
    network.add_cell(ACT0012)
    network.add_cell(PAR0015)
    network.add_cell(PAR0021)
    network.add_cell(ACT0024)
    network.add_cell(ACT0027)
    network.add_cell(ACT0031)
    network.add_cell(CON0003)
    network.add_cell(PAR0016)
    network.add_cell(ACT0025)
    network.add_cell(ACT0007)
    network.add_cell(PAR0017)
    network.add_cell(ACT0029)
    network.add_cell(CON0009)
    network.add_cell(PAR0019)
    network.add_cell(ACT0011)
    network.add_cell(ACT0022)
    network.add_cell(ACT0013)
    owner["FPS_Main"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NODELOGIC__FPS_Main')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("FPS_Main")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
