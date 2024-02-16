class BaseDocumentedException(Exception):

    PACKAGE_NAME = "documented_exception"

    PACKAGE_URL = "https://github.com/Ni-g-3l/documented-exception"

    HEADER = ""

    FOOTER = f"""\n\t
        If this is an issue with '{PACKAGE_NAME}', feel free to submit report here:
        {PACKAGE_URL}/issues/new
    """

    def __init__(self, message: str = None) -> None:
        if not message:
            formated_doc = self.__doc__.replace("\n", "\n    ")
            message = f'\t{formated_doc}'
        if self.HEADER:
            error_message = f"{self.HEADER}\n{message}{self.FOOTER}"
        else:
            error_message = f"{message}{self.FOOTER}"
        super(BaseDocumentedException, self).__init__(
            error_message
        )

__all__ = ['BaseDocumentedException']