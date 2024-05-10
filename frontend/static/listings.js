'use strict';

const addTaskModal = document.getElementById('addTaskModal');
const editTaskModal = document.getElementById('editTaskModal');
const overlay = document.querySelector('.overlay');


function addTask() {
    addTaskModal.classList.remove('hidden');
    overlay.classList.remove('hidden');
    overlay.addEventListener('click', closeAddTask);
}

function editTask(taskId) {
    document.getElementById('edit-task-id').value = taskId;
    console.log("Received ID: " + taskId);
    editTaskModal.classList.remove('hidden');
    overlay.classList.remove('hidden');
    overlay.addEventListener('click', closeEditTask);
}

function closeAddTask() {
    addTaskModal.classList.add('hidden');
    overlay.classList.add('hidden');
    overlay.removeEventListener('click', closeAddTask);
}

function closeEditTask() {
    editTaskModal.classList.add('hidden');
    overlay.classList.add('hidden');
    overlay.removeEventListener('click', closeEditTask);
}


function completeTask() {

    if (confirm("Are you sure you want to complete this task?")) {
        return true;
    }

    return false;
    
}

function deleteTask() {

    if (confirm("Are you sure you want to delete this task?")) {
        return true;
    }

    return false;
}

function clearCompletedTasks() {

    if (confirm("Are you sure you want to clear all completed tasks?")) {
        return true;
    }

    return false;

}

function clearListedTasks() {

    if (confirm("Are you sure you want to clear all listed tasks?")) {
        return true;
    }
    
    return false;
}

document.addEventListener('keydown', function (e) {

    if (e.key === 'Escape' && !addTaskModal.classList.contains('hidden')) {
      closeAddTask();
    } else if (e.key === 'Escape' && !editTaskModal.classList.contains('hidden')) {
      closeEditTask();
    }
});
