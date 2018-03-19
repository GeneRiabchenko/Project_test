from page_objects import PageObject, PageElement


class LogInPage(PageObject):
    login = PageElement(name='login')
    password = PageElement(name='password')
    submit = PageElement(css='body > div.app > div > div > div > button')
