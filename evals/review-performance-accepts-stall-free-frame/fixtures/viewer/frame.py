import json

from viewer import gpu, picking

_ROWS_PER_FRAME = 256


class Viewer:
    def __init__(self, scene):
        self.scene = scene
        self.picker = picking.Picker()
        self._shaders = {}
        self._uploads = []

    def load(self):
        """Called once when the scene is opened, before its first frame."""
        with open("camera.json") as f:
            self.scene.camera.apply(json.load(f))
        for material in self.scene.materials:
            self._shaders[material.name] = gpu.compile_shader(material.vertex_source, material.fragment_source)
        for texture in self.scene.textures:
            handle = gpu.create_texture(texture.width, texture.height)
            texture.handle = handle
            self._uploads.append((handle, texture.rows, 0))

    def frame(self, cursor):
        """Called once per frame by the window's redraw callback."""
        self.picker.collect()
        self._upload_some_rows()

        for mesh in self.scene.meshes:
            gpu.draw(mesh.buffers, self._shaders[mesh.material.name])

        self.picker.request(cursor)

    def _upload_some_rows(self):
        if not self._uploads:
            return
        handle, rows, first_row = self._uploads[0]
        last_row = min(first_row + _ROWS_PER_FRAME, len(rows))
        gpu.upload_texture_rows(handle, first_row, rows[first_row:last_row])
        if last_row == len(rows):
            self._uploads.pop(0)
        else:
            self._uploads[0] = (handle, rows, last_row)
