class PageFault(Exception):
    def __init__(self, v_page):
        self.v_page = v_page