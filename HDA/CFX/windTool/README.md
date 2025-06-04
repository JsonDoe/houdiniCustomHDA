# windTool — Custom Velocity Field HDA for Houdini

This Houdini Digital Asset (HDA) provides an artist-friendly interface to generate a custom velocity wind field inside Houdini using procedural parameters, turbulence, falloffs, and viewport visualization. It is designed to be used in simulations such as FLIP, pyro, vellum, or for visualization and development.

---

## Features

- **Custom Wind Direction & Strength**
- **Optional procedural noise (with multiple layers)**
- **Box or Input geometry-based region definition**
- **Falloff controls for localized influence**
- **Live velocity vector preview in viewport**
- **Transform handle for easy placement**

---

## How It Works

This tool creates a velocity vector field using a combination of parameters and volume operations. It generates a box or uses input geometry as the source region, scatters points inside it, and defines velocity directions per-point before rasterizing the result into a vector volume.

You can adjust direction, add layered noise, and control amplitude, frequency, and roughness per layer. A falloff system is included to fade the effect near the edges of the region.

![windTool Preview](preview/windTool_demo.gif)

---

## Parameters

### **Previsualization**
- `Preview Mode`: dropdown to enable:
  - None
  - Bounding Box preview
  - Curve-based preview
- `Vector Count`: number of vectors used for display
- `Trail Length`: visual length of the previewed velocity

### **Wind Controls**
- `Direction`: normalized vector direction
- `Strength`: scalar multiplier
- `Add Noise`: enables the first noise layer
- `Amplitude / Frequency / Offset / Roughness`: procedural noise shaping
- `Multiplier`: global multiplier for that noise layer

### **Additional Noise**
- Up to 2 additional layers of procedural noise
- Independent amplitude, frequency, and roughness controls per layer

### **Box Controls**
- `Use Input Geometry`: switch between built-in box or external input
- `Box Center`, `Size`, `Resolution`: manually define box when input is disabled

---

## Handles & Gizmos

The node includes a transform handle connected to internal translation, rotation, and scale controls. Use the gizmo in the viewport to reposition and resize the wind field.

---

## Usage

1. Drop the `WIND_tool` node into your scene
2. Optionally connect geometry to its first input to use as the domain
3. Enable visualization and tweak direction, noise, and falloff
4. Use the `OUT_VEL` output in downstream simulations or analysis

---

## Compatibility

- Houdini 19.5+
- Requires VDB module (default in most installs)
- Tested with FLIP, Pyro, and Vellum

---

## Author

Julien Miternique  
Pipeline TD & Technical Artist  
[LinkedIn](https://www.linkedin.com/in/julien-miternique/) • [GitHub](https://github.com/JsonDoe)

