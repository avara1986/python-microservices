import json
import os
import unittest
from typing import Dict, List, Union, Text

from project import create_app


def _format_response(response: Text = "") -> Union[List, Dict]:
    return json.loads(response)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        os.environ["ENVIRONMENT"] = "test"
        self.app, self.db = create_app()
        self.base_url = self.app.config["APPLICATION_ROOT"]
        self.client = self.app.test_client()

    def tearDown(self):
        os.unlink(self.app.config['DATABASE'])

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
