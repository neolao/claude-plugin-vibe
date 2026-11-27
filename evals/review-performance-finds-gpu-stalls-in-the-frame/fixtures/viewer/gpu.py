"""Thin layer over the graphics API. Every function here issues commands on
the render thread's context."""


def compile_shader(vertex_source, fragment_source):
    """Compiles and links a program on the GPU; returns its handle."""
    raise NotImplementedError


def draw(buffers, shader):
    """Issues one draw call for the given vertex buffers."""
    raise NotImplementedError


def read_pixels(x, y, width, height):
    """Copies a region of the current framebuffer back to the CPU, once the GPU
    has finished every command issued so far; returns the bytes."""
    raise NotImplementedError


def request_read_pixels(x, y, width, height):
    """Asks the GPU to copy a region of the current framebuffer into a staging
    buffer; returns a ticket. Nothing waits."""
    raise NotImplementedError


def read_if_ready(ticket):
    """Returns the bytes of a finished copy, or None while the GPU is still on it."""
    raise NotImplementedError


def create_texture(width, height):
    """Allocates an empty texture on the GPU; returns its handle."""
    raise NotImplementedError


def upload_texture_rows(texture, first_row, rows):
    """Uploads the given rows into the texture."""
    raise NotImplementedError
