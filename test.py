#coding:utf-8
import application
import mock
import unittest

class GestorDeArchivosTest(unittest.TestCase):

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

    @mock.patch('application.os.path')
    @mock.patch('__builtin__.open')
    def test_crear_archivo_inexistente(self, mock_open, mock_path):
        mock_path.isfile.return_value = False
        application.decidir_creacion("archivo_inexistente")
        mock_open.assert_called_with("archivo_inexistente", "w")

    @mock.patch('application.os.path')
    @mock.patch('__builtin__.open')
    def test_crear_archivo_existente(self, mock_open, mock_path):
        mock_path.isfile.return_value = True
        application.decidir_creacion("archivo_existente")
        self.assertFalse(mock_open.called, "Error! El archivo no debe crearse porque ya existe")


