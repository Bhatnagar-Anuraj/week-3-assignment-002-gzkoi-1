"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import scene_functions as sf

# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# ---------------------------------------------------------------------------
# tODO: Build your scene below by calling functions from scene_functions.
#
# Example calls (uncomment and modify once your functions are implemented):
#
#   sf.create_building(width=5, height=10, depth=5, position=(-10, 0, 8))
#   sf.create_tree(position=(3, 0, -5))
#   sf.create_fence(length=12, post_count=7, position=(-6, 0, -3))
#   sf.create_lamp_post(position=(8, 0, 2))
#
#   # Place 8 trees in a circle of radius 15:
#   sf.place_in_circle(sf.create_tree, count=8, radius=15)
#
# Remember: call each function at least once, and aim for 15+ objects.
# ---------------------------------------------------------------------------


# Reset scene
cmds.file(new=True, force=True)

# Ground
ground = cmds.polyPlane(name="ground", w=60, h=60)[0]

# Buildings
sf.create_building(6, 12, 6, (-10, 0, 10))
sf.create_building(5, 9, 5, (-2, 0, 10))
sf.create_building(7, 14, 7, (8, 0, 10))

# Create trees
sf.create_tree(position=(-12, 0, -5))
sf.create_tree(position=(-8, 0, -6))
sf.create_tree(position=(-10, 0, -8))

# create fence
sf.create_fence(length=12, post_count=6, position=(-14, 0, -10))

# create lamp posts
sf.create_lamp_post(position=(-5, 0, 2))
sf.create_lamp_post(position=(0, 0, 2))
sf.create_lamp_post(position=(5, 0, 2))

# circular tree layout for center area
sf.place_in_circle(sf.create_tree, count=8, radius=12)


# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
