

def convert_ISO8601_to_seconds(duration: str) -> int:
    """Convert ISO 8601 duration format to seconds.

    Args:
        duration (str): The duration in ISO 8601 format.

    Returns:
        int: The duration in seconds.
    """

    duration = duration.replace("PT", "")

    hours, minutes, seconds = 0, 0, 0
    if "H" in duration:
        hours = int(duration.split("H")[0])
        duration = duration.split("H")[1]
    if "M" in duration:
        minutes = int(duration.split("M")[0])
        duration = duration.split("M")[1]
    if "S" in duration:
        seconds = int(duration.split("S")[0])
    return hours * 3600 + minutes * 60 + seconds