class TextRepeater:
    def __init__(self, mode, section_body, format_options=[], section_header='', section_footer='', header='', 
                 footer='', indentation=0):
    """
    mode
        The mode parameter defines what will guide the repetition. Valid input for this are tuples with two elements:
        the first element is a string with the value "range" or "iterable"; the second element depends on the first
        (see below).
        "range": When mode is set to range, the second element of the tuple is an integer (n). The integer n is passed
                to the range(n) function to define the number of iterations. For example, mode=("range", 10) would use 
                'for i in range(10):' for the loop. This would generate the same section n times.
        "iterable": When mode is set to iterable, the second element of the tuple is an iterable python object. The
                intended use case is to allow iterating over a list of values to use as variables in a text block. For
                example, ("iterable", ["dogs", "cats", "spam", "eggs"]) would use for i in ["dogs", "cats", "spam", 
                "eggs"]: for the loop. This allows references to this in the format_options parameter (see below).
    section_body
    format_options
    section_header
    section_footer
    header
    footer
    indentation
    """
        pass
        
    def build_section(self):
        pass
    
    def 