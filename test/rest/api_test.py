import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.request import urlopen, HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/subtract/5/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-16"  
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 500, f"Error inesperado: {e}")
        except Exception as e:
            self.fail(f"Error en la petición API a {url}: {e}")

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_log10_0(self):
        url = f"{BASE_URL}/calc/log10/0"  
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 500, f"Error inesperado: {e}")
        except Exception as e:
            self.fail(f"Error en la petición API a {url}: {e}")

    def test_api_invalid_parameter(self):
        url = f"{BASE_URL}/calc/add/2/abc" 
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400, f"Error inesperado: {e}")
        except Exception as e:
            self.fail(f"Error en la petición API a {url}: {e}")


if __name__ == "__main__":
    unittest.main()

