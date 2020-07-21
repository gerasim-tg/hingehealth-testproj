import pytest
from test_ui.base.mybase import MyBase
from test_ui.testdata import page_constants as const
from test_ui.pageobjects import tree_page
from selenium.webdriver.common.keys import Keys


@pytest.mark.ui_test
class TestTreeManipulation:

    base = MyBase()
    # animal_tree = tree_page.AnimalTree()

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        print("\nquit driver")
        cls.base.close_all()

    def test_add_delete_element(self):
        TestTreeManipulation.base.open_page(const.tree_url)
        self.animal_tree = tree_page.AnimalTree(TestTreeManipulation.base.driver)
        print(f'current url: {TestTreeManipulation.base.driver.current_url}')
        # time.sleep(3)
        txt_box = self.animal_tree.get_ant_text_box()
        txt_box.send_keys("rat")
        txt_box.send_keys(Keys.RETURN)
        # time.sleep(5)
        animals = self.animal_tree.find_tree_text()
        # verify if rat label is on the page
        assert "rat" in animals, 'Expected creation of rat element'

        elems = self.animal_tree.get_all_list_items()
        # elems = self.base.driver.find_elements_by_class_name("deleteNode")
        for each in elems:
            if "rat" in str(each.text):
                print(f'found element with text: {each.text}')
                # delete node 'rat'
                self.animal_tree.find_delete_node_btn_in_list_element(each).click()
                break

        # time.sleep(3)
        # verify that 'rat' is no longer in my tree
        assert "rat" not in self.animal_tree.find_tree_text(), f'Deletion of rat element failed, tree text: {self.animal_tree.find_tree_text()}'
