'use strict';

const modal = document.querySelector('modal');
const overlay = document.querySelector('overlay');


function addTask() {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
}

function closeTask() {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
}

// Add possibility to close Add-task window with 'Escape' button
// TODO: Finish JS

document.addEventListener('keydown', function (e) {

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal();
    }
});
