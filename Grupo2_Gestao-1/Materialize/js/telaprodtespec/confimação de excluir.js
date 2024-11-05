function openModal() {
    document.getElementById('modal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}

function confirmDelete() {
    // Aqui você pode adicionar a lógica para excluir o produto
    closeModal();

}