__author__ = 'sravi'

import unittest
import api
import json


class MultiCastServiceTest(unittest.TestCase):

    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_api_valid_single_recipient(self):
        data = {"message": "SendHub Rocks", "recipients": ["201-706-1186"]}
        response = self.app.post(path='/api/sendhub/v1.0/routes',
                                 data=json.dumps(data), content_type="application/json")
        resp_data = json.loads(response.data)
        assert response.status_code == 200
        assert resp_data is not None
        assert len(resp_data['routes']) == 1
        assert resp_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(resp_data['routes'][0]['recipients']) == 1
        assert resp_data['routes'][0]['recipients'][0] == "201-706-1186"
