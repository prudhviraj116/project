document.getElementById('signin-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    var name = document.getElementById('name').value;
    var id = document.getElementById('id').value;
    document.getElementById('signin-section').style.display = 'none';
    document.getElementById('quiz-section').style.display = 'block';
    localStorage.setItem('username', name);
    localStorage.setItem('userid', id);
});
document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var name = localStorage.getItem('username');
    var id = localStorage.getItem('userid');
    var q1 = document.querySelector('input[name="q1"]:checked').value;
    var q2 = document.querySelector('input[name="q2"]:checked').value;
    var total = 2;
    var correct = 0;
    if (q1 === '4') correct++;
    if (q2 === '4') correct++;
    var wrong = total - correct;
    var attempted = total;
    document.getElementById('quiz-section').style.display = 'none';
    document.getElementById('result-section').style.display = 'block';
    document.getElementById('result-name').textContent = name;
    document.getElementById('result-id').textContent = id;
    document.getElementById('result-total').textContent = total;
    document.getElementById('result-correct').textContent = correct;
    document.getElementById('result-wrong').textContent = wrong;
    document.getElementById('result-attempted').textContent = attempted;
    document.getElementById('result-status').textContent = (correct === total) ? 'Pass' : 'Fail';
});
