#coding:utf-8
import application
import mock
import unittest

class BorrarTestCase(unittest.TestCase):

    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_archivo_inexistente(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        application.eliminar_archivo("archivo_inexistente")
        self.assertFalse(mock_os.remove.called, "Error! El archivo no debería eliminarse porque no existe")


    @mock.patch('application.os.path')
    @mock.patch('application.os')
    def test_eliminar_archivo_existente(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        application.eliminar_archivo("archivo_existente")
        mock_os.remove.assert_called_with("archivo_existente")

#Esta es la que no sivio
#class CrearTestCase(unittest.TestCase):

#    @mock.patch('application.os.path')
#    @mock.patch('application.os')
#    def test_crear_archivo(self, mock_os, mock_path):
#        mock_path.isfile.return_value = False
#        application.decidir_creacion('archivo_inexistente')
#        self.assertTrue(mock_os.open.called, "Error! El archivo no deberia eliminarse porque no existe")

