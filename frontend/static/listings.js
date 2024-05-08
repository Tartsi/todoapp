'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');


function addTask() {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
}

function closeTask() {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
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

overlay.addEventListener('click', closeTask);

document.addEventListener('keydown', function (e) {

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeTask();
    }
});
