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

function clearListedTasks() {

    if (confirm("Are you sure you want to clear all listed tasks?")) {
        console.log("Clearing all tasks");
        return true;
    }
    
    console.log("Not clearing tasks");
    return false;

}

overlay.addEventListener('click', closeTask);

document.addEventListener('keydown', function (e) {

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeTask();
    }
});
