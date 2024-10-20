const startButton = document.getElementById('generate-board');
startButton.addEventListener('click', function(){
    const boardTable = document.getElementById('boardTable')
    boardTable.style.display = 'block';
    startButton.style.display = 'none';
});
