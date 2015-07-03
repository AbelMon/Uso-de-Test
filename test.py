#coding:utf-8
from application import eliminar_archivo
import mock
import unittest

class BorrarTestCase(unittest.TestCase):

    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_archivo(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        eliminar_archivo("archivo_inexistente")
        self.assertFalse(mock_os.remove.called, "Error! El archivo no deberia eliminarse")
