_transform_buffer = []


def update_frame(entities, renderer, batches_by_texture):
    """Called once per frame; the frame budget is 16ms for 60fps. Reuses the
    module-level buffer instead of allocating, and batches draw calls by
    texture instead of issuing one per entity."""
    _transform_buffer.clear()
    for entity in entities:
        _transform_buffer.append(entity.transform)
        batches_by_texture[entity.texture].append(entity.mesh)

    renderer.upload_transforms(_transform_buffer)
    for texture, meshes in batches_by_texture.items():
        renderer.draw_batch(texture, meshes)
