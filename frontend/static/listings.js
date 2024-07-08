'use strict';

const addTaskModal = document.getElementById('addTaskModal');
const editTaskModal = document.getElementById('editTaskModal');
const todayContainer = document.querySelector('.container');
const completedContainer = document.querySelector('.container-completed');
const tabToday = document.getElementById('today');
const tabCompleted = document.getElementById('completed');
const overlay = document.querySelector('.overlay');


function switchCompleted() {

    if (tabToday.disabled) {
        tabToday.disabled = false;
    }

    tabCompleted.classList.toggle('active');
    tabToday.classList.toggle('active');
    completedContainer.classList.toggle('hidden');
    todayContainer.classList.toggle('hidden');
    tabCompleted.disabled = true;
}

function switchToday() {

    if (tabCompleted.disabled) {
        tabCompleted.disabled = false;
    }

    tabToday.classList.toggle('active');
    tabCompleted.classList.toggle('active');
    todayContainer.classList.toggle('hidden');
    completedContainer.classList.toggle('hidden');
    tabToday.disabled = true;
}

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
