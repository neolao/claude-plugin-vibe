package helpdesk.mobile

// Rendering of ticket statuses in the mobile client.
enum class Status(val label: String) {
    OPEN("Open"),
    WAITING("Waiting"),
    RESOLVED("Resolved"),
    CLOSED("Closed"),
    UNKNOWN("Other");

    companion object {
        fun fromWire(value: String): Status =
            values().firstOrNull { it.name.equals(value, ignoreCase = true) } ?: UNKNOWN
    }
}
