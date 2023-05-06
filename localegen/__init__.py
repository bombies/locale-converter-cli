__app_name__ = "localegen"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    ILLEGAL_LANGUAGE_ERROR,
) = range(4)

ERRORS = {
    DIR_ERROR: "Failed to create config directory.",
    FILE_ERROR: "Failed to create config file.",
    ILLEGAL_LANGUAGE_ERROR: "Illegal language code."
}
