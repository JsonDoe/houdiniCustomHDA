# Camera-Driven Reparent with Transform Transfer (Houdini Solaris + USD)

This Houdini Python LOP script procedurally transfers translation and Y-axis rotation from any camera (or `Xformable` prim) to a target prim via an intermediate `Xform` hierarchy.

It is designed for non-destructive layout control, where lighting or environmental objects need to follow camera movement with override capability.

## Features

* Extracts world transform from a source camera
* Applies weighted Y-rotation and translation (no scale)
* Creates a 3-tier hierarchy:

  ```
  /<target>_ctrl                      # driven by camera
  /<target>_ctrl/extra_offset         # editable manual override
  /<target>_ctrl/extra_offset/<target> # final target prim
  ```
* Non-destructive: original prim attributes and metadata are preserved
* Houdini-compatible: avoids unsupported USD Python APIs

## Use Case Examples

![demo](preview/demo_python_LOp_custom_parent.gif)

* Driving a dome light's orientation and position from a tracked camera
* Aligning volumetrics or FX emitters with animated cameras
* Adding override control on top of auto-aligned assets

## Parameters

| Variable           | Description                                           |
| ------------------ | ----------------------------------------------------- |
| `SOURCE_PRIM_PATH` | The driving camera or Xformable prim path             |
| `TARGET_PRIM_PATH` | The original target prim path to be reparented        |
| `TRANSFORM_WEIGHT` | Blend ratio for rotation and translation (0.0 to 1.0) |

## Output Hierarchy

If `TARGET_PRIM_PATH = "/scene/light"`, the output hierarchy will be:

```
/scene/light_ctrl
/scene/light_ctrl/extra_offset
/scene/light_ctrl/extra_offset/light
```

## Requirements

* Houdini 20.0+ with Solaris
* Python Script LOP context
* Valid USD camera and target prim on stage input

## Notes

* No scale is extracted or applied to maintain clean USD transform stack
* If the target prim is already under the final path, no reparenting occurs
* Reparenting is performed via attribute and metadata duplication
* This script is meant to be dropped inside a Python Script LOP

## License

This script is provided as-is under the MIT License. You are free to modify and use it in production environments.
