from pxr import UsdGeom, Usd, Gf, Sdf
import math

# === Stage Access ===
node = hou.pwd()
input_stage = node.inputs()[0].stage()
stage = node.editableStage()

# === CONFIGURATION PARAMETERS ===
SOURCE_PRIM_PATH = "/camera"                # Any Xformable prim (typically a camera)
TARGET_PRIM_PATH = "/scene/light"           # Any prim to follow the source transform
TRANSFORM_WEIGHT = 0.5                        # Influence factor for blending transform

# === Derived Paths ===
ctrl_path = TARGET_PRIM_PATH + "_ctrl"
extra_path = ctrl_path + "/extra_offset"
final_path = extra_path + "/" + TARGET_PRIM_PATH.split("/")[-1]

# === Get source world transform ===
src_prim = UsdGeom.Xformable(input_stage.GetPrimAtPath(SOURCE_PRIM_PATH))
world_xform = src_prim.ComputeLocalToWorldTransform(hou.frame())

# === Extract Y-axis rotation and translation ===
translate = world_xform.ExtractTranslation() * TRANSFORM_WEIGHT
rot_y_rad = math.atan2(world_xform[0][2], world_xform[2][2])
rot_y_deg = math.degrees(rot_y_rad) * TRANSFORM_WEIGHT

# === Compose transform matrix (no scale) ===
mat = Gf.Matrix4d().SetRotate(Gf.Rotation(Gf.Vec3d(0, 1, 0), rot_y_deg))
mat.SetTranslateOnly(translate)

# === Create or update camera-driven controller ===
ctrl_prim = stage.GetPrimAtPath(ctrl_path)
if not ctrl_prim.IsValid():
    ctrl_prim = stage.DefinePrim(ctrl_path, "Xform")

xform_ctrl = UsdGeom.Xformable(ctrl_prim)
xform_ctrl.ClearXformOpOrder()
xform_ctrl.AddTransformOp().Set(mat)

# === Create manual override controller (if not existing) ===
extra_prim = stage.GetPrimAtPath(extra_path)
if not extra_prim.IsValid():
    stage.DefinePrim(extra_path, "Xform")

# === Reparent target prim under override hierarchy ===
dst_prim = stage.GetPrimAtPath(TARGET_PRIM_PATH)
if dst_prim.IsValid() and dst_prim.GetPath() != final_path:
    new_prim = stage.DefinePrim(final_path, dst_prim.GetTypeName())

    for attr in dst_prim.GetAttributes():
        new_attr = new_prim.CreateAttribute(attr.GetName(), attr.GetTypeName())
        val = attr.Get()
        if val is not None:
            new_attr.Set(val)

    metadata_dict = dst_prim.GetAllMetadata()
    for key, value in metadata_dict.items():
        new_prim.SetMetadata(key, value)

    stage.RemovePrim(dst_prim.GetPath())