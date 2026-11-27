import json

from viewer import gpu, picking


class Viewer:
    def __init__(self, scene):
        self.scene = scene
        self.hovered = None
        self._shaders = {}

    def frame(self, cursor):
        """Called once per frame by the window's redraw callback."""
        with open("camera.json") as f:
            camera = json.load(f)
        self.scene.camera.apply(camera)

        for mesh in self.scene.meshes:
            shader = self._shaders.get(mesh.material.name)
            if shader is None:
                shader = gpu.compile_shader(mesh.material.vertex_source, mesh.material.fragment_source)
                self._shaders[mesh.material.name] = shader
            gpu.draw(mesh.buffers, shader)

        self.hovered = picking.object_under_cursor(cursor)
