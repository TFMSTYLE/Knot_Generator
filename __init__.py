# SPDX-FileCopyrightText: 2025-2026 The French Monkey
# SPDX-License-Identifier: GPL-3.0-or-later

bl_info = {
    "name": "Knot",
    "author": "The French Monkey",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Knot",
    "description": "Generate mathematical knots",
    "category": "Add Mesh",
    "license": "GPL-3.0-or-later",
}

import bpy, math
from mathutils import Vector

try:
    from . import relay_updater
except ImportError:  # the Addon Collection has its own updates
    relay_updater = None

# ------------------------------------------------------------------------
# Knot Generation Functions
# ------------------------------------------------------------------------

def torus_knot(p, q, radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        r = math.cos(q * t) + 2
        scale_factor = 1.0 + scale_variation * math.sin(p * t * 2)
        x = radius * r * math.cos(p * t) * scale_factor
        y = radius * r * math.sin(p * t) * scale_factor
        z = radius * math.sin(q * t) * scale_factor
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def figure_eight_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(4 * t)
        x = radius * (2.5 * math.cos(t) + math.cos(3*t)) / 2.5 * scale
        y = radius * (2.5 * math.sin(t) - math.sin(3*t)) / 2.5 * scale
        z = radius * math.sin(2*t) * 0.7 * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def trefoil_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(3 * t)
        r = math.cos(2 * t) + 2
        x = radius * r * math.cos(3 * t) * scale
        y = radius * r * math.sin(3 * t) * scale
        z = radius * math.sin(2 * t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def cinquefoil_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(5 * t)
        r = math.cos(2 * t) + 2
        x = radius * r * math.cos(5 * t) * scale
        y = radius * r * math.sin(5 * t) * scale
        z = radius * math.sin(2 * t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def celtic_knot(radius, segments, thickness, twist=0.0, complexity=4, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(complexity * t)
        r = 1.0 + 0.3 * math.cos(complexity * t)
        x = radius * r * math.cos(t) * scale
        y = radius * r * math.sin(t) * scale
        z = radius * 0.4 * math.sin(complexity * t) * math.cos(t * 2) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def pretzel_knot(radius, segments, thickness, p=3, q=7, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(p * t)
        x = radius * (2 + math.cos(p * t)) * math.cos(q * t) / 2 * scale
        y = radius * (2 + math.cos(p * t)) * math.sin(q * t) / 2 * scale
        z = radius * math.sin(p * t) * 0.8 * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def septafoil_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(7 * t)
        r = math.cos(2 * t) + 2
        x = radius * r * math.cos(7 * t) * scale
        y = radius * r * math.sin(7 * t) * scale
        z = radius * math.sin(2 * t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def granny_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(4 * t)
        x = radius * (2.5 + math.cos(2*t)) * math.cos(3*t) / 2.2 * scale
        y = radius * (2.5 + math.cos(2*t)) * math.sin(3*t) / 2.2 * scale
        z = radius * 1.1 * math.sin(4*t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def three_twist_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(3 * t)
        x = radius * (2 + math.cos(3 * t)) * math.cos(2 * t) * scale
        y = radius * (2 + math.cos(3 * t)) * math.sin(2 * t) * scale
        z = radius * math.sin(3 * t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def stevedore_knot(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(4 * t)
        x = radius * (2 + math.cos(2*t)) * math.cos(3*t) / 2 * scale
        y = radius * (2 + math.cos(2*t)) * math.sin(3*t) / 2 * scale
        z = radius * math.sin(4*t) * 0.6 * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def carrick_bend(radius, segments, thickness, twist=0.0, scale_variation=0.0, circle_segments=12):
    curve_verts = []
    for i in range(segments):
        t = i / segments * 2 * math.pi
        scale = 1.0 + scale_variation * math.sin(4 * t)
        x = radius * math.cos(t) * (1 + 0.5 * math.cos(4*t)) * scale
        y = radius * math.sin(t) * (1 + 0.5 * math.cos(4*t)) * scale
        z = radius * 0.4 * math.sin(4*t) * scale
        curve_verts.append(Vector((x, y, z)))
    
    return create_tube_from_curve(curve_verts, thickness, twist, circle_segments)

def create_tube_from_curve(curve_points, thickness, twist=0.0, circle_segments=12):
    verts, faces = [], []
    n = len(curve_points)
    
    tangents = [(curve_points[(i + 1) % n] - curve_points[i]).normalized() for i in range(n)]
    
    t0 = tangents[0]
    n0 = Vector((0, 0, 1)) if abs(t0.z) < 0.9 else Vector((1, 0, 0))
    n0 = (n0 - t0 * n0.dot(t0)).normalized()
    b0 = t0.cross(n0).normalized()
    frames = [(n0, b0)]
    
    for i in range(1, n):
        t_prev, t_curr = tangents[i - 1], tangents[i]
        n_prev, b_prev = frames[i - 1]
        axis = t_prev.cross(t_curr)
        if axis.length > 0.0001:
            axis, angle = axis.normalized(), math.asin(min(1.0, axis.length))
            cos_a, sin_a = math.cos(angle), math.sin(angle)
            n_new = (n_prev * cos_a + axis.cross(n_prev) * sin_a + axis * axis.dot(n_prev) * (1 - cos_a)).normalized()
            b_new = (b_prev * cos_a + axis.cross(b_prev) * sin_a + axis * axis.dot(b_prev) * (1 - cos_a)).normalized()
            frames.append((n_new, b_new))
        else:
            frames.append((n_prev, b_prev))
    
    t_last, t_first = tangents[-1], tangents[0]
    n_last, b_last = frames[-1]
    n_first, b_first = frames[0]
    axis = t_last.cross(t_first)
    if axis.length > 0.0001:
        axis, angle = axis.normalized(), math.asin(min(1.0, axis.length))
        cos_a, sin_a = math.cos(angle), math.sin(angle)
        n_trans = (n_last * cos_a + axis.cross(n_last) * sin_a + axis * axis.dot(n_last) * (1 - cos_a)).normalized()
    else:
        n_trans = n_last
    
    closure_twist = math.atan2(n_trans.dot(b_first), n_trans.dot(n_first))
    effective_twist = round(twist) if abs(twist) > 0.01 else 0
    rot_per_segment = (-closure_twist + effective_twist * 2 * math.pi) / n
    
    for i in range(n):
        p, n_vec, b_vec = curve_points[i], *frames[i]
        twist_angle = rot_per_segment * i
        if twist_angle != 0.0:
            cos_t, sin_t = math.cos(twist_angle), math.sin(twist_angle)
            n_vec, b_vec = n_vec * cos_t + b_vec * sin_t, -n_vec * sin_t + b_vec * cos_t
        for j in range(circle_segments):
            angle = j / circle_segments * 2 * math.pi
            offset = (n_vec * math.cos(angle) + b_vec * math.sin(angle)) * thickness
            verts.append(p + offset)
    
    for i in range(n):
        for j in range(circle_segments):
            v1 = i * circle_segments + j
            v2 = i * circle_segments + (j + 1) % circle_segments
            v3 = ((i + 1) % n) * circle_segments + (j + 1) % circle_segments
            v4 = ((i + 1) % n) * circle_segments + j
            faces.append([v1, v2, v3, v4])
    
    return verts, faces

def rebuild_knot(obj):
    knot_type = obj["knot_type"]
    radius = obj["radius"]
    segments = obj["segments"]
    thickness = obj["thickness"]
    circle_segments = obj.get("circle_segments", 12)
    p_param = obj.get("p_param", 3)
    q_param = obj.get("q_param", 2)
    twist = obj.get("twist", 0.0)
    scale_variation = obj.get("scale_variation", 0.0)
    complexity = obj.get("complexity", 4)
    bights = obj.get("bights", 3)
    leads = obj.get("leads", 2)
    
    if knot_type == "TREFOIL":
        verts, faces = trefoil_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "FIGURE_EIGHT":
        verts, faces = figure_eight_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "THREE_TWIST":
        verts, faces = three_twist_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "STEVEDORE":
        verts, faces = stevedore_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "CINQUEFOIL":
        verts, faces = cinquefoil_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "CARRICK_BEND":
        verts, faces = carrick_bend(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "SEPTAFOIL":
        verts, faces = septafoil_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "GRANNY":
        verts, faces = granny_knot(radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "TORUS_KNOT":
        verts, faces = torus_knot(p_param, q_param, radius, segments, thickness, twist, scale_variation, circle_segments)
    elif knot_type == "CELTIC":
        verts, faces = celtic_knot(radius, segments, thickness, twist, complexity, scale_variation, circle_segments)
    elif knot_type == "PRETZEL":
        verts, faces = pretzel_knot(radius, segments, thickness, p_param, q_param, twist, scale_variation, circle_segments)
    else:
        return False
    
    mesh = bpy.data.meshes.new("KnotMesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    
    old_mesh = obj.data
    obj.data = mesh
    
    if old_mesh and old_mesh.users == 0:
        bpy.data.meshes.remove(old_mesh)
        
    return True

def generate_knot(context):
    props = context.scene.kgen_props
    obj = context.active_object
    keys = ("knot_type", "radius", "segments", "thickness", "circle_segments", 
            "p_param", "q_param", "twist", "scale_variation", "complexity", 
            "bights", "leads")
    
    if obj and obj.type == "MESH" and "knot_generator" in obj and obj.select_get():
        for k in keys:
            obj[k] = getattr(props, k)
        rebuild_knot(obj)
        obj.name = obj.data.name = f"Knot_{props.knot_type}"
        return obj
    
    mesh = bpy.data.meshes.new("KnotMesh")
    new_obj = bpy.data.objects.new(f"Knot_{props.knot_type}", mesh)
    context.collection.objects.link(new_obj)
    context.view_layer.objects.active = new_obj
    new_obj.select_set(True)
    
    for k in keys:
        new_obj[k] = getattr(props, k)
    new_obj["knot_generator"] = True
    
    rebuild_knot(new_obj)
    return new_obj

# ------------------------------------------------------------------------
# Live Update
# ------------------------------------------------------------------------

def update_knot(self, context):
    props = context.scene.kgen_props
    if not props.live_update:
        return
        
    obj = context.active_object
    if not obj or "knot_generator" not in obj or not obj.select_get():
        return
        
    keys = ("knot_type", "radius", "segments", "thickness", "circle_segments",
            "p_param", "q_param", "twist", "scale_variation", "complexity", 
            "bights", "leads")
    
    for k in keys:
        obj[k] = getattr(props, k)
        
    rebuild_knot(obj)

# ------------------------------------------------------------------------
# UI Properties
# ------------------------------------------------------------------------

class KGProperties(bpy.types.PropertyGroup):
    live_update: bpy.props.BoolProperty(
        name="Live Update", 
        default=False,
        description="Update knot in real-time as you adjust parameters"
    )
    
    knot_type: bpy.props.EnumProperty(
        name="Knot Type",
        items=[
            ("TREFOIL", "Trefoil (3₁)", "Simplest non-trivial knot"),
            ("FIGURE_EIGHT", "Figure Eight (4₁)", "Figure-eight knot"),
            ("CINQUEFOIL", "Cinquefoil (5₁)", "Five-crossing (2,5)-torus knot"),
            ("THREE_TWIST", "Three-Twist (5₂)", "Three-twist knot"),
            ("STEVEDORE", "Stevedore (6₁)", "Stevedore knot"),
            ("CARRICK_BEND", "Carrick Bend", "Decorative 8-crossing knot"),
            ("SEPTAFOIL", "Septafoil (7₁)", "Seven-crossing (2,7)-torus knot"),
            ("GRANNY", "Granny Knot", "Composite knot"),
            ("TORUS_KNOT", "Torus Knot (p,q)", "Custom torus knot"),
            ("PRETZEL", "Pretzel Knot", "Pretzel-style knot"),
            ("CELTIC", "Celtic Knot", "Celtic weave pattern"),
        ],
        default="TREFOIL",
        update=update_knot
    )
    radius: bpy.props.FloatProperty(name="Radius", default=2.0, min=0.1, max=10.0, subtype='DISTANCE', update=update_knot, description="Overall size of the knot")
    segments: bpy.props.IntProperty(name="Curve Segments", default=128, min=16, max=2500, update=update_knot, description="Number of segments along the knot curve (higher = smoother)")
    thickness: bpy.props.FloatProperty(name="Thickness", default=0.15, min=0.01, max=1.0, subtype='DISTANCE', update=update_knot, description="Rope/cord thickness")
    circle_segments: bpy.props.IntProperty(name="Circle Segments", default=12, min=3, max=62, update=update_knot, description="Number of segments around the tube cross-section (higher = smoother)")
    twist: bpy.props.FloatProperty(name="Twist", default=0.0, min=0, max=50.0, update=update_knot, description="Add twist along the knot (rotations)")
    scale_variation: bpy.props.FloatProperty(name="Scale Variation", default=0.0, min=0.0, max=0.5, update=update_knot, description="Vary thickness along knot for organic look")
    complexity: bpy.props.IntProperty(name="Complexity", default=4, min=2, max=12, update=update_knot, description="Pattern complexity (for Celtic and Monkey Fist knots)")
    p_param: bpy.props.IntProperty(name="P Parameter", default=3, min=1, max=20, update=update_knot, description="Number of times knot winds around torus (longitudinal)")
    q_param: bpy.props.IntProperty(name="Q Parameter", default=2, min=1, max=20, update=update_knot, description="Number of times knot winds through torus hole (meridional)")
    bights: bpy.props.IntProperty(name="Bights", default=3, min=3, max=12, update=update_knot, description="Number of bights (scallops) in Turk's Head")
    leads: bpy.props.IntProperty(name="Leads", default=2, min=2, max=8, update=update_knot, description="Number of leads (strands) in Turk's Head")

# ------------------------------------------------------------------------
# Operators
# ------------------------------------------------------------------------

class KG_OT_generate(bpy.types.Operator):
    bl_idname = "kgen.generate"
    bl_label = "Generate Knot"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        generate_knot(context)
        return {"FINISHED"}

# ------------------------------------------------------------------------
# UI
# ------------------------------------------------------------------------

class VIEW3D_PT_knot_generator(bpy.types.Panel):
    bl_label = "Knot"
    bl_idname = "VIEW3D_PT_knot_generator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Knot"

    def draw(self, context):
        if relay_updater:
            relay_updater.draw(self.layout)
        layout = self.layout
        p = context.scene.kgen_props
        o = context.object

        layout.operator("kgen.generate", icon="MOD_SCREW")
        layout.prop(p, "live_update", toggle=True)

        layout.separator(factor=0.5)

        layout.prop(p, "knot_type", text="")
        layout.prop(p, "radius", slider=True)
        layout.prop(p, "segments", slider=True)
        layout.prop(p, "circle_segments", slider=True)
        layout.prop(p, "thickness", slider=True)
        layout.prop(p, "twist", slider=True)
        layout.prop(p, "scale_variation", slider=True)

        if p.knot_type in {"TORUS_KNOT", "PRETZEL"}:
            layout.separator(factor=0.5)
            layout.prop(p, "p_param", slider=True)
            layout.prop(p, "q_param", slider=True)

        if p.knot_type in {"CELTIC", "MONKEY_FIST"}:
            layout.separator(factor=0.5)
            layout.prop(p, "complexity", slider=True)

        layout.separator(factor=0.5)

        if o and o.select_get() and "knot_generator" in o:
            layout.label(text=f"Editing: {o.name}", icon="MOD_SCREW")
        else:
            layout.label(text="No knot selected", icon="INFO")

# ------------------------------------------------------------------------
# Registration
# ------------------------------------------------------------------------

classes = (
    KGProperties, 
    KG_OT_generate, 
    VIEW3D_PT_knot_generator, 
)

def register():
    if relay_updater:
        relay_updater.register("blender-knot")
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.kgen_props = bpy.props.PointerProperty(type=KGProperties)

def unregister():
    if relay_updater:
        relay_updater.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.kgen_props

if __name__ == "__main__":
    register()