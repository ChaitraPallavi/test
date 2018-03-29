from rest_framework.parsers import BaseParser

# Parser class


class InputParser(BaseParser):
    """
    parsing the custom content type to json format
    """
    media_type = 'application/vnd.contentful.management.v1+json'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream




