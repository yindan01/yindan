from test_requests2.api.department import Department
from test_requests2.api.wework import Wework


class TestDepartment():
    def setup_class(self):
        wework=Wework()
        self.department=Department()
        self.token=wework.get_token()

    def test_department(self):
        self.department.create_department(self.token,3)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"] == "葛莱芬多"

    def test_update_department(self):
        self.department.update_department(self.token,3)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"] == "广州研发中心"
    def test_delete_department(self):
        list = self.department.get_department_list(self.token)
        self.department.delete_department(self.token,3)
        assert len(list["department"]) == 2
    def test_get_department_list(self):
         self.department.get_department_list(self.token)


