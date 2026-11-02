# Knot Generator

![knot-thumb](https://github.com/user-attachments/assets/685ac825-2578-4f92-8e78-3e513d4812a2)

**Author:** The French Monkey (TFMSTYLE)  
**Version:** 1.0.3  

---

## Overview

The Knot Generator creates mathematically precise 3D knots based on classical and parametric equations.  
It includes a wide range of topological knots — from simple torus knots to complex Celtic and pretzel knots — all generated procedurally.  
Each knot is defined by tunable geometric parameters such as twist, radius, segment density, and scale variation, allowing for both scientific and artistic applications.  
Perfect for use in abstract design, modeling practice, rope simulation, or mathematical visualization.

---

## Parameters

### Live Update
When enabled, automatically updates the knot geometry whenever a parameter changes.  
Useful for visual iteration, though it may reduce performance for high segment counts.

---

### Knot Type
Determines the mathematical formula and structural pattern of the knot.  
Available options include:

- **Trefoil (3₁):** Simplest non-trivial knot; forms a classic three-lobed loop.  
- **Figure Eight (4₁):** Symmetrical four-crossing knot with an elegant looping shape.  
- **Cinquefoil (5₁):** Five-crossing torus knot (2,5); produces a floral looping pattern.  
- **Three-Twist (5₂):** Double-looped structure with three major twists.  
- **Stevedore (6₁):** Compact, industrial-style knot with six crossings.  
- **Carrick Bend:** Decorative eight-crossing knot often used in rope designs.  
- **Septafoil (7₁):** Seven-fold torus knot, forming a detailed looping symmetry.  
- **Granny Knot:** Composite knot consisting of two overhand knots linked together.  
- **Torus Knot (p,q):** General toroidal form defined by two integer winding parameters.  
- **Pretzel Knot:** Extended variation with adjustable p/q ratios for twisted multi-loop forms.  
- **Celtic Knot:** Decorative interwoven pattern based on sinusoidal and radial modulation.

---

### Radius
Defines the overall scale of the knot.  
Larger values expand the knot’s size proportionally.

---

### Curve Segments
Controls the resolution of the underlying curve.  
Higher values produce smoother shapes but increase polygon count.

---

### Thickness
Determines the tube radius used to create the knot’s body.  
Adjust this to simulate rope thickness or to fine-tune visual proportions.

---

### Circle Segments
Number of segments used to form the circular cross-section of the tube.  
Higher values result in smoother and rounder geometry.

---

### Twist
Applies a continuous rotational twist along the length of the knot.  
Measured in full turns, where 1.0 equals a 360° rotation.

---

### Scale Variation
Adds periodic modulation to the knot’s cross-sectional scale.  
Use this to simulate organic thickness variation or rope tension.

---

### Complexity
Modifies the oscillation frequency for knots that use sinusoidal variation (e.g., Celtic and decorative types).  
Higher values create more intricate surface patterns.

---

### P Parameter
For torus and pretzel knots, defines the longitudinal winding count — how many times the curve loops around the torus axis.

---

### Q Parameter
For torus and pretzel knots, defines the meridional winding count — how many times the curve passes through the torus hole.

---

### Bights
Used for Turk’s Head and related patterns (if implemented).  
Specifies the number of scalloped arcs or “bights” around the circumference.

---

### Leads
Defines the number of parallel strands or “leads” within the woven structure.

---

## Operators

### Generate Knot
Creates a new knot based on the current parameters, or regenerates the selected one if it was produced by the Knot Generator.  
Automatically names the object according to the chosen knot type.

---

## Usage Notes

- The **Knot Type** determines the mathematical model used to generate the shape.  
- Adjust **Radius**, **Segments**, and **Thickness** for scale and detail.  
- Use **Twist** and **Scale Variation** to add stylistic or natural irregularities.  
- For torus and pretzel types, experiment with **P** and **Q** parameters to create unique looping configurations.  
- Enable **Live Update** to see changes instantly while tuning parameters.  
- Generated geometry is clean, manifold, and suitable for rendering, simulation, or further mesh editing.  
- Combining procedural knots with materials or displacement textures can produce realistic rope or wire structures.

---

## Install

Needs Blender 4.2 or later. Get the zip from [tfmstyle.com](https://tfmstyle.com), then in Blender open Edit > Preferences > Get Extensions, open the menu at the top right and pick Install from Disk.

To build the zip yourself, run this in the repo folder:

```bash
blender --command extension build
```

The addon is `__init__.py`, plus `relay_updater.py` for its update checks. It depends on nothing but Blender.

---

## License

GPL 3.0 or later. See [LICENSE](LICENSE).
