# test_task_manager.py
import unittest
from task_manager import TaskManager, TaskStatus

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tm = TaskManager()

    def test_add_task_successfully(self):
        # REQ-01 / TEST-01
        task_id = self.tm.add_task("Comprar pão", "Ir à padaria da esquina.")
        task = self.tm.get_task(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(task.name, "Comprar pão")
        self.assertEqual(task.description, "Ir à padaria da esquina.")
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)

    def test_reject_task_with_empty_name(self):
        # REQ-01 / TEST-02
        with self.assertRaisesRegex(ValueError, "O nome da tarefa não pode ser vazio."):
            self.tm.add_task("", "Descrição qualquer.")

    def test_mark_task_as_completed(self):
        # REQ-02 / TEST-03
        task_id = self.tm.add_task("Estudar TDD", "Ler os slides da aula.")
        result = self.tm.mark_as_completed(task_id)
        task = self.tm.get_task(task_id)
        self.assertTrue(result)
        self.assertEqual(task.status, TaskStatus.COMPLETED)

    def test_cannot_mark_already_completed_task(self):
        # REQ-02 / TEST-04
        task_id = self.tm.add_task("Tarefa", "Descrição")
        self.tm.mark_as_completed(task_id)
        result = self.tm.mark_as_completed(task_id)
        self.assertFalse(result)

    def test_mark_task_as_in_progress_validation(self):
        # REQ-03 / TEST-05 (Agora testa a validação)
        task_id = self.tm.add_task("Tarefa Inicial", "Desc")
        # A função reopen não retorna um booleano, apenas valida.
        # Se nenhuma exceção for levantada, o teste passa.
        self.tm.mark_as_in_progress(task_id)
        task = self.tm.get_task(task_id)
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        
    def test_cannot_mark_completed_task_as_in_progress(self):
        # REQ-03 / TEST-06
        task_id = self.tm.add_task("Tarefa finalizada", "Esta tarefa não deve ser reaberta.")
        self.tm.mark_as_completed(task_id)
        with self.assertRaisesRegex(ValueError, "Não é possível alterar o status de uma tarefa concluída."):
            self.tm.mark_as_in_progress(task_id)

    def test_edit_existing_task(self):
        # REQ-04 / TEST-07
        task_id = self.tm.add_task("Nome Antigo", "Descrição Antiga")
        self.tm.edit_task(task_id, "Nome Novo", "Descrição Nova")
        task = self.tm.get_task(task_id)
        self.assertEqual(task.name, "Nome Novo")
        self.assertEqual(task.description, "Descrição Nova")

    def test_edit_non_existent_task(self):
        # REQ-04 / TEST-08
        with self.assertRaisesRegex(ValueError, "Tarefa com ID 999 não encontrada."):
            self.tm.edit_task(999, "Nome", "Desc")

    def test_delete_task_successfully(self):
        # REQ-05 / TEST-09
        task_id = self.tm.add_task("Para deletar", "...")
        result = self.tm.delete_task(task_id)
        task = self.tm.get_task(task_id)
        self.assertTrue(result)
        self.assertIsNone(task)

    def test_delete_non_existent_task(self):
        # REQ-05 / TEST-10
        with self.assertRaisesRegex(ValueError, "Tarefa com ID 999 não encontrada."):
            self.tm.delete_task(999)

if __name__ == '__main__':
    unittest.main()