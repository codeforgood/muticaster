__author__ = 'sravi'

import unittest
import api
import json


class MultiCasterFunctionalTest(unittest.TestCase):

    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_api_valid_single_recipient(self):
        data = {"message": "SendHub Rocks", "recipients": ["201-706-1185"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 1
        assert resp_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(resp_data['routes'][0]['recipients']) == 1
        assert resp_data['routes'][0]['recipients'][0] == "201-706-1185"

    def test_api_valid_2_recipient(self):
        data = {"message": "SendHub Rocks", "recipients": ["201-706-1185", "551-208-6869"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 2

    def test_api_valid_4_recipient(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 4
        assert resp_data['routes'][0]['ip'] == "10.0.1.1"
        assert resp_data['routes'][1]['ip'] == "10.0.1.2"
        assert resp_data['routes'][2]['ip'] == "10.0.1.3"
        assert resp_data['routes'][3]['ip'] == "10.0.1.4"
        assert resp_data['routes'][0]['recipients'][0] == "201-706-1185"
        assert resp_data['routes'][1]['recipients'][0] == "551-208-6869"
        assert resp_data['routes'][2]['recipients'][0] == "123-406-1385"
        assert resp_data['routes'][3]['recipients'][0] == "541-208-6869"

    def test_api_valid_5_recipient_3(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869",
                               "541-208-6860"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 1
        assert resp_data['routes'][0]['ip'] == "10.0.2.1"
        assert len(resp_data['routes'][0]['recipients']) == 5

    def test_api_valid_6_recipient_4(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869",
                               "541-208-6860", "541-208-6867"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 2
        assert resp_data['routes'][0]['ip'] == "10.0.2.1"
        assert resp_data['routes'][1]['ip'] == "10.0.1.1"
        assert len(resp_data['routes'][0]['recipients']) == 5
        assert len(resp_data['routes'][1]['recipients']) == 1

    def test_api_valid_12_recipient_4(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869",
                               "541-108-6860", "541-200-6867",
                               "541-108-6861", "541-202-6864",
                               "541-108-6862", "541-203-6865",
                               "541-108-6863", "541-205-6866"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 3
        assert resp_data['routes'][0]['ip'] == "10.0.3.1"
        assert resp_data['routes'][1]['ip'] == "10.0.1.1"
        assert resp_data['routes'][2]['ip'] == "10.0.1.2"
        assert len(resp_data['routes'][0]['recipients']) == 10
        assert len(resp_data['routes'][1]['recipients']) == 1
        assert len(resp_data['routes'][2]['recipients']) == 1

    def test_api_valid_25_recipient_4(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869",
                               "541-108-6860", "541-200-6867",
                               "541-108-6861", "541-202-6864",
                               "541-108-6862", "541-203-6865",
                               "541-108-6863", "541-205-6866",
                               "301-706-1185", "351-208-6869",
                               "323-406-1385", "341-208-6869",
                               "341-108-6860", "341-200-6867",
                               "341-108-6861", "341-202-6864",
                               "341-108-6862", "341-203-6865",
                               "341-108-6863", "341-205-6866",
                               "441-205-6866"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 1
        assert resp_data['routes'][0]['ip'] == "10.0.4.1"
        assert len(resp_data['routes'][0]['recipients']) == 25

    def test_api_valid_26_recipient_4(self):
        data = {"message": "SendHub Rocks",
                "recipients": ["201-706-1185", "551-208-6869",
                               "123-406-1385", "541-208-6869",
                               "541-108-6860", "541-200-6867",
                               "541-108-6861", "541-202-6864",
                               "541-108-6862", "541-203-6865",
                               "541-108-6863", "541-205-6866",
                               "301-706-1185", "351-208-6869",
                               "323-406-1385", "341-208-6869",
                               "341-108-6860", "341-200-6867",
                               "341-108-6861", "341-202-6864",
                               "341-108-6862", "341-203-6865",
                               "341-108-6863", "341-205-6866",
                               "441-205-6866", "641-205-6866"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 2
        assert resp_data['routes'][0]['ip'] == "10.0.4.1"
        assert resp_data['routes'][1]['ip'] == "10.0.1.1"
        assert len(resp_data['routes'][0]['recipients']) == 25
        assert len(resp_data['routes'][1]['recipients']) == 1

    def test_api_invalid_uri(self):
        data = {"message": "SendHub Rocks", "recipients": ["201-706-1185", "551-208-6869"]}
        response = self.app.post(path='/api/sendhub/v2.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 404

    def test_api_invalid_json_body(self):
        data = None
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_1(self):
        data = {"message": "SendHub Rocks", "recipients": []}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_2(self):
        data = {"message": "SendHub Rocks", "recipients": [123, 345]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_3(self):
        data = {"message": 123, "recipients": []}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_4(self):
        data = {"message": "SendHub Rocks", "recipients": ["201-706-1185", "201-706-1185"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_5(self):
        data = {"message": "SendHub Rocks", "recipients": "201-706-1185"}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_6(self):
        data = {"message": "SendHub Rocks"}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_7(self):
        data = {"recipients": ["201-706-1185"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400

    def test_api_invalid_schema_8(self):
        data = {"message": "SendHub Rocks", "recipients": ["20-706-1185"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        assert response.status_code == 400