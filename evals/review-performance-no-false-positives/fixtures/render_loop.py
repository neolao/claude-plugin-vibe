_transform_buffer = []
_meshes_by_texture = {}


def load_level(level):
    """Called once when a level loads, before its first frame."""
    _meshes_by_texture.clear()
    for texture in level.textures:
        _meshes_by_texture[texture] = []


def update_frame(entities, renderer):
    """Called once per frame; the frame budget is 16ms for 60fps."""
    _transform_buffer.clear()
    for meshes in _meshes_by_texture.values():
        meshes.clear()

    for entity in entities:
        _transform_buffer.append(entity.transform)
        _meshes_by_texture[entity.texture].append(entity.mesh)

    renderer.upload_transforms(_transform_buffer)
    for texture, meshes in _meshes_by_texture.items():
        if meshes:
            renderer.draw_batch(texture, meshes)
