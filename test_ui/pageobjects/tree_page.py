import test_ui.testdata.page_constants  as const
from selenium.common.exceptions import NoSuchElementException


class AnimalTree:

    def __init__(self, driver):
        self.driver = driver

    def get_ant_text_box(self):
        return self.driver.find_element_by_css_selector(const.ant_text_box_css)

    def get_all_list_items(self):
        return self.driver.find_elements_by_css_selector(const.tree_list_css)

    def find_delete_node_btn_in_list_element(self, elem):
        return elem.find_element_by_css_selector(const.delete_node_btn_css)

    def find_rat_delete_btn(self):
        try:
            elem = self.driver.find_element_by_xpath(const.rat_delete_node_xpth)
            print(f'rat element text: {elem.text}, {elem.get_attribute("label")}, {elem.get_attribute("area-label")}')
            return elem
        except NoSuchElementException:
            print(f'Rat node is not found')
            return None

    def find_tree_text(self):
        return self.driver.find_element_by_css_selector(const.whole_tree_css).text

