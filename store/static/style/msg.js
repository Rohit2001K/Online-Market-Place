document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.querySelector('.messages');

    if (messagesContainer) {
        messagesContainer.classList.add('show');
        setTimeout(() => {
            messagesContainer.classList.remove('show');
        }, 1000);
    }
});
