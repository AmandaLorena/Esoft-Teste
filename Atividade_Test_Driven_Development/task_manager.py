# task_manager.py
from enum import Enum

class TaskStatus(Enum):
    """Define os status possíveis para uma tarefa de forma segura."""
    IN_PROGRESS = "em andamento"
    COMPLETED = "concluída"

class Task:
    """Representa uma única tarefa como um objeto."""
    def __init__(self, task_id: int, name: str, description: str):
        if not name or not name.strip():
            raise ValueError("O nome da tarefa não pode ser vazio.")
        
        self.id = task_id
        self.name = name
        self.description = description
        self.status = TaskStatus.IN_PROGRESS

    def complete(self) -> bool:
        """Marca a tarefa como concluída. Retorna True se o status foi alterado."""
        if self.status != TaskStatus.COMPLETED:
            self.status = TaskStatus.COMPLETED
            return True
        return False

    def reopen(self):
        """Tenta reabrir uma tarefa. Levanta um erro se a tarefa já estiver concluída."""
        if self.status == TaskStatus.COMPLETED:
            raise ValueError("Não é possível alterar o status de uma tarefa concluída.")
        # Como a única outra opção é IN_PROGRESS, não há mudança de estado real aqui,
        # mas a validação é o ponto principal.
        return self.status == TaskStatus.IN_PROGRESS

    def update(self, new_name: str, new_description: str):
        """Atualiza o nome e a descrição da tarefa."""
        if not new_name or not new_name.strip():
            raise ValueError("O nome da tarefa não pode ser vazio.")
        self.name = new_name
        self.description = new_description

class TaskManager:
    """Gerencia uma coleção de objetos Task."""
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, name: str, description: str) -> int:
        task_id = self._next_id
        new_task = Task(task_id, name, description)
        self._tasks[task_id] = new_task
        self._next_id += 1
        return task_id

    def get_task(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def mark_as_completed(self, task_id: int) -> bool:
        task = self._tasks.get(task_id)
        return task.complete() if task else False

    def mark_as_in_progress(self, task_id: int):
        task = self._tasks.get(task_id)
        if not task:
            raise ValueError(f"Tarefa com ID {task_id} não encontrada.")
        task.reopen()

    def edit_task(self, task_id: int, new_name: str, new_description: str) -> bool:
        task = self._tasks.get(task_id)
        if not task:
            raise ValueError(f"Tarefa com ID {task_id} não encontrada.")
        task.update(new_name, new_description)
        return True

    def delete_task(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            raise ValueError(f"Tarefa com ID {task_id} não encontrada.")
        del self._tasks[task_id]
        return True