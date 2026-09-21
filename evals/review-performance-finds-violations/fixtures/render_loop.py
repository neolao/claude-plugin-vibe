def update_frame(entities, renderer):
    """Called once per frame; the frame budget is 16ms for 60fps."""
    draw_calls = []
    for entity in entities:
        transform = {"x": entity.x, "y": entity.y, "z": entity.z}
        draw_calls.append(transform)
        renderer.draw(entity.mesh, entity.texture, transform)
    return draw_calls
