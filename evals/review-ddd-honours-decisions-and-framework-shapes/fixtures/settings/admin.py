# Called by the admin page's preferences form.
from settings.preferences import PreferencesRepository


def update_preferences(repo: PreferencesRepository, form: dict) -> None:
    prefs = repo.get()
    prefs.shop_name = form["shop_name"]
    prefs.support_email = form["support_email"]
    prefs.currency = form["currency"]
    prefs.items_per_page = int(form["items_per_page"])
    repo.save(prefs)
