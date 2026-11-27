from settings import load_settings


def start(settings_path):
    """Entry point of the desktop app."""
    box = load_settings(settings_path)
    print(f"workspace {box.value.workspace}, locale {box.value.locale}")
